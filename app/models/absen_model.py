from datetime import datetime
from bson import ObjectId
from app.database import db

class Absen(db.Document):
  idUser = db.ObjectIdField(required=True, default=lambda: ObjectId())
  idCompany = db.ObjectIdField(required=True, default=lambda: ObjectId())
  status = db.StringField(required=True) #Datang/Pulang/DLL
  type = db.StringField(required=True) #jam1/jam2/jam3/jam4
  date = db.StringField(required=True) #2023-06-27
  time = db.StringField(required=True) #0800
  image = db.StringField(required=True)
  approve = db.BooleanField(required=True)
  lat = db.StringField(required=True)
  long = db.StringField(required=True)
  deepface = db.DynamicField()
  created_at = db.DateTimeField(default=datetime.now)
  
  def to_dict(self):
    return {
      'id': str(self.id),
      'idUser': str(self.idUser),
      'idCompany': str(self.idCompany),
      'status': self.status,
      'type': self.type,
      'date': self.date,
      'time': self.time,
      'image': self.image,
      'approve': self.approve,
      'lat': self.lat,
      'long': self.long
    }
    
  @staticmethod
  def get_all():
    absens = Absen.objects.all()
    return [absen.to_dict() for absen in absens]
    
  @staticmethod
  def create(idUser, idCompany, status, type, date, image, approve, lat, long, time, deepface):
      absen = Absen(idUser=idUser, idCompany=idCompany, status=status, type=type, date=date, image=image, approve=approve, lat=lat, long=long, time=time, deepface=deepface)
      absen.save()
      return absen.to_dict()
    
  @staticmethod
  def update(absen_id, idUser=None, idCompany=None, status=None, type=None, date=None, image=None, approve=None, lat=None, long=None, time=None):
      absen = Absen.objects(id=absen_id).first()
      if not absen:
        return None
      if idUser:
        absen.idUser = idUser
      if idCompany:
        absen.idCompany = idCompany
      if status:
        absen.status = status
      if type:
        absen.type = type
      if date:
        absen.date = date
      if image:
        absen.image = image
      if approve:
        absen.approve = approve
      if lat:
        absen.lat = lat
      if long:
        absen.long = long
      if time:
        absen.time = time
      absen.save()
      return absen.to_dict()
    
  @staticmethod
  def delete(absen_id):
      absen = Absen.get_by_id(absen_id)
      if not absen:
          return None
      absen.delete()
      return absen.to_dict()
  
  @staticmethod
  def get_by_id(absen_id):
      try:
          absen = Absen.objects.get(id=absen_id)
          return absen.to_dict()
      except Absen.DoesNotExist:
          return None
  
  def get_by_id_company(idCompany):
      try:
          absens = Absen.objects.filter(idCompany=ObjectId(idCompany))
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
  
  def get_by_id_company_n_date(idCompany, date):
      try:
          absens = Absen.objects.filter(idCompany=ObjectId(idCompany), date=date)
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
        
  def get_by_id_user(idUser):
      try:
          absens = Absen.objects.filter(idUser=ObjectId(idUser))
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
        
  def get_by_id_user_n_datenow(idUser, now):
      try:
          absens = Absen.objects.filter(idUser=ObjectId(idUser), date=now)
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
        
  def get_by_id_user_n_datenow_n_type(idUser, now, type):
      try:
          absens = Absen.objects.filter(idUser=ObjectId(idUser), date=now, type=type)
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
        
  @staticmethod
  def get_by_datenow(datenow):
      try:
          absens = Absen.objects.filter(date=datenow)
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
  
  @staticmethod
  def get_by_datenow_n_company(company, datenow):
      try:
          absens = Absen.objects.filter(idCompany=company ,date=datenow)
          return [absen.to_dict() for absen in absens]
      except Absen.DoesNotExist:
          return None
      
  