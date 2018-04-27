# -*- encoding: utf-8 -*-
from flask.ext.script import Manager
from database import db_session
from models import Event
import requests
from requests.packages import urllib3
import datetime
from events import app
import settings
from mail import send_mail

urllib3.disable_warnings()
manager = Manager(app)

@manager.command
def update_events():
    fields = "fields=description,name,start_time,place"
    access_token = "%s|%s" % (settings.CLIENT_ID, settings.CLIENT_SECRET)
    counter = 0
    facebook_api_error_list = []

    for p in settings.PROFILES:
        url = "https://graph.facebook.com/%s/events?%s&access_token=%s" % (p['id'], fields, access_token)
        try:
            r = requests.get(url).json()

            if 'error' in r and r['error']['code'] != 100:
                print r['error']
                facebook_api_error_list.append(r['error'])
        except Exception, e:
            print u"requests lib exception: %s" % e
            continue

        try:
            if 'data' in r:
                for i in r['data']:
                    e = Event.query.filter(Event.event_id == int(i["id"])).first()

                    if e == None:
                        time = i["start_time"].split('T')[0]
                        start_time = datetime.datetime.strptime(time, "%Y-%m-%d")

                        if "place" in i:
                            location = i["place"]["name"]
                        else:
                            location = u"<nav norādīts>"

                        e = Event(
                                event_id        = i["id"],
                                name            = i["name"],
                                start_time      = start_time,
                                date            = start_time.date(),
                                location        = location,
                                is_date_only    = False,
                                description     = i["description"] if 'description' in i else ""
                            )
                        db_session.add(e)
                        db_session.commit()
                        counter += 1
                        print u"%s added:\n %s \n %s \n %s \n" % (p['name'], e.name, e.start_time, e.location)
        except Exception, e:
            print u"Exception: %s" % e

    if counter > 0:
        print "======================= >>>>>>>>>>>>> db updated %s \n\n" % datetime.datetime.now()

    if len(facebook_api_error_list) > 0 and settings.FACEBOOK_API_ERROR_REPORT_ENABLED:
        facebook_api_error_string = '\n\n'.join(str(item) for item in facebook_api_error_list)
        message = 'Subject: Facebook API errors \n\n %s' % facebook_api_error_string
        send_mail(settings.EMAIL_ADDRESS, settings.ADMINS, message)

if __name__ == '__main__':
    manager.run()
