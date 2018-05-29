import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    # for dev only
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
)

#app.config.from_pyfile('config.py', silent=True)

# ensure instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import auth, dash, db
app.cli.add_command(auth.set_password)
db.init_app(app)
app.register_blueprint(auth.bp)
app.register_blueprint(dash.bp)

app.add_url_rule('/', endpoint='dashboard')
