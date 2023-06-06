from flask import flask, render_template

app = flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/regis')
def regis():
    return render_template("regis.html")


if __name__ == '__main__':
    app.run()