# Packages
from flask import Flask, jsonify, render_template
import json


#Create the app
app = Flask(__name__)

#load the Lenovo JSON file
with open('lenovo_laptops.json') as lenovo_prod:
    lenovo_laptops = json.load(lenovo_prod)

#Homepage
@app.route('/')
def hello():
   return render_template('index.html')


# Lenovo laptops route
@app.route('/lenovo', methods=['GET'])
def lenovo():
    return jsonify(lenovo_laptops), 200

#Run the app
app.run()



