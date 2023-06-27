from flask import Blueprint
from app.controllers.absen_controller import *

absen_bp = Blueprint('absen', __name__, url_prefix='/absen')

absen_bp.route('/cek/<string:user_id>', methods=['GET'])(absen_check)
absen_bp.route('/jam1', methods=['POST'])(absen_jam1)