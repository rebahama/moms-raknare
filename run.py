from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///moms'

db = SQLAlchemy(app)


class Momssix(db.Model):

    moms_id = db.Column(db.Integer, primary_key=True)
    moms_six = db.Column(db.Integer)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
    # __repr__ to represent itself in the form of a string
        return f"6:{self.moms_six} {self.date_add}"


class Momstwentyfive(db.Model):
    moms_id = db.Column(db.Integer, primary_key=True)
    moms_twentyfive = db.Column(db.Integer)

    def __repr__(self):
    #  __repr__ to represent itself in the form of a string
        return f"25:{self.moms_twentyfive}"


class Momsthirty(db.Model):
    moms_id = db.Column(db.Integer, primary_key=True)
    moms_thirty = db.Column(db.Integer)

    def __repr__(self):
            # __repr__ to represent itself in the form of a string
        return f"30:{self.moms_thirty}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display')
def display():
    moms = list(Momssix.query.order_by(Momssix.moms_id).all())
    return render_template('display.html', moms=moms)


@app.route('/showsix')
def showsix():
    moms = list(Momssix.query.order_by(Momssix.moms_id).all())
    return render_template('showsix.html', moms=moms)


@app.route('/showtwentyfive')
def showtwentyfive():
    moms = list(Momstwentyfive.query.order_by(Momstwentyfive.moms_id).all())
    return render_template('showtwentyfive.html', moms=moms)


@app.route('/showthirty')
def showthirty():
    moms = list(Momsthirty.query.order_by(Momsthirty.moms_id).all())
    return render_template('showthirty.html', moms=moms)


@app.route('/calculatesix',  methods=["GET", "POST"])
def calculatesix():
    if request.method == "POST":
        moms = Momssix(moms_six=request.form.get("result"))
        db.session.add(moms)
        db.session.commit()
        return redirect(url_for("showsix"))
    return render_template('calculatesix.html')


@app.route('/calculaetwentyfive', methods=["GET", "POST"])
def calculatetwentyfive():
    if request.method == "POST":
        momstwentyfive = Momstwentyfive(moms_twentyfive=request.form.get("resulttwentyfive"))
        db.session.add(momstwentyfive)
        db.session.commit()
        return redirect(url_for("showtwentyfive"))
    return render_template('calculatetwentyfive.html')


@app.route('/calculatethirty', methods=["GET", "POST"])
def calculatethirty():
    if request.method == "POST":
        momsthirty = Momsthirty(moms_thirty=request.form.get("resultthirty"))
        db.session.add(momsthirty)
        db.session.commit()
        return redirect(url_for("showthirty"))
    return render_template('calculatethirty.html')

@app.route("/sixedit/<int:moms_id>", methods=["GET", "POST"])
def sixedit(moms_id):
    moms=Momssix.query.get_or_404(moms_id)
    if request.method == "POST":
        moms.moms_six=request.form.get("result")
        db.session.commit()
        return redirect(url_for("showsix"))
    return render_template("sixedit.html", moms=moms)


if __name__ == "__main__":
    app.run(
        debug=True
    )