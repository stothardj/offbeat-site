function displayEvents(req, title) {
    const titleEl = document.getElementById('event-title');
    titleEl.textContent = title;
    const eventsEl = document.getElementById('event-list');
    if (this.status != 200) {
	eventsEl.textContent = 'Failed to retrieve events. Please check Meetup directly';
    }
    // TODO: Seems dubious to set innerHTML based on http response
    eventsEl.innerHTML = req.responseText;
}

function fetchUpcomingEvents() {
    const req = new XMLHttpRequest();
    req.addEventListener('load', () => displayEvents(req, 'Upcoming Events'));
    req.open('GET', '/upcomingevents');
    req.send();
}

function fetchPastEvents() {
    const req = new XMLHttpRequest();
    req.addEventListener('load', () => displayEvents(req, 'Past Events'));
    req.open('GET', '/pastevents');
    req.send();
}

function setType(type) {
    const u = new URL(window.location.href);
    const params = new URLSearchParams(u.hash.substring(1));
    params.set('type', type);
    u.hash = `#?${params.toString()}`;
    window.history.pushState({}, '', u.href);
}

function main() {
    const params = new URLSearchParams(window.location.hash.substring(1));
    if (params.get('type') == 'past') {
	fetchPastEvents();
    } else {
	fetchUpcomingEvents();
    }
    const upcomingLink = document.getElementById('upcoming-link');
    upcomingLink.onclick = () => {
	setType('upcoming');
	fetchUpcomingEvents();
	return false;
    };

    // a link to the past
    const pastLink = document.getElementById('past-link');
    pastLink.onclick = () => {
	setType('past');
	fetchPastEvents();
	return false;
    }
}

window.onload = main;





