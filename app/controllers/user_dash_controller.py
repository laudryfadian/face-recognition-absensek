from flask import request
from app.models.user_model import User
from app.utils import *

def login_admin():
  email = request.json['email']
  password = request.json['password']
  
  emailCek = User.get_by_email(email)
  if not emailCek:
    return error_response("email salah")
  
  if emailCek['password'] != password:
    return error_response("password salah")
  
  if emailCek['jobType'] != 'admin':
    return error_response("kamu bukan admin")
  
  return success_response(emailCek)
