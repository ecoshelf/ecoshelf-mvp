import settings
import mongoengine
from models import Users

class MongoPort:

    def __init__(self):
        self.db = self.connect()

    @staticmethod
    def connect():
        users_conn = mongoengine.connect(host=settings.MONGODB_USERS_HOST, username=settings.MONGODB_USERS_USER,
                                         password=settings.MONGODB_USERS_PASSWORD,
                                         db=settings.MONGODB_USERS_DATABASE)
        return users_conn.get_database(settings.MONGODB_USERS_DATABASE)

    def find_all(self):
        collection = self.db.get_collection(settings.MONGODB_USERS_COLLECTION)
        return collection.find({})

    def find(self, query):
        collection = self.db.get_collection(settings.MONGODB_USERS_COLLECTION)
        return collection.find(query)

    @staticmethod
    def upsert_one(user_object):
        return Users.objects(phone_number=user_object.phone_number).upsert_one(phone_number=user_object.phone_number,
                                                                               first_name=user_object.first_name,
                                                                               last_name=user_object.last_name,
                                                                               ads_enabled=user_object.ads_enabled,
                                                                               is_active=user_object.is_active,
                                                                               updated_at=user_object.updated_at)

    @staticmethod
    def delete_one(phone_number):
        Users.objects(phone_number=phone_number).delete()
