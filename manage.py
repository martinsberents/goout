# -*- encoding: utf-8 -*-
from flask.ext.script import Manager
from database import db_session
from models import Event
import requests
from requests.packages import urllib3
import datetime
from events import app
import settings

urllib3.disable_warnings()
manager = Manager(app)

@manager.command
def update_events():
    fields = "fields=picture.type(square),description,name,start_time,location"
    access_token = "%s|%s" % (settings.CLIENT_ID, settings.CLIENT_SECRET)
    counter = 0
    for p in settings.PROFILES:
        url = "https://graph.facebook.com/%s/events?%s&access_token=%s" % (p['id'], fields, access_token)
        try:
            r = requests.get(url).json()
        except Exception, e:
            print u".json() Exception: %s" % e
            continue

        try:
            if r.get('data'):
                for i in r['data']:
                    e = Event.query.filter(Event.event_id == int(i["id"])).first()
                    if e == None:
                        time = i["start_time"].split('T')[0]
                        start_time = datetime.datetime.strptime(time, "%Y-%m-%d")

                        e = Event(
                                event_id        = i["id"],
                                name            = i["name"],
                                start_time      = start_time,
                                date            = start_time.date(),
                                location        = i["location"] if i.get('location') else u"<nav norādīts>",
                                is_date_only    = False,
                                description     = i["description"] if i.get('description') else "",
                                picture_url     = i["picture"]["data"]["url"]
                            )
                        db_session.add(e)
                        db_session.commit()
                        counter += 1
                        print u"%s added:\n %s \n %s \n %s \n" % (p['name'], e.name, e.start_time, e.location)
        except Exception, e:
            print u"Exception: %s" % e

    if counter > 0:
        print "======================= >>>>>>>>>>>>> db updated %s \n\n" % datetime.datetime.now()

if __name__ == '__main__':
    manager.run()
