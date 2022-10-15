from pyexpat import model
from urllib.request import Request
# import fastapi
from fastapi import FastAPI, Body, Path, Query
import copy
import pydantic_models
from database import *
import crud


import datetime
# import config
import pydantic_models
import bit
import db
import models 
import pony
pony.MODE = 'INTERACTIVE'
# import pydantic
from datetime import datetime
from pony.orm import *


app = FastAPI()


# Информация о состоянии баланса по id
@app.get('/get_user_balance_by_id/{user_id:int}')
@crud.db_session
def get_user_balance(user_id):
    crud.update_wallet_balance(models.User[user_id].wallet)
    return models.User[user_id].wallet.balance


@app.get('/get_total_balance')
@crud.db_session
def get_total_balance():
    # balance = 0
    crud.update_all_wallets()
    return (sum( b.balance for b in models.Wallet))


#  Все юзеры
@app.get("/users/all")
@crud.db_session
def get_users(skip: int = 0, limit: int = 10):
    return select(a.id for a in models.User)[:]


@app.get('/get_info_by_user_id/{user_id:int}')
@crud.db_session
def get_info_about_user(user_id):
    return crud.get_user_info(models.User[user_id])

# Внесение новго пользователя в бд
@app.post('/user/create')
@crud.db_session
def create_user(user: pydantic_models.User_to_create = Body()):
    return crud.create_user(tg_id=user.tg_ID,
                            nick=user.nick if user.nick else None).to_dict()
    # fake_database['users'].append(user)
    # return {'User Created!': user}

# функция для обновления информации о пользователе
@app.put('/user/{user_id}')
@crud.db_session
def update_user(user_id: int, user: pydantic_models.User_to_update = Body()):
    return crud.update_user(user).to_dict()

# Получить всех юзеров
@app.get("/users")
@crud.db_session
def get_users():
    users = []
    for user in models.User.select()[:]:
        users.append(user.to_dict())
    return users

# Получаем юзера по айди его телеги
@app.get('/user_by_tg_id/{tg_ID}')
@crud.db_session
def get_user_by_tg(tg_ID : int = Path()):
    return crud.get_user_info(crud.get_user_by_tg_id(tg_ID))
    

# функция удаления юзера
@app.delete('/user/{user_id}')
@crud.db_session
def delete_user(user_id: int = Path()): # используя Path() мы явно указываем, что переменную нужно брать из пути
    crud.get_user_by_id(user_id).delete()
    return True


@app.post("/create_transaction")
@crud.db_session
def create_transaction(transaction : pydantic_models.Create_Transaction = Body()):
    pass
    # return crud.create_transaction(sender: models.User, amount_btc_without_fee = transaction.amount_btc_without_fee, receiver_address = transaction.receiver_address, fee: float | None = None, testnet: bool = False)


@app.get("/get_user_wallet/{user_id:int}")
@crud.db_session
def get_user_wallet(user_id):
    return crud.get_wallet_info(models.User[user_id].wallet)