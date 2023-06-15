from flask import Blueprint
from app.controllers.user_dash_controller import *

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

auth_bp.route('/logindash', methods=['POST'])(login_admin)

