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
    with open('food.json') as food_data:
        foods = json.load(food_data)
    if 'foodItem' in request.args:
        foodItem = request.args['foodItem']
        householdweight1 = get_householdweight1_totals(foods, foodItem)
        householdweight1Description = get_householdweight1Description_totals(foods, foodItem)
        householdweight2 = get_householdweight2_totals(foods, foodItem)
        householdweight2Description = get_householdweight2Description_totals(foods, foodItem)
        return render_template('householdresponse.html', options=get_food_options(), foodItem=foodItem, householdweight1=householdweight1, householdweight1Description=householdweight1Description, householdweight2=householdweight2, householdweight2Description=householdweight2Description)
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

def get_householdweight1_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            houseHoldWieghts1 = w["Data"]["Household Weights"]["1st Household Weight"]
            return (houseHoldWieghts1)

def get_householdweight1Description_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            houseHoldWieghts1Description = w["Data"]["Household Weights"]["1st Household Weight Description"]
            return (houseHoldWieghts1Description)
            
def get_householdweight2_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            houseHoldWieghts2 = w["Data"]["Household Weights"]["2nd Household Weight"]
            return (houseHoldWieghts2)
            
def get_householdweight2Description_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            houseHoldWieghts2Description = w["Data"]["Household Weights"]["2nd Household Weight Description"]
            return (houseHoldWieghts2Description)
    
@app.route('/majorMinerals')
def render_majorMinerals():
    with open('food.json') as food_data:
        foods = json.load(food_data)
    if 'foodItem' in request.args:
        foodItem = request.args['foodItem']
        calcium = get_calcium_totals(foods, foodItem)
        copper = get_copper_totals(foods, foodItem)
        iron = get_iron_totals(foods, foodItem)
        magnesium = get_magnesium_totals(foods, foodItem)
        phosphorus = get_phosphorus_totals(foods, foodItem)
        potassium = get_potassium_totals(foods, foodItem)
        sodium = get_sodium_totals(foods, foodItem)
        zinc = get_zinc_totals(foods, foodItem)
        return render_template('majorMineralsresponse.html', options=get_food_options(), foodItem=foodItem, calcium=calcium, copper=copper, iron=iron, magnesium=magnesium, phosphorus=phosphorus, potassium=potassium, sodium=sodium, zinc=zinc)
    return render_template('majorMinerals.html', options=get_food_options())

def get_calcium_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            calcium = w["Data"]["Major Minerals"]["Calcium"]
            return (calcium)
            
def get_copper_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            copper = w["Data"]["Major Minerals"]["Copper"]
            return (copper)

def get_iron_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            iron = w["Data"]["Major Minerals"]["Iron"]
            return (iron)

def get_magnesium_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            magnesium = w["Data"]["Major Minerals"]["Magnesium"]
            return (magnesium)
            
def get_phosphorus_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            phosphorus = w["Data"]["Major Minerals"]["Phosphorus"]
            return (phosphorus)
            
def get_potassium_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            potassium = w["Data"]["Major Minerals"]["Potassium"]
            return (potassium)
            
def get_sodium_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            sodium = w["Data"]["Major Minerals"]["Sodium"]
            return (sodium)
            
def get_zinc_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            zinc = w["Data"]["Major Minerals"]["Zinc"]
            return (zinc)
            
@app.route('/vitamins')
def render_vitamins():
    with open('food.json') as food_data:
        foods = json.load(food_data)
    if 'foodItem' in request.args:
        foodItem = request.args['foodItem']
        vitA = get_vitA_totals(foods, foodItem)
        vitARAE = get_vitARAE_totals(foods, foodItem)
        vitB12 = get_vitB12_totals(foods, foodItem)
        vitB6 = get_vitB6_totals(foods, foodItem)
        vitC = get_vitC_totals(foods, foodItem)
        vitE = get_vitE_totals(foods, foodItem)
        vitK = get_vitK_totals(foods, foodItem)
        return render_template('vitaminsresponse.html', options=get_food_options(), foodItem=foodItem, vitA=vitA, vitARAE=vitARAE, vitB12=vitB12, vitB6=vitB6, vitC=vitC, vitE=vitE, vitK=vitK)
    return render_template('vitamins.html', options=get_food_options())

def get_vitA_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitA = w["Data"]["Vitamins"]["Vitamin A - IU"]
            return (vitA)
            
def get_vitARAE_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitARAE = w["Data"]["Vitamins"]["Vitamin A - RAE"]
            return (vitARAE)
            
def get_vitB12_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitB12 = w["Data"]["Vitamins"]["Vitamin B12"]
            return (vitB12)    
            
def get_vitB6_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitB6 = w["Data"]["Vitamins"]["Vitamin B6"]
            return (vitB6)
            
def get_vitC_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitC = w["Data"]["Vitamins"]["Vitamin C"]
            return (vitC)
            
def get_vitE_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitE = w["Data"]["Vitamins"]["Vitamin E"]
            return (vitE)
            
def get_vitK_totals(data, foodItem):
    for w in data:
        if w["Description"] == foodItem:
            vitK = w["Data"]["Vitamins"]["Vitamin K"]
            return (vitK)
    
if __name__ == '__main__':
    app.run(debug=False) # change to False when running on heroku
