from datetime import datetime
import random
from threading import Lock
import csv
import os

thread = None
thread_lock = Lock()

def get_current_time():
    current_datetime = datetime.now()
    return current_datetime.strftime(r"%d-%m-%Y %H-%M-%S")

def sensor_data_generator():
    in_time = get_current_time()
    oil_temps = random.randrange(180,230)
    intake_temps = random.randrange(95,115)
    coolant_temps = random.randrange(170,220)
    rpms = random.randrange(1000,9500)
    speeds = random.randrange(30,140)
    throttle_pos = random.randrange(10,90)

    return in_time, oil_temps, intake_temps, coolant_temps, rpms, speeds, throttle_pos

def create_csv_file():
    filename = os.path.join(os.path.dirname(__file__), 'assets', get_current_time())+'.csv'
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        headers = ['in_time', 'oil_temps', 'intake_temps', 'coolant_temps', 'rpms', 'speeds', 'throttle_pos']
        writer.writerow(headers)
    return filename

def update_csv_file(filename, data=[]):
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        print(f"Error updating CSV file: {e}")


# db_data = SensorModel(
    #     datetime=str(in_time), oil_temps=oil_temps, intake_temps=intake_temps,
    #     coolant_temps=coolant_temps, rpms=rpms, speeds=speeds, throttle_pos=throttle_pos
    # )
    # db.session.add(db_data)
    # db.session.commit()

