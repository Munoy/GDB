from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, GDB!'


@bp.route('/')
def index():
    return render_template('main.html')