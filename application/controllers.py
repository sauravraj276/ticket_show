from flask import Flask, request, redirect
from flask import render_template
from flask import current_app as app
from application.models import *
from flask_login import login_user, logout_user, login_required , current_user 

@app.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
            return redirect("/dashboard",200)   
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
     venue = Venue.query.filter_by()
     return render_template('user_dashboard.html',venue=venue)
    venue = Venue.query.filter_by(admin_id=current_user.user_id)

    return render_template('admin_dashboard.html',venue=venue)

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

        if current_user.type==0:
            

            if request.form["update"]=="1":
                venue = db.session.execute(db.select(Venue).filter_by(venue_id=request.form["venue_id"])).scalar_one()
                venue.capacity=request.form["venue_capacity"]
                venue.location=request.form["venue_location"]
                venue.name=request.form["venue_name"]
                venue.place=request.form["venue_place"]
                venue.admin_id=current_user.user_id
                venue.verified = True
                db.session.commit()
                return "Venue data Updated go to <a href='dashboard'>dashboard</a>"

            venue = Venue()
            venue.capacity=request.form["venue_capacity"]
            venue.location=request.form["venue_location"]
            venue.name=request.form["venue_name"]
            venue.place=request.form["venue_place"]
            venue.admin_id=current_user.user_id
            db.session.add(venue)
            db.session.commit()
            return "Venue added go to <a href='dashboard'>dashboard</a>"
       
    
# delete Venue
@app.route('/deleteVenue', methods=['POST'])
@login_required
def deleteVenue():
    venue = db.session.execute(db.select(Venue).filter_by(venue_id=request.form["venue_id"])).scalar_one()
    db.session.delete(venue)
    db.session.commit()
    return "Venue deleted go to <a href='dashboard'>dashboard</a>"
                


    
# add show
@app.route('/addshow', methods=['POST'])
@login_required
def addShow():
        if current_user.type==0:
            
            # if request.form["update"]:
            #     venue = db.session.execute(db.select(Venue).filter_by(venue_id=request.form["venue_id"])).scalar_one()
            #     venue.capacity=request.form["venue_capacity"]
            #     venue.location=request.form["venue_location"]
            #     venue.name=request.form["venue_name"]
            #     venue.place=request.form["venue_place"]
            #     venue.admin_id=current_user.user_id
            #     venue.verified = True
            #     db.session.commit()
            #     return "Venue data Updated go to <a href='dashboard'>dashboard</a>"

            show = Show()
            show.name=request.form["show_name"]
            show.rating=request.form["show_rating"]
            show.start_time=request.form["start_time"]
            show.end_time=request.form["end_time"]
            show.tags=request.form["show_tags"]
            show.price=request.form["show_price"]
            show.venue_id=request.form["venue_id"]
            db.session.add(show)
            db.session.commit()
            return "Show added go to <a href='dashboard'>dashboard</a>"

        
        





