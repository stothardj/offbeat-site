import requests
from flask import Flask, render_template, json
from datetime import datetime, timedelta
from babel.dates import format_datetime
app = Flask(__name__)

UPCOMING_EVENTS = 'https://api.meetup.com/Offbeat-Fun/events?photo-host=public&page=20&sig_id=214474886&sig=c8c6b6f5ac38abae010127a30e600755a3438e13'
PAST_EVENTS = 'https://api.meetup.com/Offbeat-Fun/events?desc=true&scroll=recent_past&photo-host=public&page=20&sig_id=214474886&sig=760f449ea62647e9f967fd9afffcb3fcec6b83f9'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def format_event(ev):
    # TODO: timezones and locale
    utc_time = datetime.fromtimestamp(ev['time'] // 1000)
    start_time = format_datetime(utc_time, locale='en')
    duration = timedelta(milliseconds = ev['duration'])
    end_time = format_datetime(utc_time + duration, locale='en')
    result = {
        'name': ev['name'],
        'description': ev['description'],
        'start_time': start_time,
        'end_time': end_time,
        'yes_rsvp_count': ev['yes_rsvp_count'],
        'rsvp_limit': ev.get('rsvp_limit', 'unlimited'),
        'waitlist_count': ev['waitlist_count'],
    }
    return result

def fetch_events(uri):
    response_json = requests.get(uri).content
    response = json.loads(response_json)
    return [format_event(ev) for ev in response]

@app.route('/upcomingevents')
def upcomingevents():
    events = fetch_events(UPCOMING_EVENTS)
    return render_template('eventslist.html', events=events)

@app.route('/pastevents')
def pastevents():
    events = fetch_events(PAST_EVENTS)
    return render_template('eventslist.html', events=events)

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
