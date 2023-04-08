from flask import Flask, request, redirect
from flask import render_template
from flask import current_app as app
from application.models import *
from flask_login import login_user, logout_user, login_required , current_user 

@app.route("/", methods=["GET", "POST"])
def index():    
    return render_template("index.html")

# login controllers
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/dashboard",200)

    if request.method == "GET":    
        return render_template("login.html")

    user = User.query.filter_by(email=request.form['email']).first()
    
    if user and user.password==request.form['password']:
        login_user(user)
        return redirect("/dashboard",200)
    return "worng password or user not exist"

# signup controllers
@app.route("/signup", methods=["GET", "POST"])
def signup():
    try:
        if current_user.is_authenticated:
            return redirect("/dashboard",200)
    
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

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect("/login",200)

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    if current_user.type==1:
     return render_template('user_dashboard.html') 
    return render_template('admin_dashboard.html')

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/bookings', methods=['GET'])
@login_required
def bookings():
    return render_template('bookings.html')

# add venue
@app.route('/addVenue', methods=['POST'])
@login_required
def addVenue():
    return request.form



