from datetime import datetime

from bson import ObjectId
from app.database import db

class Category(db.Document):
    idCompany = db.ObjectIdField(required=True, default=lambda: ObjectId())
    name = db.StringField(required=True)
    absenCount = db.IntField(required=True)
    jam1 = db.StringField(required=True)
    jam2 = db.StringField(required=False)
    jam3 = db.StringField(required=False)
    jam4 = db.StringField(required=False)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'idCompany': str(self.idCompany),
            'absenCount': self.absenCount,
            'jam1': self.jam1,
            'jam2': self.jam2 if self.jam2 else None,
            'jam3': self.jam3 if self.jam3 else None,
            'jam4': self.jam4 if self.jam4 else None
        }

    @staticmethod
    def get_all():
        categorys = Category.objects.all()
        return [category.to_dict() for category in categorys]

    @staticmethod
    def create(name, idCompany, absenCount, jam1, jam2, jam3, jam4):
        category = Category(name=name, idCompany=idCompany,absenCount=absenCount, jam1=jam1, jam2=jam2, jam3=jam3, jam4=jam4)
        category.save()
        return category.to_dict()

    @staticmethod
    def update(category_id, name=None, idCompany=None, absenCount=None, jam1=None, jam2=None, jam3=None, jam4=None):
        category = Category.objects(id=category_id).first()
        if not category:
          return None
        if name:
          category.name = name
        if idCompany:
          category.idCompany = idCompany
        if absenCount:
          category.absenCount = absenCount
        if jam1:
          category.jam1 = jam1
        if jam2:
          category.jam2 = jam2
        if jam3:
          category.jam3 = jam3
        if jam4:
          category.jam4 = jam4
        category.save()
        return category.to_dict()

    @staticmethod
    def delete(category_id):
        category = Category.get_by_id(category_id)
        if not category:
            return None
        category.delete()
        return category.to_dict()
    
    @staticmethod
    def get_by_id(category_id):
        try:
            category = Category.objects.get(id=category_id)
            return category.to_dict()
        except Category.DoesNotExist:
            return None
    
    def get_by_id_company(idCompany):
        try:
            categorys = Category.objects.filter(idCompany=ObjectId(idCompany))
            return [category.to_dict() for category in categorys]
        except Category.DoesNotExist:
            return None
        
    