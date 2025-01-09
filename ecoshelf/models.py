import mongoengine as mongo


class UserPreferences(mongo.document):
    ads_enabled = mongo.BooleanField(default=True)

class Users(mongo.Document):
    phone_number = mongo.StringField(required=True, unique=True)
    first_name = mongo.StringField()
    last_name = mongo.StringField()
    preferences = mongo.ListField(UserPreferences, required=True)
    created_at = mongo.DateTimeField(required=True)
    updated_at = mongo.DateTimeField(required=True)
    last_seen = mongo.DateTimeField(required=True)
    is_active = mongo.DateTimeField(required=True)
