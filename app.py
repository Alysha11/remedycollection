import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'remedy_collection'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_remedies')
def get_remedies():
    return render_template("remedies.html", remedies=mongo.db.remedies.find())


@app.route('/add_remedy')
def add_remedy():
    return render_template('addremedy.html', types=mongo.db.type.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)