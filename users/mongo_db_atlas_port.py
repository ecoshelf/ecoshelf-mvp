from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import parameters


class ForStoringUsers:
    """Naming conventions:
    https://dev.to/xoubaman/understanding-hexagonal-architecture-3gk
    """

    def __init__(self):
        self.uri = parameters.MONGODB_USERS_URI
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))

    def test_connection(self):
        """
        Send a ping to confirm a successful connection
        """

        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

