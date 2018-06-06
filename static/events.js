function displayUpcomingEvents() {
    const upcomingeventsEl = document.getElementById('upcomingevents');
    if (this.status != 200) {
	upcomingeventsEl.textContent = 'Failed to retrieve upcoming events. Please check Meetup directly';
    }
    // TODO: Seems dubious to set innerHTML based on http response
    upcomingeventsEl.innerHTML = this.responseText;
}

function fetchUpcomingEvents() {
    const req = new XMLHttpRequest();
    req.addEventListener('load', displayUpcomingEvents);
    req.open('GET', '/upcomingevents');
    req.send();
}

fetchUpcomingEvents();
