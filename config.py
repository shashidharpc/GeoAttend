import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    # MongoDB Configuration
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "qr_attendance_db")

    # Flask-Login
    REMEMBER_COOKIE_DURATION = timedelta(days=7)

    # Mail Configuration
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() == "true"

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_DEFAULT_SENDER = (
        "Attendance Geo Tracker",
        os.getenv("MAIL_FROM", "no-reply@attendancegeotracker.local")
    )

    # QR Code Settings
    QR_EXPIRY_MINUTES = 20

    # Geofencing Settings
    ALLOWED_RADIUS_METERS = 30

    # Admin Credentials
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")