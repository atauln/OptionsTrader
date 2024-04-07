from data import Account
import logging

class BaseModule:
    def __init__(self, name: str, description: str, account: Account):
        self.name = name
        self.description = description
        self.account = account

    def run(self) -> int:
        if not self.account:
            logging.error("Account not found")
            return 1
        if not self.account.a_id:
            logging.error("Account not initialized, has this module been registered?")
            return 1
        logging.info(f"Running module \"{self.name}\" [{self.description}]")
        return 0

    def details(self):
        return f"{self.name}: {self.description}"