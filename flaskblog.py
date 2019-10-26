from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Boy meets world!</h1>'

@app.route('/about')
def about():
    return '<h1>This is the about page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
