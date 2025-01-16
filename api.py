from fastapi import FastAPI, Path
from mongo_db_atlas_adaptor import MongoAdaptor
from helpers import convert_mongo_results_to_dict
from models import Users

app = FastAPI()
mongo = MongoAdaptor()

@app.get("/users", status_code=200)
def get_users():
    results = mongo.find_all()
    return convert_mongo_results_to_dict(results)

@app.get("/users/phone_number/{phone_number}", status_code=200)
def get_user_by_phone_number(
        phone_number: str = Path(description="Insira o número de whatsapp do usuário")):

    results = mongo.find({'phone_number': phone_number})
    return convert_mongo_results_to_dict(results)

@app.post("/users", status_code=201)
def create_user(user: dict):
    try:
        user_obj = Users(phone_number=user.get('phone_number'),
                        first_name=user.get('first_name'),
                        last_name=user.get('last_name'),
                        ads_enabled=user.get('ads_enabled'),
                        is_active=user.get('is_active'),
                        updated_at=user.get('updated_at')
                        )
        mongo.upsert_one(user_obj)
        return {"message": "Usuário criado com sucesso"}
    except Exception as e:
        return {"error": str(e)}

