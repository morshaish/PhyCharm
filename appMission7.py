from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/hey')
def hey():
    return 'hey!'


@app.route('/bye')
def bye():
    return redirect('/hey')


@app.route('/redirectFor')
def redFor():
    return redirect(url_for('hello_world'))
