#!/bin/python
# -*- coding:utf-8 -*-

import logging
import webapp2
import json
import os

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.ext import db

from model import PortalActivity

class HeatmapHandler(webapp2.RequestHandler):
    def get(self):
        output = memcache.get('heatmap_html')
        if output is None:
            template_values = {}
            path = os.path.join(os.path.dirname(__file__), 'templates', 'heatmap.html')
            output = template.render(path, template_values)
            memcache.add('heatmap_html', output)
        self.response.out.write(output)

class HeatmapJSONHandler(webapp2.RequestHandler):
    def get(self):
        output = memcache.get('heatmap_json')
        results=[]
        if output is None:
            query_results = db.GqlQuery("SELECT * FROM PortalActivity")
            for result in query_results:
                results.append(dict(latitude=result.portal_location.lat, longitude=result.portal_location.lon, weight=result.activity_times))
            output = json.dumps(results)
            memcache.add('heatmap_json', output, 600)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(output)


logging.getLogger().setLevel(logging.INFO)
app = webapp2.WSGIApplication([("/heatmap.html", HeatmapHandler),
                                ("/heatmap.json", HeatmapJSONHandler)], debug=False)


def real_main():
    """ main for wsgi app """
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()