from flask import Flask
from flask import render_template

import nba_py as nba

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = "Home")

# Get list of games on a specific date
def get_games(date):
    # type: (datetime) -> array
    scoreboard = nba.Scoreboard(month = date.month, day = date.day, year = date.year)
    line = scoreboard.line_score()
    
    
    


if __name__ == "__main__":
    # app.run(threaded=True)
    app.run(host = "0.0.0.0", port = "8080", threaded= True, debug = True)
