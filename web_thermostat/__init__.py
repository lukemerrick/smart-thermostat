import os
from flask import Flask

def create_app(test_config=None):
    '''
    Create and configure an instance
    of the application
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # for dev only
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    if test_config is None:
        # load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def landing_page():
        return 'More coming soon!'

    from . import db
    db.init_app(app)

    from . import auth
    from .auth import set_password
    app.cli.add_command(set_password)

    return app
