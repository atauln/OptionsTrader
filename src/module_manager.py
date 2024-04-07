from db import service_layer
from modules.base_module import BaseModule

modules: list[BaseModule] = []

def load_module(module: BaseModule):
    modules.append(module)
    account = service_layer.getAccountByName(module.account.name)
    a_id = None
    if account is None:
        a_id = service_layer.insertAccount(module.account)
    else:
        a_id = account.a_id
    module.account.a_id = a_id

def run_modules():
    for module in modules:
        print("\n************************************")
        module.run()