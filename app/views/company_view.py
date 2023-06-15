from flask import Blueprint
from app.controllers.company_controller import *

company_bp = Blueprint('company', __name__, url_prefix='/companys')

company_bp.route('', methods=['GET'])(get_companys)
company_bp.route('', methods=['POST'])(create_company)
company_bp.route('/<string:company_id>', methods=['GET'])(get_company)
company_bp.route('/<string:company_id>', methods=['PUT'])(update_company)
company_bp.route('/<string:company_id>', methods=['DELETE'])(delete_company)
