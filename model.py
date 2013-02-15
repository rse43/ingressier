#!/usr/bin/env python
# -*- coding: utf8 -*-

import modelx
from google.appengine.ext import db
from google.appengine.ext import ndb
from uuid import uuid4

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


class Base(ndb.Model, modelx.BaseX):
  created = ndb.DateTimeProperty(auto_now_add=True)
  modified = ndb.DateTimeProperty(auto_now=True)
  _PROPERTIES = set([
      'key', 'id', 'created', 'modified', 'created_ago', 'modified_ago',
    ])


class Config(Base, modelx.ConfigX):
  analytics_id = ndb.StringProperty(default='')
  brand_name = ndb.StringProperty(default='gae-init')
  facebook_app_id = ndb.StringProperty(default='')
  facebook_app_secret = ndb.StringProperty(default='')
  feedback_email = ndb.StringProperty(default='')
  flask_secret_key = ndb.StringProperty(default=str(uuid4()).replace('-', ''))
  twitter_consumer_key = ndb.StringProperty(default='')
  twitter_consumer_secret = ndb.StringProperty(default='')
  _PROPERTIES = Base._PROPERTIES.union(set([
      'analytics_id',
      'brand_name',
      'facebook_app_id',
      'facebook_app_secret',
      'feedback_email',
      'flask_secret_key',
      'twitter_consumer_key',
      'twitter_consumer_secret',
    ]))


class User(Base, modelx.UserX):
  name = ndb.StringProperty(indexed=True, required=True)
  username = ndb.StringProperty(indexed=True, required=True)
  email = ndb.StringProperty(default='')

  active = ndb.BooleanProperty(default=True)
  admin = ndb.BooleanProperty(default=False)

  federated_id = ndb.StringProperty(default='')
  facebook_id = ndb.StringProperty(default='')
  twitter_id = ndb.StringProperty(default='')

  _PROPERTIES = Base._PROPERTIES.union(set([
      'name', 'username', 'avatar_url',
    ]))
