from flask import request
from app.models.user_model import User
from app.models.category_model import Category
from app.models.absen_model import Absen
from app.models.company_model import Company
from app.controllers.face_recognition import *
from app.utils import *

def absen_check(user_id):
  user = User.get_by_id(user_id)
  if not user:
    return error_response("user tidak ada")
  
  category = Category.get_by_id(user['idCategory'])
  if not category:
    return error_response("user belum punya category")
  
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d') #YYYY-MM-DD
  print(dt)
  print(dateNow)
  timeNow = dt.strftime('%H%M') #HH:MM
  
  toleransiAwalAbsen = 100 #1 jam
  toleransiKeterlambatan = 15 #15 menit
  
  match category['absenCount']:
    case 1:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 1:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      absenTime = int(timeNow)  #batas awal absen
      userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
      absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
      
      if absenTime < userTime:
        return success_response({'message': 'Belum saatnya absen', 'route': "/"})
      
      elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
        return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})
      
      else:
        return success_response({'message': 'Telat absen', 'route': "/"})
      
    case 2:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 2:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      if len(absenNow) == 0:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam2']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam2']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case 3: #SUDAH BENAR
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 3:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      if len(absenNow) == 0:
        absenTime = int(timeNow) #batas awal absen
        userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/jam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam2']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam2']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/jam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
      
      if len(absenNow) == 2:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam3']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam3']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam3"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case 4:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 4:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      if len(absenNow) == 0:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam2']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam2']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
      
      if len(absenNow) == 2:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam3']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam3']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam3"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 3:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam4']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam4']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam4"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case _:
      return error_response('Terjadi kesalahan, mohon hubungi admin')

def absen(jam): #param jam = jam1/jam2/jam3/jam4
  idUser = request.json['idUser']
  idCompany = request.json['idCompany']
  image = request.json['image']
  lat = request.json['lat']
  long = request.json['long']
  
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  timeNow = dt.strftime('%H%M') #HH:MM
  
  # cek = Absen.get_by_id_user_n_datenow_n_type(idUser, dateNow, jam)
  # if cek[0]:
  #   return error_response("Kamu sudah absen!")
  
  user = User.get_by_id(idUser)
  if not user:
    return error_response("user tidak ada")
  
  faceRecog = face_recog_deepface(image1=user['image'], image2=image, model="ArcFace")
  if not faceRecog['verified']:
    return error_response("Face Recognition gagal, harap coba lagi")
  
  absen = Absen.create(idUser=idUser, image=image, approve="Aproved", date=dateNow, idCompany=idCompany, status="Absen Masuk", type=jam, lat=lat, long=long, time=timeNow, deepface=faceRecog)
  
  return success_response(absen)

def get_absen_by_id_user(user_id):
  absens = Absen.get_by_id_user(user_id)
  if absens:
    return success_response(absens)
  else:
    return error_response("gagal lihat history")
  
def get_absen_by_id_user_n_date(user_id):
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  
  absens = Absen.get_by_id_user_n_datenow(user_id, dateNow)
  return success_response(absens)
  
def get_user_absen_today(company_id):
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  
  absen = Absen.get_by_id_company_n_date(company_id, dateNow)
  if absen:
    for i in range(len(absen)):
      user = User.get_by_id(absen[i]['idUser'])
      if not user:
        return error_response("user tidak ada")

      absen[i]['idUser'] = {'id': str(user['id']), 'name': user['name']}
      
  return success_response(absen)

def get_absen_by_date(date):
  absens = Absen.get_by_datenow(datenow=date)
  if absens:
    for i in range(len(absens)):
      user = User.get_by_id(absens[i]['idUser'])
      company = Company.get_by_id(absens[i]['idCompany'])
      absens[i]['idUser'] = user
      absens[i]['idCompany'] = company
  
  return success_response(absens)

def get_absen_by_date_n_company(company_id, date):
  absens = Absen.get_by_datenow_n_company(company=company_id,datenow=date)
  if absens:
    for i in range(len(absens)):
      user = User.get_by_id(absens[i]['idUser'])
      company = Company.get_by_id(absens[i]['idCompany'])
      absens[i]['idUser'] = user
      absens[i]['idCompany'] = company
  
  return success_response(absens)