from flask import Flask
from bs4 import BeautifulSoup
from ics import Calendar, Event

app = Flask(__name__)

def scrap_for(year, month):
    url = "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok={}&miesiac={}&lang=1".format(year, month)

@app.route("/")
def index():
    return "MOBILE WEEIA CALENDAR API"

@app.route("/events")
def actual_events():
    pass

@app.route("/events/<year>/<month>")
def events(year, month):
    pass

app.run("lan", 8080)
