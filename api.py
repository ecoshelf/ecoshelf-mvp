from fastapi import FastAPI, Path, Query
from mongo_db_atlas_adaptor import MongoAdaptor
from helpers import convert_mongo_results_to_dict
from bson import ObjectId

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

@app.post("/users")
def create_user(user: dict):
    try:
        results = mongo.upsert_one(user)
        return {"message": "Usuário criado com sucesso", "id": str(results.inserted_id)}
    except Exception as e:
        return {"error": str(e)}




@app.patch("/users/{user_id}/is_active/")
def update_is_active(
    user_id: str = Path(description="ID do usuário no banco de dados"),
    is_active: bool = Query(description="Novo status de is_active")
):
    try:
        user_id = ObjectId(user_id)
        results = mongo.upsert_one(
            {"_id": user_id},
            {"$set": {"is_active": is_active}}
        )
        if results.matched_count == 0:
            return {"message": "Usuário não encontrado"}
        return {"message": "Status do usuário atualizado com sucesso"}
    except Exception as e:
        return {"error": str(e)}
