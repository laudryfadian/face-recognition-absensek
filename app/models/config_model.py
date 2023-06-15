from datetime import datetime
from app.database import db

class Config(db.Document):
    versi1 = db.StringField(required=True)
    versi2 = db.StringField(required=True)
    versi3 = db.StringField(required=True)
    faceRecogModel = db.StringField(required=True)
    maintenance = db.BooleanField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'versi1': self.versi1,
            'versi2': self.versi2,
            'versi3': self.versi3,
            'faceRecogModel': self.faceRecogModel,
            'maintenance': self.maintenance
        }
    
    @staticmethod
    def get_by_id(config_id):
        try:
            company = Config.objects.get(id=config_id)
            return company.to_dict()
        except Config.DoesNotExist:
            return None
        
    