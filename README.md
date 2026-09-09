# GeoAttend — QR Code Attendance with Geofencing

> A secure, web-based attendance management system that combines **QR code verification**, **GPS-based geofencing**, and **proxy-attempt detection** to automate and secure classroom attendance.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![Deployment](https://img.shields.io/badge/Deployed-Render-46E3B7)](https://render.com/)

---

## 🚀 Live Demo

**Live Application:**  
https://geoattend-12dj.onrender.com

> The application is deployed using Render with MongoDB Atlas as the cloud database.

### Demo Admin Login

Email: admin@edu.com
Password: ********

The demo account is provided for evaluation purposes.
---

## 📌 Overview

GeoAttend is a QR code-based attendance management system designed to make classroom attendance faster, more reliable, and resistant to proxy attendance.

Instead of relying only on a QR code, the system verifies the student's **physical location** using GPS coordinates. Attendance is recorded only when the student is within the configured classroom geofence.

The system also records unsuccessful attendance attempts when a student is outside the permitted geographical area.

---

## ✨ Key Features

### 👨‍💼 Admin Management

- Secure admin authentication
- Admin dashboard
- Classroom management
- Student management
- Add students individually
- Bulk student import using Excel
- Generate temporary attendance QR codes
- View attendance reports
- View and track proxy/invalid attendance attempts

### 👨‍🎓 Student Features

- Student authentication
- Student dashboard
- QR code scanning
- Automatic GPS location retrieval
- Geofence-based attendance verification
- Attendance history

### 🔐 Security & Validation

- Password hashing using bcrypt
- Flask-Login based authentication
- Role-based access control
- Temporary QR attendance sessions
- QR/session expiry validation
- Duplicate attendance prevention
- GPS-based geofence verification
- Proxy-attempt logging
- Environment-variable based configuration

### 📧 Email

- Email-based student credential functionality
- Gmail SMTP integration
- Secure email credentials through environment variables

---

## 🧠 How It Works

The attendance process follows these steps:

```text
Admin Login
     ↓
Create Classroom
     ↓
Add / Import Students
     ↓
Generate Attendance QR Code
     ↓
Student Logs In
     ↓
Student Scans QR Code
     ↓
Validate QR Session
     ↓
Get Student GPS Location
     ↓
Check Geofence
     ↓
 ┌───────────────┐
 │ Within Radius?│
 └───────┬───────┘
         │
    ┌────┴────┐
    ↓         ↓
   YES        NO
    ↓         ↓
Attendance   Proxy Attempt
  Marked       Logged
