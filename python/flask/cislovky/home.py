import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from cislovky.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=('GET',))
def home():
    return render_template('home/home.html')


@bp.route('/en', methods=('GET',))
def en():
    return render_template('home/en.html')


@bp.route('/cs', methods=('GET',))
def cd():
    return render_template('home/cs.html')

