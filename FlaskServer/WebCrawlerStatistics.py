from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'


@app.route('/api')
def hi():
    return render_template("home.html")


@app.route('/home')
@app.route('/')
def greeting():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
