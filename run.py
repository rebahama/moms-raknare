from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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