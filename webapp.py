from flask import Flask, request, Markup, render_template, flash
from datetime import datetime

import os
import json

app = Flask(__name__)

@app.route('/')
def render_about():
    return render_template('about.html')

@app.route('/household')
def render_household():
    return render_template('household.html', options=get_food_options())
    
def get_food_options():
    listOfFood = []
    with open('food.json') as food_data:
        foods = json.load(food_data)
    for food in foods:
    	if not(food["Description"] in listOfFood):
    		listOfFood.append(food["Description"])
    		
    options = ""
    for food in listOfFood:
        options = options + Markup("<option value=\"" + food + "\">" + food + "</option>")
    return options

@app.route('/majorMinerals')
def render_majorMinerals():
    return render_template('majorMinerals.html', options=get_food_options())

@app.route('/vitamins')
def render_vitamins():
    return render_template('vitamins.html', options=get_food_options())
    
    
if __name__ == '__main__':
    app.run(debug=False) # change to False when running on heroku
