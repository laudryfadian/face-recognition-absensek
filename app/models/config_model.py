from datetime import datetime
from app.database import db

class Config(db.Document):
    faceRecogModel = db.StringField(required=True)
    distanceMetric = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'faceRecogModel': self.faceRecogModel,
            'distanceMetric': self.distanceMetric
        }
    
    @staticmethod
    def get_by_id(config_id):
        try:
            company = Config.objects.get(id=config_id)
            return company.to_dict()
        except Config.DoesNotExist:
            return None
    
    @staticmethod
    def update(config_id, faceRecogModel, distanceMetric):
        config = Config.objects(id=config_id).first()
        if not config:
          return None
        if faceRecogModel:
          config.faceRecogModel = faceRecogModel
        if distanceMetric:
          config.distanceMetric = distanceMetric
        config.save()
        return config.to_dict()        
    