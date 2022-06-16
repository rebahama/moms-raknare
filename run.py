from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///moms'

db = SQLAlchemy(app)

class Moms(db.Model):
    moms_id = db.Column(db.Integer, primary_key=True)
    moms_six = db.Column(db.Integer, nullable=False)
    moms_twentyfive = db.Column(db.Integer, nullable=False)
    moms_thirty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return f"6:{self.moms_six} 25: {self.moms_twentyfive} 30 :{self.moms_thirty}"






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def display():
    moms = list(Moms.query.order_by(Moms.moms_id).all())
    return render_template('display.html', moms=moms)


@app.route('/calculatesix')
def calculatesix():
    return render_template('calculatesix.html')


@app.route('/calculaetwentyfive')
def calculatetwentyfive():
    return render_template('calculatetwentyfive.html')

@app.route('/calculatethirty')
def calculatethirty():
    return render_template('calculatethirty.html')


if __name__ == "__main__":
    app.run(
        debug=True
    )