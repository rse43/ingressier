#!/bin/python
# -*- coding:utf-8 -*-

import logging
import webapp2
import re

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from model import ItemDestroyActivity
from model import LinkDestroyActivity

from bs4 import BeautifulSoup

class NotificationMailHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        logging.info(mail_message.original)
        owner_regex = re.compile('([a-zA-Z0-9]+?),<br/>')
        link_regex = re.compile("Your Link has been destroyed by (.*?) at (.*?) hrs. \- \<a href\=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)\&z=3D19\">View start location\<\/a\> - <a href=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)&z=3D19\">View end location<\/a>")
        item_regex = re.compile("(\d+?) (.+?) were destroyed by (.*?) at (.*?) hrs. \- \<a href\=3D\"http:\/\/www\.ingress\.com\/intel\?latE6=3D(.*?)&lngE6=3D(.*?)\&z=3D19\">View location\<\/a\>")
        for content_type, body in mail_message.bodies('text/html'):
            decoded_html = str(BeautifulSoup(body.decode()))

            owner_match = owner_regex.match(decoded_html)
            owner = "Unknown"
            if owner_match:
                owner = owner_match.group(1)
            
            match = activity_regex.findall(decoded_html)
            for group in match:
                attacker = group[1]
                attack_hours = float(group[2].split(':')[0]) + float(int(group[2].split(':')[0])/100)
                start_latitude = float(group[3])/100000
                start_longitude = float(group[4])/100000
                end_latitude = float(group[5])/100000
                end_longitude = float(group[6])/100000
                link_start_location = GeoPt(lat=start_latitude, lon=start_longitude)
                link_end_location = GeoPt(lat=end_latitude, lon=end_longitude)
                activity = LinkDestroyActivity(link_creator=owner, attacker=attacker, attack_hours=attack_hours, link_start_location=link_start_location, link_end_location=link_end_location)
                activity.put()

            match = item_regex.findall(decoded_html)
            for group in match:
                item_amount = int(group[1])
                item_type = group[2]
                attacker = group[3]
                attack_hours = float(group[4].split(':')[0]) + float(int(group[4].split(':')[0])/100)
                latitude = float(group[5])/100000
                longitude = float(group[6])/100000
                item_location = GeoPt(lat=latitude, lon=longitude)
                activity = ItemDestroyActivity(item_owner=owner, item_amount=item_amount, item_type=item_type, attacker=attacker, attack_hours=attack_hours, item_location=item_location)
                activity.put()


logging.getLogger().setLevel(logging.INFO)
app = webapp2.WSGIApplication([NotificationMailHandler.mapping()], debug=False)


def real_main():
    """ main for wsgi app """
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()