from fastapi import FastAPI, Path
from mongo_db_atlas_adaptor import MongoAdaptor
from helpers import convert_mongo_results_to_dict

app = FastAPI()
mongo = MongoAdaptor()

@app.get("/users")
def get_users():
    results = mongo.find_all()
    return convert_mongo_results_to_dict(results)

@app.get("/users/phone_number/{phone_number}")
def get_user_by_phone_number(
        phone_number: str = Path(description="Insira o número de whatsapp do usuário")):

    results = mongo.find({'phone_number': phone_number})
    return convert_mongo_results_to_dict(results)
