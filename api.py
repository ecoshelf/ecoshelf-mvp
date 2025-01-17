from fastapi import FastAPI, Path, Response
from mongo_db_atlas_adaptor import MongoAdaptor
from helpers import convert_mongo_results_to_dict
from models import Users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
mongo = MongoAdaptor()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users", status_code=200)
def get_users(response: Response):
    results = mongo.find_all()
    results_len = len(list(results))
    response.headers['X-Total-Count'] = str(results_len)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    response.headers["Content-Range"] = "bytes: 0-9/*"
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

