from flask import Blueprint

# Create blueprints
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
student_bp = Blueprint('student', __name__, url_prefix='/student')

# Note: do NOT import the submodules here. Importing them at package
# import time can cause a circular import with `app` (routes import app
# and app imports routes) which results in blueprint route decorators
# being applied after the blueprint has already been registered.
#
# Submodules (`routes.auth`, `routes.admin`, `routes.student`) should
# be imported explicitly in the application factory or `app.py` before
# calling `app.register_blueprint(...)` so that all routes are added
# to the blueprint prior to registration.