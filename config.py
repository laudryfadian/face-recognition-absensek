import os

class Config:
    # MongoDB configuration
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:3001/cobalagi')
    }