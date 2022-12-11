from datetime import datetime
from pony.orm import *

db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    tg_ID = Required(int, unique=True)
    nick = Optional(str)
    create_date = Required(datetime, default=datetime.now())
    wallet = Required('Wallet')
    sended_transactions = Set('Transaction', reverse='sender')
    received_transactions = Set('Transaction', reverse='receiver')


class Transaction(db.Entity):
    id = PrimaryKey(int, auto=True)
    sender = Optional(User, reverse='sended_transactions')
    receiver = Optional(User, reverse='received_transactions')
    sender_wallet = Optional('Wallet', reverse='sended_transactions')
    receiver_wallet = Optional('Wallet', reverse='received_transactions')
    sender_address = Optional(str)
    receiver_address = Optional(str)
    amount_btc_with_fee = Required(float)
    amount_btc_without_fee = Required(float)
    fee = Required(float)
    date_of_transaction = Required(datetime, default=datetime.now())
    tx_hash = Required(str, unique=True)


class Wallet(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Optional(User)
    balance = Required(float, default="0.0")
    private_key = Required(str, unique=True)
    address = Required(str, unique=True)
    sended_transactions = Set(Transaction, reverse='sender_wallet')
    received_transactions = Set(Transaction, reverse='receiver_wallet')