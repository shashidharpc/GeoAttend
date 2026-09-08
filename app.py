from flask import Flask, render_template
from flask_login import LoginManager, current_user
from flask_mail import Mail
from config import Config
from models import Database, User
import os
from bson.objectid import ObjectId

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = Database(app.config['MONGO_URI'], app.config['MONGO_DB_NAME']).db
# Attach db to app to avoid circular imports from route modules
app.db = db

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Initialize Flask-Mail
mail = Mail(app)
# Attach mail to app so route modules can access it via `current_app.mail`
app.mail = mail

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(db, user_id)

# Register blueprints
from routes import auth_bp, admin_bp, student_bp

# Import route modules so that route decorators are applied to the
# blueprints before the blueprints are registered with the app. This
# avoids a circular import/timing issue where the blueprint might be
# registered before its routes are attached.
import routes.auth
import routes.admin
import routes.student

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.template_filter('datetime')
def format_datetime(value):
    import pytz
    if isinstance(value, str):
        return value
    if value:
        # Convert UTC to IST
        ist = pytz.timezone('Asia/Kolkata')
        if value.tzinfo is None:
            value = pytz.utc.localize(value)
        value_ist = value.astimezone(ist)
        return value_ist.strftime("%Y-%m-%d %H:%M:%S")
    return ""


@app.template_filter('ObjectId')
def to_objectid(value):
    try:
        return ObjectId(value)
    except Exception:
        return value

# Initialize admin user
def init_admin():
    admin = User.get_by_email(db, Config.ADMIN_EMAIL)
    if not admin:
        User.create_user(
            db,
            Config.ADMIN_EMAIL,
            'Administrator',
            Config.ADMIN_PASSWORD,
            role='admin'
        )
        print("Admin user created successfully!")

if __name__ == '__main__':
    with app.app_context():
        init_admin()
    app.run(debug=True, host='0.0.0.0', port=5000)