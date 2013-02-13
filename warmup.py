#!/bin/python
# -*- coding:utf-8 -*-

import logging
import webapp2

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import memcache
from google.appengine.ext import db

class WarmupHandler(webapp2.RequestHandler):
    def get(self):
        #TODO Figure out how to warm up this instance properly.
        pass


logging.getLogger().setLevel(logging.INFO)
app = webapp2.WSGIApplication([("/_ah/warmup", WarmupHandler)], debug=False)


def real_main():
    """ main for wsgi app """
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()