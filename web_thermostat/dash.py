from flask import (
        Blueprint, render_template, request, url_for
)

from web_thermostat.auth import login_required
from web_thermostat.db import get_db

bp = Blueprint('dashboard', __name__)

placeholder_notifications = [
    {
        'icon':'comment',
        'icon_color':'green',
        'message':'placeholder notification 1',
        'link':'javascript:void(0);',
        'access_time':'2 hours ago',
    },
    {
        'icon':'settings',
        'icon_color':'red',
        'message':'placeholder notification 2',
        'link':'javascript:void(0);',
        'access_time':'3 hours ago',
    },
    {
        'icon':'comment',
        'icon_color':'green',
        'message':'placeholder notification 3',
        'link':'javascript:void(0);',
        'access_time':'8 hours ago',
    },
]

@bp.route('/')
@login_required
def index():
    return render_template('dashboard/index.html', notifications=placeholder_notifications)
