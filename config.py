import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here-change-in-production'
    
    # MongoDB Configuration
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/'
    MONGO_DB_NAME = 'qr_attendance_db'
    
    # Flask-Login
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    
    # Mail Configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # Mail credentials (use env vars in production)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'shashidharpc1012@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'aqlsnbtbfiukwvnd'
    MAIL_DEFAULT_SENDER = (
        'Attendance Geo Tracker',
        os.environ.get('MAIL_FROM') or 'no-reply@attendancegeotracker.local'
    )
    
    # QR Code Settings
    QR_EXPIRY_MINUTES = 20
    
    # Geofencing Settings
    ALLOWED_RADIUS_METERS = 30
    
    # Admin Credentials
    ADMIN_EMAIL = 'admin@edu.com'
    ADMIN_PASSWORD = 'admin123'