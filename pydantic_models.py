from pydantic import BaseModel
from datetime import datetime
from typing import List


class User(BaseModel):
    id: int
    tg_ID:  int
    nick:   str = None
    create_date: datetime
    wallet: 'Wallet'
    sended_transactions: List['Transaction'] = None
    received_transactions:  List['Transaction'] = None


class Transaction(BaseModel):
    id: int
    sender: User = None
    receiver: User = None
    sender_wallet: 'Wallet' = None
    receiver_wallet: 'Wallet' = None
    sender_address: str
    receiver_address: str
    amount_btc_with_fee: float
    amount_btc_without_fee: float
    fee: float
    date_of_transaction: datetime
    tx_hash: str

class Wallet(BaseModel):
    id: int
    user: User
    balance: float = 0.0
    private_key: str
    address: str
    sended_transactions: List[Transaction] = []
    received_transactions: List[Transaction] = []


class User_to_update(BaseModel):
    id: int
    tg_ID:  int = None
    nick:   str = None
    create_date: datetime = None
    wallet: 'Wallet' = None

class User_to_create(BaseModel):
    tg_ID:  int = None
    nick:   str = None

class Create_Transaction(BaseModel):
    receiver_address: str
    amount_btc_without_fee: float


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Admin(BaseModel): # вместо User, так как он уже есть 
# а так же удаляем лишние свойства
    username: str


class UserInDB(Admin):
    hashed_password: str
    
User_to_update.update_forward_refs()