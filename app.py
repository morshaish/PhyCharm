from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def cvStart():
    return render_template('homepageCV.html')


@app.route('/Contact')
def contact():
    return render_template('cvConntactPage.html')


@app.route('/About')
def about():
    return render_template('cvMor.html')


@app.route('/assignment8')
def assign():
    return render_template('assignment8.html',
                           hobbies={'Dance', 'Travel', 'Watch Movies'},
                           ComedySeries={'Brooklyn99', '70s Show', 'Friends', 'Great Country'},
                           DramaSeries={'Greys anatomy', 'Suits', 'Deckster', 'Game Of Thrones'},
                           foodAndCalories={'Hamburger': "200", 'peanutButter': "400", 'Pizza': "300"}
                           )


@app.route('/tv')
def tv():
    return render_template('tv.html',
                           user={'name': "haim", 'if Work': "no", 'loveComedy': 'yes'},
                           ComedySeries={'Brooklyn99', '70s Show', 'Friends', 'Great Country'},
                           DramaSeries={'Greys anatomy', 'Suits', 'Deckster', 'Game Of Thrones'},
                           )


if __name__ == '__main__':
    app.run()
