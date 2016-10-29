# -*- encoding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask.ext.babel import Babel, format_date
from database import db_session
from models import Event
import datetime
import requests
import settings
app = Flask(__name__)
app.config.from_object(settings)
babel = Babel(app)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.template_filter('date_format')
def date_format(value, format="EEEE d. MMMM yyyy"):
    return format_date(value, format)

@app.route('/')
def index():
    today = datetime.datetime.today()
    start_time = today.date()

    if today.hour <= 5:
        margin = datetime.timedelta(days=-1)
        start_time = start_time + margin

    events = Event.query.filter(Event.start_time >= start_time).order_by(Event.start_time)
    return render_template('index.html', events=events)

@app.route('/about')
def about():
    profiles = sorted(settings.PROFILES, key=lambda profile: profile['name'].lower())
    return render_template('about.html', profiles=profiles)

if __name__ == '__main__':
    app.run()
