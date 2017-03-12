import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        contests = db.session.query(Contest).all()
        return render_template('index.html',contests=contests )
    else: # method == POST
        print request.form.get("keyword_0")
        print request.form.get("keyword_1")
        contests = db.session.query(Contest).all()
        return render_template('index.html',contests=contests )

# Database Methods
class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(120), unique=True)
    men = db.Column(db.String(5))
    women = db.Column(db.String(5))
    animals = db.Column(db.String(5))
    glasses = db.Column(db.String(5))
    other = db.Column(db.String(120))
    scenery = db.Column(db.String(120))
    incongruity = db.Column(db.String(120))
    description_0 = db.Column(db.String(120))
    description_1 = db.Column(db.String(120))
    description_2 = db.Column(db.String(120))
    implied = db.Column(db.String(120))
    
    def __init__(self, image, men, women, animals, glasses, other, scenery, incongruity, description_0, description_1, description_2, implied):
        self.image = image
        self.men = men
        self.women = women
        self.animals = animals
        self.glasses = glasses
        self.other = other
        self.scenery = scenery
        self.incongruity = incongruity
        self.description_0 = description_0
        self.description_1 = description_1
        self.description_2 = description_2
        self.implied = implied

    def __repr__(self):
        return '<Image %r>' % self.image
