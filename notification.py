#!/bin/python
# -*- coding:utf-8 -*-

import logging
import webapp2
import os
import math

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from google.appengine.api import users
from google.appengine.api import search
from google.appengine.api import xmpp

from model import NotificationSetting

def create_document(email, latitude, longitude):
    return search.Document(
        fields=[search.TextField(name='email', value=email),
                search.GeoField(name='centre', value=GeoPoint(latitude=latitude, longitude=longitude))])


def calc_distance(origin, destination):
    lat1 = origin.lat
    lon1 = origin.lon
    lat2 = destination.lat
    lon2 = destination.lon
    radius = 6367500
 
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
 
    return d

class CheckHandler(webapp2.RequestHandler):
    def get(self):
        latitude = float(self.request.get('lat').strip())
        longitude = float(self.request.get('lon').strip())
        attacker = self.request.get('attacker').strip()
        target_location = db.GeoPt(lat=latitude, lon=longitude)
        query_results = db.GqlQuery("SELECT * FROM NotificationSetting")

        for result  in query_results:
            distance = calc_distance(target_location, result.centre_location)
            if distance < result.radius:
                template_values = { 'sender' : "sydneyresistancewatch@appspot.com",
                                    'receiver' : result.email,
                                    'link' : "geo:%s,%s?z=19" % (str(latitude), str(longitude)),
                                    'text' : "%s is attacking our portal at %s,%s" % (attacker, str(latitude), str(longitude)) }
                path = os.path.join(os.path.dirname(__file__), 'templates', 'message.xml')
                xml = template.render(path, template_values)
                xmpp.send_message(jids=result.email, raw_xml=True, body=xml, message_type=xmpp.MESSAGE_TYPE_HEADLINE)
                



class NewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email = user.email()
            latitude = float(self.request.get('lat').strip())
            longitude = float(self.request.get('lon').strip())
            radius = int(self.request.get('r').strip())
            centre_location = db.GeoPt(lat=latitude, lon=longitude)
            setting_record = NotificationSetting(email=email, centre_location=centre_location, radius=radius)
            setting_record.put()
            self.response.out.write("record added.")
        else:
            self.redirect(users.create_login_url("/new"))

    def post(self):
        pass

class RemoveHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass

class ShowHandler(webapp2.RequestHandler):
    def get(self):
        pass


logging.getLogger().setLevel(logging.DEBUG)
app = webapp2.WSGIApplication([("/notifications/check", CheckHandler),
                                ("/notifications/new", NewHandler),
                                ("/notifications/remove", RemoveHandler),
                                ("/notifications/show", ShowHandler)], debug=False)

def real_main():
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()