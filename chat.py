#!/bin/python
# -*- coding:utf-8 -*-

import webapp2
import logging

from google.appengine.api import xmpp

from google.appengine.ext.webapp.util import run_wsgi_app

class XMPPHandler(webapp2.RequestHandler):
    def post(self):
        message = xmpp.Message(self.request.POST)
        if message.body[0:5].lower() == 'hello':
            xmpp.send_invite(message.sender)
            message.reply("Greetings!")

app = webapp2.WSGIApplication([('/_ah/xmpp/message/chat/', XMPPHandler)], debug=True)

def real_main():
    """ main for wsgi app """
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()