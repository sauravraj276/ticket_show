import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

app = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SECRET_KEY'] = 'very secret key'
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()

from flask_login import LoginManager
login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_email):
  try:
    #: Flask Peewee used here to return the user object
    user = User.query.filter_by(email=user_email).first()
    if user:
       return user
    else :
       return None
  except:
        return None
  
# Import all the controllers so they are loaded
from application.controllers import *

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8080)
