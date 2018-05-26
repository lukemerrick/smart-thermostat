import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask.cli import with_appcontext

import click

from werkzeug.security import check_password_hash, generate_password_hash

from web_thermostat.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

ADMIN_USERNAME = 'admin'


def login_required(view):
    '''View decorator that redirects anonymous users to the login page.'''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    '''If a user id is stored in the session, load the user object from
    the database into ``g.user``.'''
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@click.command('set-password')
@click.argument('password')
@with_appcontext
def set_password(password):
    '''Adds command line method to set and reset the admin password'''
    db = get_db()

    user_exists = db.execute(
                'SELECT id FROM user WHERE username = ?', (ADMIN_USERNAME,)
            ).fetchone()
    if user_exists:
        # user already set, so we delete it
        db.execute('DELETE FROM user WHERE username = ?', (ADMIN_USERNAME,))

    db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (ADMIN_USERNAME, generate_password_hash(password))
    )
    db.commit()
    message = 'passowrd updated!' if user_exists else 'admin password set!'
    click.echo(message)



@bp.route('/login', methods=('GET', 'POST'))
def login():
    '''Log in a registered user by adding the user id to the session.'''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    '''Clear the current session, including the stored user id.'''
    session.clear()
    return redirect(url_for('index'))
