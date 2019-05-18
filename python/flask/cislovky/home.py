import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from cislovky.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=('GET',))
def home():
    db = get_db()
    cislovky = db.execute(
        "SELECT id, rome, cs, en"
        " FROM cislovky"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template('home/home.html', cislovky=cislovky)


@bp.route('/en', methods=('GET',))
def en():
    db = get_db()
    cislovky = db.execute(
        "SELECT id, en"
        " FROM cislovky"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template('home/en.html', cislovky=cislovky)


@bp.route('/cs', methods=('GET',))
def cs():
    db = get_db()
    cislovky = db.execute(
        "SELECT id, cs"
        " FROM cislovky"
        " ORDER BY id ASC"
    ).fetchall()
    return render_template('home/cs.html', cislovky=cislovky)

