from flask import render_template
from . import db  # import db to use if needed
from flask import Blueprint

# Create a Blueprint for routes if you plan to organize them
main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Here you can fetch your products or data from the database as required
    return render_template('index.html')
