from flask import Flask
from bs4 import BeautifulSoup
from ics import Calendar, Event
from urllib.request import urlopen

# app = Flask(__name__)

def scrap_for(year, month):
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={}&miesiac={}&lang=1".format(year, month)
    event_selector = "#kalendarz a.active"
    
    response = urlopen(url)
    html = BeautifulSoup(response.read())
    selected_elements = html.select(event_selector)
    
    for e in selected_elements:
        print(e)

# @app.route("/")
# def index():
#     return "MOBILE WEEIA CALENDAR API"
# 
# @app.route("/events")
# def actual_events():
#     pass
# 
# @app.route("/events/<year>/<month>")
# def events(year, month):
#     pass

scrap_for(2020, 10)
# app.run("lan", 8080)
