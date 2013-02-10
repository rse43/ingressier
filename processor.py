import logging
import webapp2
import datetime

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

from model import ItemDestroyActivity
from model import PortalActivity
from model import ProcessTimeCursor

def process_data(activity, portal):
        if portal is None:
            portal = PortalActivity(portal_location=activity.item_location, activity_times=activity.item_amount)
        else:
            portal.activity_times = portal.activity_times + activity.item_amount

        time_cursor = ProcessTimeCursor(latest_processed_time=activity.activity_added_time)

        portal.put()
        time_cursor.put()

class PortalDataProcessHandler(webapp2.RequestHandler):
    def get(self):
        xg_on = db.create_transaction_options(xg=True)
        output = "Nothing to process."
        time_cursor = None
        try:
            query_results = db.GqlQuery("SELECT latest_processed_time FROM ProcessTimeCursor ORDER BY cursor_added_at DESC LIMIT 1")
        except Exception, e:
            pass
        
        for result in query_results:
            time_cursor = result.latest_processed_time

        if time_cursor is None:
            if self.request.get('initialize').strip() == 'true':
                time_cursor = datetime.datetime.fromtimestamp(0)
                query_results = db.GqlQuery("SELECT * FROM ItemDestroyActivity WHERE activity_added_time > :1 ORDER BY activity_added_time ASC LIMIT 50", time_cursor)
                for result in query_results:
                    activity_location = result.item_location

                    portals = db.GqlQuery("SELECT * FROM PortalActivity WHERE portal_location = :1 LIMIT 1", activity_location)
                    this_portal = None
                    for portal in portals:
                        this_portal = portal

                    db.run_in_transaction_options(xg_on, process_data, result, this_portal)
                output = "FIRST TIME, activities have been processed"
            else:
                output = "No cursor found"
                logging.error(output)
        else:
            query_results = db.GqlQuery("SELECT * FROM ItemDestroyActivity WHERE activity_added_time > :1 ORDER BY activity_added_time ASC LIMIT 50", time_cursor)
            for result in query_results:
                activity_location = result.item_location

                portals = db.GqlQuery("SELECT * FROM PortalActivity WHERE portal_location = :1 LIMIT 1", activity_location)
                this_portal = None
                for portal in portals:
                    this_portal = portal

                db.run_in_transaction_options(xg_on, process_data, result, this_portal)
            output = "activities have been processed "

        self.response.out.write(output)


logging.getLogger().setLevel(logging.INFO)
app = webapp2.WSGIApplication([("/process", PortalDataProcessHandler)], debug=False)


def real_main():
    """ main for wsgi app """
    run_wsgi_app(app)


if __name__ == "__main__":
    real_main()