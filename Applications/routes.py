from Applications import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px


@app.route("/")
def index():
    #Graph 1
    df = pd.read_csv("equalPayStats.csv")
    fig1 = px.bar(df,x="nation",y=['gold','silver','bronze'],title="Wide=Form Input")
    graph1JSON = json.dumps(fig1,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html",title="Home",graph1JSON=graph1JSON)