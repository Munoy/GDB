import functools

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect


bp = Blueprint('cards', __name__, url_prefix='/cards')
#cardJson = url_for('static', filename='json/all-cards.json')

@bp.route('/search/')
def _search():

    return render_template('cards/search.html')
