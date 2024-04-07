# this is a router for account related operations
from fastapi import APIRouter, HTTPException
from datetime import datetime
from db import application_layer, service_layer
from data import *
from routers.router_utils import *

router = APIRouter(prefix="/accounts")

@router.get("")
async def get_accounts():
    accounts = service_layer.getAccounts()
    account_dicts = [account.__dict__ for account in accounts]
    for account in account_dicts:
        account['cur_balance'] = application_layer.calculateAccountBalance(account['a_id'])
    return format_response(account_dicts)

@router.get("/{a_id}")
async def get_account_by_id(a_id: int):
    account = service_layer.getAccountById(a_id)
    if account:
        account_dict = account.__dict__
        account_dict['cur_balance'] = application_layer.calculateAccountBalance(a_id)
        return format_response(account_dict)
    else:
        raise HTTPException(status_code=404, detail="Account not found")
    
@router.get("/{a_id}/balance")
async def get_account_balance(a_id: int):
    balance = application_layer.calculateAccountBalance(a_id)
    return format_response({'balance': balance})

@router.get("/{a_id}/balance_at", summary="Format for timestamp: YYYY-MM-DD")
async def get_account_balance_at(a_id: int, timestamp: str):
    timestamp = datetime.strptime(timestamp, "%Y-%m-%d")
    balance = application_layer.calculateAccountBalance(a_id, timestamp)
    return format_response({'balance': balance})

@router.get("/{a_id}/transactions")
async def get_account_transactions(a_id: int):
    transactions = service_layer.getTransactionsByAccountId(a_id)
    transaction_dicts = [transaction.__dict__ for transaction in transactions]
    for transaction in transaction_dicts:
        asset = service_layer.getAssetById(transaction['asset_id'])
        transaction['ticker'] = asset.symbol
        transaction['asset_type'] = asset.type
    return format_response(transaction_dicts)

@router.post("")
async def create_account(name: str, init_balance: float):
    a_id = service_layer.insertAccount(Account(0, name, init_balance))
    return format_response({'a_id': a_id})

@router.delete("/{a_id}")
async def delete_account(a_id: int):
    service_layer.deleteAccount(a_id)
    return format_response({'message': 'Account deleted'})