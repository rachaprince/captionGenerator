import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from phrasedictionary import PhraseDictionary
from captiongenerator import CaptionGenerator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        contests = db.session.query(Contest).all()
        # for now, set it to the third item until I delete the first two
        return render_template('index.html',contest=contests[2], captions = [] )

@app.route('/contests/<contest_id>', methods=["GET", "POST"])
def contests(contest_id):
    contests = db.session.query(Contest).all()
    if request.method == "GET": # increase or decrease
        return render_template('index.html',contest=contests[int(contest_id)-1])
    else: # method == POST
        current_contest = Contest.query.filter_by(id=contest_id).first()
        current_contest.keyword_0 = request.form.get("keyword_0")
        current_contest.keyword_1 = request.form.get("keyword_1")
        db.session.commit()
        return render_template('index.html',contest=current_contest, captions = [])

@app.route('/captions/<contest_id>', methods=["GET", "POST"])
def captions(contest_id):
    phrase_dict = PhraseDictionary(['cliche_list.txt'])
    phrase_dict.create_index()
    caption_gen = CaptionGenerator(phrase_dict)

    contest = Contest.query.filter_by(id=contest_id).first()

    phrases = caption_gen.get_phrase(contest.keyword_0)
    print phrases
    captions = caption_gen.create_caption(phrases, contest.keyword_1)

    return render_template('index.html',contest=contest, captions = captions)

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
    keyword_0 = db.Column(db.String(120))
    keyword_1 = db.Column(db.String(120))

    def __init__(self, image, men, women, animals, glasses, other, scenery, incongruity, description_0, description_1, description_2, implied,keyword_0,keyword_1):
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
        self.keyword_0 = keyword_0
        self.keyword_1 = keyword_1

    # Query returns this
    def __repr__(self):
        return '<Image %r>' % self.image
