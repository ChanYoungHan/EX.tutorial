from fastapi import FastAPI
from typing import Union

from app.database.db_sqlalchemy import DB_SQLAlchemy, UserInfo, CreditCradInfo


app = FastAPI()
db = DB_SQLAlchemy()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_user_credit_info/{name}")
def read_item(name: str, q: Union[str, None] = None):
    res_user_info: UserInfo = db.get_user_info(name=name)
    res_credit_card_info: CreditCradInfo = db.get_credit_card_info(name=name)

    return {
        "user_name": name,
        "user_id": res_user_info.id,
        "credit_card_id": res_credit_card_info.id,
        "credit_card_bank_name": res_credit_card_info.bank_name,
    }
