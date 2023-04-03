from flask import Flask, request
from flask import render_template
from flask import current_app as app

@app.route("/", methods=["GET", "POST"])
def index():    
    return render_template("index.html")

# login controllers
@app.route("/login", methods=["GET", "POST"])
def login():    
    return render_template("login.html")

# signup controllers
@app.route("/signup", methods=["GET", "POST"])
def signup():    
    return render_template("signup.html")

@app.route("/articles_by/<user_name>", methods=["GET", "POST"])
def articles_by_author(user_name):
    articles = Article.query.filter(Article.authors.any(username=user_name))
    return render_template("articles_by_author.html", articles=articles, username=user_name)
