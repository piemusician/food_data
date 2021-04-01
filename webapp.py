from flask import Flask, request, Markup, render_template, flash
from datetime import datetime

import os
import json

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('about.html')
    
    
    
if __name__ == '__main__':
    app.run(debug=False) # change to False when running on heroku
