# __init__.py - initialization
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models
"""
    This script creates the application object (of
    class Flask) and then imports the views module).

    The import statement is at the end and not at the beginning 
    of the script to avoid circular references. 
    The views module needs to import the app variable 
    defined in this script. Putting the import at the 
    end avoids the circular import error.
"""
