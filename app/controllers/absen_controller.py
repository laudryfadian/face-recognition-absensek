from flask import request
from app.models.user_model import User
from app.models.category_model import Category
from app.models.absen_model import Absen
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
  timeNow = dt.strftime('%H%M') #HH:MM
  
  toleransiAwalAbsen = 100 #1 jam
  toleransiKeterlambatan = 15 #15 menit
  
  match category['absenCount']:
    case 1:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 1:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
      userTime = int(category['jam1']) #jam absen user
      absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
      
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
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam1']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam2']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case 3:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 3:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      if len(absenNow) == 0:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam1']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam2']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
      
      if len(absenNow) == 2:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam3']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
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
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam1']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam2']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
      
      if len(absenNow) == 2:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam3']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam3"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 3:
        absenTime = int(timeNow) - toleransiAwalAbsen #batas awal absen
        userTime = int(category['jam4']) #jam absen user
        absenTimeWithToleransi = userTime + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam4"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case _:
      return error_response('Terjadi kesalahan, mohon hubungi admin')

def absen_jam1():
  idUser = request.json['idUser']
  idCompany = request.json['idCompany']
  image = request.json['image']
  
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  
  cek = Absen.get_by_id_user_n_datenow_n_type(idUser, dateNow, "jam1")
  if cek[0]:
    return error_response("Kamu sudah absen!")
  
  user = User.get_by_id(idUser)
  if not user:
    return error_response("user tidak ada")
  
  faceRecog = face_recog_deepface(image1=user['image'], image2=image, model="VGG-Face") #user['image'] belum ada di model
  if not faceRecog:
    return error_response("Face Recognition gagal, harap coba lagi")
  
  absen = Absen.create(idUser=idUser, image=image, approve="Aproved", date=dateNow, idCompany=idCompany, status="Absen Masuk", type="Jam1")
  return success_response(absen)