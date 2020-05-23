from flask import Flask, render_template
from Statistics.statistics_utils import get_api

app = Flask(__name__, template_folder='FlaskServer/templates')
app.static_folder = 'FlaskServer/static'


@app.route('/api')
def hi():
    return get_api()


@app.route('/home')
@app.route('/')
def greeting():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
