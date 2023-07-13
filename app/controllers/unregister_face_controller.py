from flask import request
from app.models.unregister_face_mode import Unregister
from app.models.user_model import User
from app.models.company_model import Company
from app.utils import *

def get_unregs():
    unregs = Unregister.get_all()
    if unregs:
        for i in range(len(unregs)):
            company = Company.get_by_id(unregs[i]['idCompany'])
            user = User.get_by_id(unregs[i]['idUser'])
            unregs[i]['idCompany'] = company
            unregs[i]['idUser'] = user
        
    return success_response(unregs)

def create_unreg():
    email = request.json['email']
    password = request.json['password']
    image = request.json['image']
    
    emailCek = User.get_by_email(email)
    if not email:
      return error_response("Email Salah")
    
    if emailCek['password'] != password:
      return error_response("Password Salah")
    
    cekVerify = Unregister.get_by_id_user(emailCek['id'])
    if cekVerify:
      return error_response("Wajahmu masih di verifikasi! tunggu...")

    unreg = Unregister.create(idUser=emailCek['id'], idCompany=emailCek['idCompany'], image=image)
    if not unreg:
      return error_response("gagal mendaftarkan wajah")
      
    return success_response(unreg)

def get_unreg(unreg_id):
    unreg = Unregister.get_by_id(unreg_id)
    if unreg:
        return success_response(unreg)
    else:
        return error_response("Unregister tidak ada")

def update_unreg(unreg_id):
    idUser = request.json['idUser']
    idCompany = request.json['idCompany']
    image = request.json['image']
    
    unreg = Unregister.update(unreg_id, idUser=idUser, idCompany=idCompany, image=image)
    if unreg:
        return success_response(unreg)
    else:
        return error_response("Unregister tidak ada")

def delete_unreg(unreg_id):
    unreg = Unregister.delete(unreg_id)
    if unreg:
        return success_response(unreg)
    else:
        return error_response("Unregister tidak ada")
      
def get_unreg_by_id_company(company_id):
    unregs = Unregister.get_by_id_company(company_id)
    if unregs:
        for i in range(len(unregs)):
            company = Company.get_by_id(unregs[i]['idCompany'])
            user = User.get_by_id(unregs[i]['idUser'])
            unregs[i]['idCompany'] = company
            unregs[i]['idUser'] = user
    return success_response(unregs)

def approve_face(unreg_id):
    unreg = Unregister.get_by_id(unreg_id)
    if not unreg:
        return error_response("Data tidak ada")
    
    update = User.update(user_id=unreg['idUser'], image=unreg['image'], isAbsen=False, verify=True)
    if not update:
        return error_response("Update gagal")
    
    delete = Unregister.delete_by_id(unreg_id=unreg_id)
    if not delete:
        return error_response("Gagal menghapus")
    
    return success_response(update)

def not_approve_face(unreg_id):
    unreg = Unregister.get_by_id(unreg_id)
    if not unreg:
        return error_response("Data tidak ada")
    
    delete = Unregister.delete_by_id(unreg_id=unreg['id'])
    if not delete:
        return error_response("Gagal menghapus")
    
    return success_response(delete)
    