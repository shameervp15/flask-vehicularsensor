from . import db

class SensorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(20), unique=True)
    oil_temps = db.Column(db.Integer, nullable=False)
    intake_temps = db.Column(db.Integer, nullable=False)
    coolant_temps = db.Column(db.Integer, nullable=False)
    rpms = db.Column(db.Integer, nullable=False)
    speeds = db.Column(db.Integer, nullable=False)
    throttle_pos = db.Column(db.Integer, nullable=False)