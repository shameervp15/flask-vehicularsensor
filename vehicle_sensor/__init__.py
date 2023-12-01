from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_wtf.csrf import CSRFProtect

socketio = SocketIO(cors_allowed_origins="*")

csrf_protect = CSRFProtect()

db = SQLAlchemy()
DB_Name = "vehicleSensor.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='0b70b35b6e09d382c506ec70983450e9'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_Name}"
    db.init_app(app)

    from .models import SensorModel

    socketio.init_app(app)

    csrf_protect.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app