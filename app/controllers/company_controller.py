from flask import request
from app.models.company_model import Company
from app.utils import *

def get_companys():
    companys = Company.get_all()
    return success_response(companys)

def create_company():
    name = request.json['name']
    address = request.json['address']
    
    company = Company.create(name, address)
    return success_response(company)

def get_company(company_id):
    company = Company.get_by_id(company_id)
    if company:
        return success_response(company)
    else:
        return error_response("Company tidak ada")

def update_company(company_id):
    name = request.json['name']
    address = request.json['address']
    
    company = Company.update(company_id, name=name, address=address)
    if company:
        return success_response(company)
    else:
        return error_response("Company tidak ada")

def delete_company(company_id):
    company = Company.delete(company_id)
    if company:
        return success_response(company)
    else:
        return error_response("Company tidak ada")
