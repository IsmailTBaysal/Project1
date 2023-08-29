from flask import Blueprint, render_template

# Create a blueprint for routes
bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

# Define more route handlers as needed
