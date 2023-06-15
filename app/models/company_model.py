from datetime import datetime
from app.database import db

class Company(db.Document):
    name = db.StringField(required=True)
    address = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'address': self.address
        }

    @staticmethod
    def get_all():
        companys = Company.objects.all()
        return [company.to_dict() for company in companys]

    @staticmethod
    def create(name, address):
        company = Company(name=name, address=address)
        company.save()
        return company.to_dict()

    @staticmethod
    def update(company_id, name=None, address=None):
        company = Company.objects(id=company_id).first()
        if not company:
            return None
        if name:
            company.name = name
        if address:
            company.address = address
        company.save()
        return company.to_dict()

    @staticmethod
    def delete(company_id):
        company = Company.get_by_id(company_id)
        if not company:
            return None
        company.delete()
        return company.to_dict()
    
    @staticmethod
    def get_by_id(company_id):
        try:
            company = Company.objects.get(id=company_id)
            return company.to_dict()
        except Company.DoesNotExist:
            return None
        
    