from flask import request
from app.models.setting_model import Setting
from app.models.user_model import User
from app.models.company_model import Company
from app.utils import *

def get_settings():
    settings = Setting.get_all()
    if settings:
        for i in range(len(settings)):
            user = User.get_by_id(settings[i]['idUser'])
            company = Company.get_by_id(settings[i]['idCompany'])
            settings[i]['idUser'] = user
            settings[i]['idCompany'] = company
        
    return success_response(settings)

def create_setting():
    idUser = request.json['idUser']
    idCompany = request.json['idCompany']
    absenCount = request.json['absenCount']
    jam1 = request.json['jam1']
    jam2 = request.json['jam2']
    jam3 = request.json['jam3']
    jam4 = request.json['jam4']
    
    setting = Setting.create(idUser, idCompany, absenCount, jam1, jam2, jam3, jam4)
    return success_response(setting)

def get_setting(setting_id):
    setting = Setting.get_by_id(setting_id)
    if setting:
        return success_response(setting)
    else:
        return error_response("Setting tidak ada")

def update_setting(setting_id):
    idUser = request.json['idUser']
    idCompany = request.json['idCompany']
    absenCount = request.json['absenCount']
    jam1 = request.json['jam1']
    jam2 = request.json['jam2']
    jam3 = request.json['jam3']
    jam4 = request.json['jam4']
    
    setting = Setting.update(setting_id, idUser=idUser, idCompany=idCompany, absenCount=absenCount, jam1=jam1, jam2=jam2, jam3=jam3, jam4=jam4)
    if setting:
        return success_response(setting)
    else:
        return error_response("Setting tidak ada")

def delete_setting(setting_id):
    setting = Setting.delete(setting_id)
    if setting:
        return success_response(setting)
    else:
        return error_response("Setting tidak ada")
