from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# import secrets
# secrets.token_hex(16)

app.config["SECRET_KEY"] = "90cc24befbeab41d93d7e14cb6fff4ca"


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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data} !", "Success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


# export FLASK_APP=flaskblog.py
# flask run

# No need to restart the server after changes
# FLASK_DEBUG = 1
# flask run


# python flaskblog.py
if __name__ == "__main__":
    app.run(debug=True)
