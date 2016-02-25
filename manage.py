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
    fields = "fields=picture.type(square),description,name,start_time,is_date_only,location"
    access_token = "%s|%s" % (settings.CLIENT_ID, settings.CLIENT_SECRET)
    for p in settings.PROFILES:
        url = "https://graph.facebook.com/%s/events?%s&access_token=%s" % (p['id'], fields, access_token)
        r = requests.get(url).json()
        try:
            print "============ checking %s" % p['name']
            if r.get('data'):
                for i in r['data']:
                    e = Event.query.filter(Event.event_id == int(i["id"])).first()
                    if e == None:
                        if i["is_date_only"]:
                            start_time = datetime.datetime.strptime(i["start_time"], "%Y-%m-%d")
                        else:
                            time = i["start_time"].split('T')[0]
                            start_time = datetime.datetime.strptime(time, "%Y-%m-%d")

                        e = Event(
                                event_id        = i["id"],
                                name            = i["name"],
                                start_time      = start_time,
                                date            = start_time.date(),
                                location        = i["location"] if i.get('location') else u"<nav norādīts>",
                                is_date_only    = i["is_date_only"],
                                description     = i["description"] if i.get('description') else "",
                                picture_url     = i["picture"]["data"]["url"]
                            )
                        db_session.add(e)
                        db_session.commit()
                        print u"added\n %s \n %s \n %s \n" % (e.name, e.start_time, e.location)
        except Exception, e:
            print u"Exception: %s" % e

    print "======================= >>>>>>>>>>>>> db updated %s \n\n" % datetime.datetime.now()

if __name__ == '__main__':
    manager.run()
