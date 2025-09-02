"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    
    if account_number not in accounts:
        accounts[account_number] = {"name": name, "balance": 0.0}
    else:
        return f"Account {account_number} already exist"
    
    accounts[account_number].update(kwargs)

    return f"{name}'s has been created successfully!!"


def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    if account_number in accounts:
        if amount >= 50 and amount <= 150000:
            accounts[account_number]["balance"] += amount
            return f"Deposited {amount} into {accounts[account_number]['name']}'s account successfully!!!"
        elif amount > 150000:
            return "Amount has exceed account limit"
        elif amount < 50:
            return "Amount must greater than 50"
        else:
            return "Invalid amount"

    else:
        return "Account does not exists"

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number in accounts:
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount
            return f"You have withdrawed ${amount} from {accounts[account_number]['name']}'s account."
        else:
            return "Insufficient Fund"
    else:
        return "Account not found!!!!"

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    pass
    if from_acc in accounts and to_acc in accounts:
        if amount >= 50 and amount <= 150000:
            if accounts[from_acc]["balance"] >= amount:
                accounts[from_acc]["balance"] -= amount
                accounts[to_acc]["balance"] += amount
                return f"Transfered {amount} from {accounts[from_acc]['name']}'s account to {accounts[to_acc]['name']}'s account successfully!!"
            else:
                return "Insufficient Fundz!!!.."
        else:
            return "Your limit is beteween 50 to 150000"
    else:
        return "Account does not exists"