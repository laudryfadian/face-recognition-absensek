from datetime import datetime

from bson import ObjectId
from app.database import db

class Setting(db.Document):
    idUser = db.ObjectIdField(required=True, default=lambda: ObjectId())
    idCompany = db.ObjectIdField(required=True, default=lambda: ObjectId())
    absenCount = db.IntField(required=True)
    jam1 = db.StringField(required=True)
    jam2 = db.StringField(required=False)
    jam3 = db.StringField(required=False)
    jam4 = db.StringField(required=False)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'idUser': str(self.idUser),
            'idCompany': str(self.idCompany),
            'absenCount': self.absenCount,
            'jam1': self.jam1,
            'jam2': self.jam2 if self.jam2 else None,
            'jam3': self.jam3 if self.jam3 else None,
            'jam4': self.jam4 if self.jam4 else None
        }

    @staticmethod
    def get_all():
        settings = Setting.objects.all()
        return [setting.to_dict() for setting in settings]

    @staticmethod
    def create(idUser, idCompany, absenCount, jam1, jam2, jam3, jam4):
        setting = Setting(idUser=idUser, idCompany=idCompany,absenCount=absenCount, jam1=jam1, jam2=jam2, jam3=jam3, jam4=jam4)
        setting.save()
        return setting.to_dict()

    @staticmethod
    def update(setting_id, idUser=None, idCompany=None, absenCount=None, jam1=None, jam2=None, jam3=None, jam4=None):
        setting = Setting.objects(id=setting_id).first()
        if not setting:
          return None
        if idUser:
          setting.idUser = idUser
        if idCompany:
          setting.idCompany = idCompany
        if absenCount:
          setting.absenCount = absenCount
        if jam1:
          setting.jam1 = jam1
        if jam2:
          setting.jam2 = jam2
        if jam3:
          setting.jam3 = jam3
        if jam4:
          setting.jam4 = jam4
        setting.save()
        return setting.to_dict()

    @staticmethod
    def delete(setting_id):
        setting = Setting.get_by_id(setting_id)
        if not setting:
            return None
        setting.delete()
        return setting.to_dict()
    
    @staticmethod
    def get_by_id(setting_id):
        try:
            setting = Setting.objects.get(id=setting_id)
            return setting.to_dict()
        except Setting.DoesNotExist:
            return None
    
    def get_by_id_company(idCompany):
        try:
            settings = Setting.objects.filter(idCompany=ObjectId(idCompany))
            return [setting.to_dict() for setting in settings]
        except Setting.DoesNotExist:
            return None
        
    