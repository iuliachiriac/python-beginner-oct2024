import csv
import json


class BankClient:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def notify(self):
        print(f"Notification sent to {self.email}.")


class BankAccount:
    def __init__(self, id_, owner: BankClient, overdraft):
        self.id = id_
        self.owner = owner
        self.overdraft = overdraft
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def load_clients_from_json(json_file):
    with open(json_file, "r") as f:
        return json.load(f)


def build_accounts_dict(clients_data):
    accounts_dict = {}
    for client_data in clients_data:
        client = BankClient(client_data["name"], client_data["email_address"])
        for account in client_data["bank_accounts"]:
            bank_account = BankAccount(account["id"], client, account["overdraft"])
            accounts_dict[bank_account.id] = bank_account
    return accounts_dict


def parse_transactions(csv_file, accounts_dict):
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip first row
        for account_id, transaction_type, amount in reader:
            account_id = int(account_id)
            amount = int(amount)
            bank_account = accounts_dict[account_id]
            if transaction_type == "debit":
                try:
                    bank_account.withdraw(amount)
                except ValueError as ex:
                    print(ex, bank_account.id, bank_account.owner)
            elif transaction_type == "credit":
                bank_account.deposit(amount)


def main():
    clients_data = load_clients_from_json("docs/clients.json")
    all_accounts = build_accounts_dict(clients_data)
    parse_transactions("docs/transactions.csv", all_accounts)

    for account in all_accounts.values():
        # print(account.id, account.balance, account.overdraft)
        if account.balance < 0 and -account.balance >= 0.7 * account.overdraft:
            account.owner.notify()


if __name__ == "__main__":
    main()