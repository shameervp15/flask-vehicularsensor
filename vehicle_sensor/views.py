from flask import Blueprint, render_template, request, send_from_directory
import os

from .utils import sensor_data_generator, thread_lock, thread, create_csv_file, update_csv_file
from .models import SensorModel
from . import db, socketio
from .forms import SensorDataForm

views = Blueprint("views", __name__)

@views.route('/', methods=['GET'])
def sensor_data_view():
    return render_template('sensor_data.html',)

def sensor_data_process():

    csv_file = create_csv_file()

    while True:
        in_time, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos = sensor_data_generator()

        data = [in_time, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos]
        update_csv_file(filename=csv_file, data=data)

        socketio.emit('updateSensorData', {"time": in_time[11:],
                                           'oil_temps': oil_temps,
                                           'intake_temps': intake_temps,
                                           'coolant_temps': coolant_temps,
                                           'rpms': rpms,
                                           'speeds': speeds,
                                           'throttle_pos': throttle_pos,
                                            })
        socketio.sleep(1)

@socketio.on('connect')
def connect():
    global thread
    print('Client connected')
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(sensor_data_process)

@socketio.on('client_disconnecting')
def disconnect():
    print('Client disconnected',  request.sid)


@views.route('/data', methods=["GET", "POST"])
def data_analysis():
    form = SensorDataForm()
    csv_files = [f for f in os.listdir(os.path.join(os.path.dirname(__file__), 'assets')) if f.endswith('.csv')]
    if request.method == "POST":

        return render_template("data.html", form=form)
    
    return render_template("data.html", form=form, csv_files=csv_files)

@views.route("/download/<file>")
def download_csv_file(file):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'assets'), file, as_attachment=True)
