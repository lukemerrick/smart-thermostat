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

placeholder_rooms = [
        {
            'id':1,
            'name':'Living Room',
            'current_temp':72.34,
            'current_humidity':32.1,
            'temp_setting':72,
        },
        {
            'id':2,
            'name':'Bedroom',
            'current_temp':69.5,
            'current_humidity':26.22,
            'temp_setting':70,
        }
]


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        room_id = request.form.get('room_id')
        new_temp_setting = request.form.get('temp_setting', type=float)
        if room_id == 1:
            placeholder_rooms[0]['temp_setting'] = new_temp_setting
        else:
            placeholder_rooms[1]['temp_setting'] = new_temp_setting
    return render_template('dashboard/index.html',
            notifications=placeholder_notifications,
            rooms=placeholder_rooms, temp_unit='F')
