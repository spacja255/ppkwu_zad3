from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
from ics import Calendar, Event
from urllib.request import urlopen
import datetime

app = Flask(__name__)

def scrap_for(year, month):
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={}&miesiac={}&lang=1".format(year, month)
    event_selector = "#kalendarz td.active"
    title_selector = "#kalendarz .InnerBox"
    day_and_url_selector = "#kalendarz a"
    
    response = urlopen(url)
    html = BeautifulSoup(response.read())
    selected_elements = html.select(event_selector)
    data = []
    
    for e in selected_elements:
        title = e.select(title_selector)[0].getText()
        day_and_url = e.select(day_and_url_selector)[0]
        date = "{}-{}-{}".format(year, month, day_and_url.getText())
        url = day_and_url["href"]
        
        data.append({
            "title": title,
            "date": date,
            "url": url
        })
        
    return data

@app.route("/")
def index():
    return "MOBILE WEEIA CALENDAR API"
 
@app.route("/events")
def actual_events():
    now = datetime.datetime.now()
    return jsonify(scrap_for(now.year, now.month))
 
@app.route("/events/<year>/<month>")
def events(year, month):
    return jsonify(scrap_for(year, month))

app.run("lan", 8080)
