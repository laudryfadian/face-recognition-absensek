from flask_mongoengine import MongoEngine

# Initialize the database
db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
