from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        "author": "Sushrut Tendulkar",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "October 2, 2019",
    },
    {
        "author": "Abdul Kalam",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "October 3, 2019",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


# export FLASK_APP=flaskblog.py
# flask run

# No need to restart the server after changes
# FLASK_DEBUG = 1
# flask run


# python flaskblog.py
if __name__ == "__main__":
    app.run(debug=True)
