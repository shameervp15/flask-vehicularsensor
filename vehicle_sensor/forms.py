from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, FileField
from wtforms.validators import DataRequired

class SensorDataForm(FlaskForm):
    csv_file = FileField('Upload CSV File (.csv)')