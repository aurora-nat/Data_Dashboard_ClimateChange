from myapp import app
import json, plotly

from flask import render_template
#from wrangling_scripts.wrangling_data import return_figures

@app.route('/')
@app.route('/index')
