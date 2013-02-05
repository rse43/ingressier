#!/usr/bin/env python
# -*- coding: utf8 -*-

from google.appengine.ext import db

class ItemDestroyActivity(db.Model):
    item_owner = db.StringProperty(required=True)
    item_type = db.StringProperty(required=True)
    item_amount = db.IntegerProperty(required=True)
    attacker = db.StringProperty(required=True)
    item_location = db.GeoPtProperty(required=True)
    attack_hours = db.FloatProperty(required=True)
    activity_added_time = db.DateTimeProperty(auto_now_add=True)

class LinkDestroyActivity(db.Model):
    link_creator = db.StringProperty(required=True)
    attacker = db.StringProperty(required=True)
    link_start_location = db.GeoPtProperty(required=True)
    link_end_location = db.GeoPtProperty(required=True)
    attack_hours = db.FloatProperty(required=True)
    activity_added_time = db.DateTimeProperty(auto_now_add=True)
