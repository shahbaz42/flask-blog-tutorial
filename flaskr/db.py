import sqlite3

import click
from flask import current_app, g
# g is a special object that is unique for each request.
# It is used to store data that might be accessed by multiple functions during the request.

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        # tells the connection to return rows that behave like dicts. 
    return g.db

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """
    Function for registering with the Application.
    """
    app.teardown_appcontext(close_db)
    # tells Flask to call that function 
    # when cleaning up after returning the response.
    app.cli.add_command(init_db_command)
    # adds a new command
    # that can be called with the flask command.
