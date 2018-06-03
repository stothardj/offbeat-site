import requests
from flask import Flask, render_template, json
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

@app.route('/upcomingevents')
def upcomingevents():
    response = requests.get('https://api.meetup.com/2/events?offset=0&format=json&limited_events=False&group_urlname=Offbeat-Fun&page=200&fields=&order=time&desc=false&status=upcoming&sig_id=214474886&sig=dad844af55cda43bf7e0ea2e09ea1e9dafd2863d').content
    events = json.loads(response)
    return render_template('upcomingevents.html', events=events)

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
