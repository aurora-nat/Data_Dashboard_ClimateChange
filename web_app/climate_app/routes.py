from climate_app import app
import json, plotly

from flask import render_template
from .wrangling_scripts.wrangling_data import return_figures

@app.route('/')
@app.route('/index')
def index():
    
    figures = return_figures()

    #plot ids for html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
    #Convert the plotly figures to JSON for javascript in HTML template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figuresJSON)

