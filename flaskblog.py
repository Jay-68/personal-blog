from flask import Flask, render_template,url_for

app = Flask(__name__)

posts = [
    {
        'author': 'James Ngari',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 24,2019'
    },
    {
        'author': 'Brian Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 22,2011'
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__':
    app.run(debug=True)
