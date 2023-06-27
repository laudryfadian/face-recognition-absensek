from flask import request
from app.models.user_model import User
from app.models.company_model import Company
from app.utils import *

def get_users():
    users = User.get_all()
    if users:
        for i in range(len(users)):
            company = Company.get_by_id(users[i]['idCompany'])
            users[i]['idCompany'] = company
    # print(users)
    return success_response(users)

def create_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    job = request.json['job']
    superUser = request.json['superUser']
    salary = request.json['salary']
    isAbsen = request.json['isAbsen']
    jobType = request.json['jobType']
    idCompany = request.json['idCompany']
    
    emailCek = User.get_by_email(email)
    if emailCek:
        return error_response("email sudah ada")
    
    user = User.create(name, email, password, phone, job, superUser, salary, jobType, idCompany, isAbsen)
    if not user:
        return error_response("gagal membuat akun")
    
    return success_response(user)

def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return success_response(user)
    else:
        return error_response("User tidak ada")

def update_user(user_id):
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    job = request.json['job']
    superUser = request.json['superUser']
    salary = request.json['salary']
    isAbsen = request.json['isAbsen']
    jobType = request.json['jobType']
    idCompany = request.json['idCompany']
    
    user = User.update(user_id=user_id, name=name, email=email, idCompany=idCompany, isAbsen=isAbsen, job=job, jobType=jobType, password=password, phone=phone, salary=salary, superUser=superUser)
    if user:
        return success_response(user)
    else:
        return error_response("User not found")

def delete_user(user_id):
    user = User.delete(user_id)
    if user:
        return success_response(user)
    else:
        return error_response("User not found")
    
def get_user_by_id_company(company_id):
    # user = User.get_by_id_company(company_id)
    # print(user)
    # if user:
    #     return success_response(user)
    # else:
    #     return error_response("User tidak ada")
    user = User.get_by_id_company(company_id)
    if user:
        for i in range(len(user)):
            company = Company.get_by_id(user[i]['idCompany'])
            user[i]['idCompany'] = company
    return success_response(user)