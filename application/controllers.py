from flask import Flask, request, redirect
from flask import render_template
from flask import current_app as app
from application.models import *

@app.route("/", methods=["GET", "POST"])
def index():    
    return render_template("index.html")

# login controllers
@app.route("/login", methods=["GET", "POST"])
def login():  
    if request.method == "GET":    
        return render_template("login.html")

    user = User.query.filter_by(email=request.form['email']).first()
    
    if user and user.password==request.form['password']:
        return redirect("/userdashboard",200)
    return "worng password or user not exist"

# signup controllers
@app.route("/signup", methods=["GET", "POST"])
def signup():
    try:
        # If request type is get render and return signup form
        if request.method == "GET":
            return render_template("signup.html")
        
        # 
        user=User()
        user.name=request.form['name']
        user.email=request.form['email']
        user.password=request.form['password']
        user.type=1
        db.session.add(user)
        db.session.commit()
        return redirect("/login",200)
    except:
        return render_template('403.html'), 403
    
