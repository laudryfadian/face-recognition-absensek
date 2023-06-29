from flask import Blueprint
from app.controllers.absen_controller import *

absen_bp = Blueprint('absen', __name__, url_prefix='/absen')

absen_bp.route('/cek/<string:user_id>', methods=['GET'])(absen_check)
absen_bp.route('/<string:jam>', methods=['POST'])(absen)
absen_bp.route('/history/<string:user_id>', methods=['GET'])(get_absen_by_id_user)
absen_bp.route('/today/<string:company_id>', methods=['GET'])(get_user_absen_today)