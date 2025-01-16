from datetime import datetime
import mongoengine as mongo


class Users(mongo.Document):
    phone_number = mongo.StringField(required=True, unique=True)
    first_name = mongo.StringField()
    last_name = mongo.StringField()
    ads_enabled = mongo.BooleanField(default=True)
    is_active = mongo.BooleanField(default=True)
    updated_at = mongo.DateTimeField(default=datetime.now())


