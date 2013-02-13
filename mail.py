#!/bin/python
# -*- coding:utf-8 -*-

import logging
import webapp2
import re
import pickle
import datetime

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext import db

from google.appengine.api import mail
from google.appengine.api import taskqueue

from model import ItemDestroyActivity
from model import LinkDestroyActivity
from model import Message

from bs4 import BeautifulSoup

class NotificationMailHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        decoded_html = ""

        confirmation_subject_regex = re.compile('.*Gmail Forwarding Confirmation \- Receive Mail from (.*)')

        sender_match = confirmation_subject_regex.match(mail_message.subject)
        if sender_match:
            for content_type, body in mail_message.bodies('text/plain'):
                decoded_text = body.decode()
                logging.info(decoded_text)
                
                reply_email = sender_match.group(1)
                link_match = re.search('(^https://.*?mail.google.com/mail/.*$)', decoded_text, re.MULTILINE)
                if link_match:
                    link = link_match.group(1)
                    sender_address = "Sydney Resistance Watch <info@sydneyresistancewatch.appspotmail.com>"
                    subject = "Gmail Forwarding Confirmation - to info@sydneyresistancewatch.appspotmail.com"
                    body = """
                        Please confirm your forwarding setting by
                        clicking on the link below:

                        %s
                        """ % link

                    mail.send_mail(sender_address, reply_email, subject, body)

        try:
            owner_regex = re.compile('([a-zA-Z0-9]+?),<br/>')
            link_regex = re.compile("Your Link has been destroyed by (.*?) at (.*?) hrs\..*?<a href\=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)&.*?lngE6=(.*?)&.*?\">View start location\<\/a\>.*?<a href=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)&.*?lngE6=(.*?)&.*?\">View end location<\/a>")
            item_regex = re.compile("(\d+?) ([a-zA-Z0-9()]+?) were destroyed by (.*?) at (.*?) hrs\..*?<a href\=\"http:\/\/www\.ingress\.com\/intel\?latE6=(.*?)&.*?lngE6=(.*?)&.*?\">View location\<\/a\>")
            for content_type, body in mail_message.bodies('text/html'):
                decoded_html = body.decode()

                owner_match = owner_regex.match(decoded_html)
                owner = "Unknown"
                if owner_match:
                    owner = owner_match.group(1)
                else:
                    logging.debug(decoded_html)
                
                match = link_regex.findall(decoded_html)
                for group in match:
                    attacker = group[0]
                    attack_time = datetime.time(hour=int(group[1].split(':')[0]), minute=int(group[1].split(':')[1]))
                    start_latitude = float(group[2])/1000000
                    start_longitude = float(group[3])/1000000
                    end_latitude = float(group[4])/1000000
                    end_longitude = float(group[5])/1000000
                    link_start_location = db.GeoPt(lat=start_latitude, lon=start_longitude)
                    link_end_location = db.GeoPt(lat=end_latitude, lon=end_longitude)
                    activity = LinkDestroyActivity(link_creator=owner, attacker=attacker, attack_time=attack_time, link_start_location=link_start_location, link_end_location=link_end_location)
                    activity.put()

                match = item_regex.findall(decoded_html)
                for group in match:
                    item_amount = int(group[0])
                    item_type = group[1]
                    attacker = group[2]
                    attack_time = datetime.time(hour=int(group[3].split(':')[0]), minute=int(group[3].split(':')[1]))
                    latitude = float(group[4])/1000000
                    longitude = float(group[5])/1000000
                    item_location = db.GeoPt(lat=latitude, lon=longitude)
                    activity = ItemDestroyActivity(item_owner=owner, item_amount=item_amount, item_type=item_type, attacker=attacker, attack_time=attack_time, item_location=item_location)
                    activity.put()
                    taskqueue.add(url='/notifications/check', params={ 'lat' : str(latitude),
                                                                        'lon' : str(longitude),
                                                                        'attacker' : attacker})
        except Exception, e:
            logging.debug(mail_message.original)
            logging.debug(decoded_html)
            message = Message(mail=pickle.dumps(mail_message), analyzed=False)
            message.put()
            raise e


logging.getLogger().setLevel(logging.DEBUG)
app = webapp2.WSGIApplication([NotificationMailHandler.mapping()], debug=False)


def real_main():
    """ main for wsgi app """
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()