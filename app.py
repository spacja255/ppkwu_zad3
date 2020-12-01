from flask import Flask
from flask import Response
from bs4 import BeautifulSoup
from ics import Calendar, Event
from urllib.request import urlopen
import datetime

app = Flask(__name__)

def scrap_events_from(year, month):
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={}&miesiac={}&lang=1".format(year, month)
    event_selector = "#kalendarz td.active"
    title_selector = "div.calendar-text"
    day_and_url_selector = "a.active"
    
    response = urlopen(url)
    html = BeautifulSoup(response.read())
    selected_elements = html.select(event_selector)
    calendar = Calendar()
    
    for e in selected_elements:
        event = Event()
        event.name = e.select(title_selector)[0].getText()
        day_and_url = e.select(day_and_url_selector)[0]
        event.begin = "{}-{}-{:02d}".format(year, month, int(day_and_url.getText()))
        event.url = day_and_url["href"]
        event.make_all_day()
        calendar.events.add(event)
        
    return str(calendar)

@app.route("/")
def index():
    return "MOBILE WEEIA CALENDAR API"
 
@app.route("/events")
def actual_events():
    now = datetime.datetime.now()
    return Response(scrap_events_from(now.year, now.month), mimetype="text/calendar")
 
@app.route("/events/<year>/<month>")
def events(year, month):
    return Response(scrap_events_from(year, month), mimetype="text/calendar")

app.run("0.0.0.0", 8080)
