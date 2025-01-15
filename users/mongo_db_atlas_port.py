import parameters
import mongoengine
from models import Users


class MongoPort:

    def __init__(self):
        self.db = self.connect()

    @staticmethod
    def connect():
        users_conn = mongoengine.connect(host=parameters.MONGODB_USERS_HOST, username=parameters.MONGODB_USERS_USER,
                                         password=parameters.MONGODB_USERS_PASSWORD,
                                         db=parameters.MONGODB_USERS_DATABASE)
        return users_conn.get_database(parameters.MONGODB_USERS_DATABASE)

    def find_all(self):
        collection = self.db.get_collection(parameters.MONGODB_USERS_COLLECTION)
        return collection.find({})

    def find(self, query):
        collection = self.db.get_collection(parameters.MONGODB_USERS_COLLECTION)
        return collection.find(query)

    @staticmethod
    def upsert_one(user_data):
        Users.objects(phone_number=user_data.phone_number).upsert_one(phone_number=user_data.phone_number,
                                                                      first_name=user_data.first_name,
                                                                      last_name=user_data.last_name,
                                                                      ads_enabled=user_data.ads_enabled,
                                                                      is_active=user_data.is_active)

    @staticmethod
    def delete_one(phone_number):
        Users.objects(phone_number=phone_number).delete()

