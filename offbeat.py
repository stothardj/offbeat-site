import requests
from flask import Flask, render_template, json
from datetime import datetime, timedelta
from babel.dates import format_datetime
app = Flask(__name__)

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
    return {
        'name': ev['name'],
        'description': ev['description'],
        'start_time': start_time,
        'end_time': end_time,
        'yes_rsvp_count': ev['yes_rsvp_count'],
        'rsvp_limit': ev.get('rsvp_limit', 'unlimited'),
        'waitlist_count': ev['waitlist_count'],
    }

@app.route('/upcomingevents')
def upcomingevents():
    response_json = requests.get('https://api.meetup.com/2/events?offset=0&format=json&limited_events=False&group_urlname=Offbeat-Fun&page=200&fields=&order=time&desc=false&status=upcoming&sig_id=214474886&sig=dad844af55cda43bf7e0ea2e09ea1e9dafd2863d').content
    response = json.loads(response_json)
    events = [format_event(ev) for ev in response['results']]
    return render_template('upcomingevents.html', events=events)

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
