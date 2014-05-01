from flask import Flask, Response

import scrape as i_league_scraper

app = Flask(__name__)

@app.route("/")
def do_scrape():
    return Response(i_league_scraper.scrape(), mimetype="text/plain")
