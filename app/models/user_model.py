from datetime import datetime

from bson import ObjectId
from app.database import db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    phone = db.StringField(required=True)
    job = db.StringField(required=True)
    superUser = db.BooleanField(required=True)
    salary = db.IntField(required=True)
    isAbsen = db.BooleanField(required=True)
    jobType = db.StringField(required=True)
    idCompany = db.ObjectIdField(required=True, default=lambda: ObjectId())
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'job': self.job,
            'superUser': self.superUser,
            'salary': self.salary,
            'isAbsen': self.isAbsen,
            'jobType': self.jobType,
            'idCompany': str(self.idCompany)
        }

    @staticmethod
    def get_all():
        users = User.objects.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def create(name, email, password, phone, job, superUser, salary, jobType, idCompany, isAbsen):
        user = User(name=name, email=email, password=password, phone=phone, job=job, superUser=superUser, salary=salary, jobType=jobType, idCompany=idCompany, isAbsen=isAbsen)
        user.save()
        return user.to_dict()

    @staticmethod
    def update(user_id, name=None, email=None, password=None, phone=None, job=None, superUser=None, salary=None, jobType=None, idCompany=None, isAbsen=None):
        user = User.objects(id=user_id).first()
        if not user:
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        if phone:
            user.phone = phone
        if job:
            user.job = job
        if superUser:
            user.superUser = superUser
        if salary:
            user.salary = salary
        if jobType:
            user.jobType = jobType
        if idCompany:
            user.idCompany = idCompany
        user.isAbsen = isAbsen
        user.save()
        return user.to_dict()

    @staticmethod
    def delete(user_id):
        user = User.get_by_id(user_id)
        if not user:
            return None
        user.delete()
        return user.to_dict()
    
    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.objects.get(id=user_id)
            return user.to_dict()
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def get_by_email(email):
        try:
            user = User.objects.get(email=email)
            return user.to_dict()
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def get_by_id_company(idCompany):
        try:
            users = User.objects.filter(idCompany=ObjectId(idCompany))
            return [user.to_dict() for user in users]
        except User.DoesNotExist:
            return None
    