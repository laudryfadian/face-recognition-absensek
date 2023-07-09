from datetime import datetime

from bson import ObjectId
from app.database import db

class Unregister(db.Document):
  idUser = db.ObjectIdField(required=True, default=lambda: ObjectId())
  idCompany = db.ObjectIdField(required=True, default=lambda: ObjectId())
  image = db.StringField(required=True)
  created_at = db.DateTimeField(default=datetime.now)
  
  def to_dict(self):
    return {
      'id': str(self.id),
      'idUser': str(self.idUser),
      'idCompany': str(self.idCompany),
      'image': self.image
    }
  
  @staticmethod
  def get_all():
      unregs = Unregister.objects.all()
      return [unreg.to_dict() for unreg in unregs]
    
  @staticmethod
  def create(idUser, idCompany, image):
      unreg = Unregister(idUser=idUser, idCompany=idCompany, image=image)
      unreg.save()
      return unreg.to_dict()
    
  @staticmethod
  def update(unreg_id, idUser=None, idCompany=None, image=None):
      unreg = Unregister.objects(id=unreg_id).first()
      if not unreg:
        return None
      if idUser:
        unreg.idUser = idUser
      if idCompany:
        unreg.idCompany = idCompany
      if image:
        unreg.absenCount = image
      unreg.save()
      return unreg.to_dict()
    
  @staticmethod
  def delete_by_id(unreg_id):
    try:
      unreg = Unregister.objects.get(id=unreg_id)
      unreg.delete()
      return unreg.to_dict()
    except Unregister.DoesNotExist:
      return None
  
  @staticmethod
  def get_by_id(unreg_id):
      try:
          unreg = Unregister.objects.get(id=unreg_id)
          return unreg.to_dict()
      except Unregister.DoesNotExist:
          return None
  
  def get_by_id_company(idCompany):
      try:
          unregs = Unregister.objects.filter(idCompany=ObjectId(idCompany))
          return [unreg.to_dict() for unreg in unregs]
      except Unregister.DoesNotExist:
          return None
        
  def get_by_id_user(idUser):
      try:
          unregs = Unregister.objects.filter(idUser=ObjectId(idUser))
          return [unreg.to_dict() for unreg in unregs]
      except Unregister.DoesNotExist:
          return None