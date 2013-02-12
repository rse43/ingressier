#!/usr/bin/env python
# -*- coding: utf8 -*-

from google.appengine.ext import db

class ItemDestroyActivity(db.Model):
    item_owner = db.StringProperty(required=True)
    item_type = db.StringProperty(required=True)
    item_amount = db.IntegerProperty(required=True)
    attacker = db.StringProperty(required=True)
    item_location = db.GeoPtProperty(required=True)
    attack_time = db.TimeProperty(required=True)
    activity_added_time = db.DateTimeProperty(auto_now_add=True)

class LinkDestroyActivity(db.Model):
    link_creator = db.StringProperty(required=True)
    attacker = db.StringProperty(required=True)
    link_start_location = db.GeoPtProperty(required=True)
    link_end_location = db.GeoPtProperty(required=True)
    attack_time = db.TimeProperty(required=True)
    activity_added_time = db.DateTimeProperty(auto_now_add=True)

class Message(db.Model):
    mail = db.BlobProperty(required=True)
    received_at = db.DateTimeProperty(auto_now_add=True)
    analyzed = db.BooleanProperty(required=True)

class PortalActivity(db.Model):
    portal_location = db.GeoPtProperty(required=True)
    activity_times = db.IntegerProperty(required=True)
    portal_added_at = db.DateTimeProperty(auto_now_add=True)

class ProcessTimeCursor(db.Model):
    latest_processed_time=db.DateTimeProperty(required=True)
    cursor_added_at = db.DateTimeProperty(auto_now_add=True)

class NotificationSetting(db.Model):
    email = db.StringProperty(required=True)
    centre_location = db.GeoPtProperty(required=True)
    radius = db.IntegerProperty(required=True)
    added_at = db.DateTimeProperty(auto_now_add=True)