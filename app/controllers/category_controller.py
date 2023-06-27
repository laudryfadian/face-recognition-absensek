from flask import request
from app.models.category_model import Category
from app.models.company_model import Company
from app.utils import *

def get_categorys():
    categorys = Category.get_all()
    if categorys:
        for i in range(len(categorys)):
            company = Company.get_by_id(categorys[i]['idCompany'])
            categorys[i]['idCompany'] = company
        
    return success_response(categorys)

def create_category():
    name = request.json['name']
    idCompany = request.json['idCompany']
    absenCount = request.json['absenCount']
    jam1 = request.json['jam1']
    jam2 = request.json['jam2']
    jam3 = request.json['jam3']
    jam4 = request.json['jam4']
    
    category = Category.create(name, idCompany, absenCount, jam1, jam2, jam3, jam4)
    return success_response(category)

def get_category(category_id):
    category = Category.get_by_id(category_id)
    if category:
        return success_response(category)
    else:
        return error_response("Category tidak ada")

def update_category(category_id):
    name = request.json['name']
    idCompany = request.json['idCompany']
    absenCount = request.json['absenCount']
    jam1 = request.json['jam1']
    jam2 = request.json['jam2']
    jam3 = request.json['jam3']
    jam4 = request.json['jam4']
    
    category = Category.update(category_id, name=name, idCompany=idCompany, absenCount=absenCount, jam1=jam1, jam2=jam2, jam3=jam3, jam4=jam4)
    if category:
        return success_response(category)
    else:
        return error_response("Category tidak ada")

def delete_category(category_id):
    category = Category.delete(category_id)
    if category:
        return success_response(category)
    else:
        return error_response("Category tidak ada")
      
def get_category_by_id_company(company_id):
    categorys = Category.get_by_id_company(company_id)
    if categorys:
        for i in range(len(categorys)):
            company = Company.get_by_id(categorys[i]['idCompany'])
            categorys[i]['idCompany'] = company
    return success_response(categorys)
