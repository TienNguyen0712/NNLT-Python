# BaiTap1
from abc import ABC, abstractmethod

class Transaction:
    @abstractmethod
    def process(self):
        pass
    
    @abstractmethod
    def get_value(self):
        pass

class SaleTransaction(Transaction):
    def __init__(self, amount):
        self.amount = amount
    
    def process(self):
        print(f"Thực hiện nạp tiền {self.amount} VNĐ")
    
    def get_value(self):
        return self.amount
    

class RefundTransaction(Transaction):
    def __init__(self, amount):
        self.amount = amount
    
    def process(self):
        print(f"Thực hiện hoàn tiền {self.amount} VNĐ")
    
    def get_value(self):
        return -self.amount
    

class PromotionTransaction(SaleTransaction):
    def __init__(self, amount, discount_rate):
        super().__init__(amount)
        self.amount = amount
        self.discount = discount_rate
    
    def dis_pro(self):
        return self.amount - (self.amount * self.discount)
    
# BaiTap2
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.salary = base_salary
    
    def get_salary(self):
        return self.salary
class Manager:
    def __init__(self, bonus):
        self.bonus = bonus
    
    def get_bonus(self):
       return self.bonus

class Salesperson:
    def __init__(self, commission_rate):
        self.commission = commission_rate
    
    def caculate_commission(self, sale):
        return sale * self.commission
    
class SaleManager(Employee, Salesperson, Manager):
    def __init__(self, name, base_salary, commission_rate, bonus):
        Employee.__init__(self, name, base_salary)
        Salesperson.__init__(self, commission_rate)
        Manager.__init__(self, bonus)

    def total_income(self, sale):
        print(f"Tổng: {self.get_salary() + self.caculate_commission(sale) + self.get_bonus()}")

# BaiTap3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(func):
    """Decorator to log transaction actions."""
    def wrapper(*args, **kwargs):
        logging.info(f"Executing transaction: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Transaction {func.__name__} successful.")
            return result
        except Exception as e:
            logging.error(f"Transaction {func.__name__} failed: {e}")
            raise  # Re-raise the exception to be handled by the caller
    return wrapper

class Account:
    def __init__(self, balance = 0):
        self._balance = balance
    
    @log_action       
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền nạp không đủ")
        self._balance += amount

    @log_action    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Số dư không đủ")
        self._balance -= amount
    
    def get_balance(self):
        return self._balance
    
class TransactionManager(Account):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, account):
        self.accounts[account_id] = account

    def execute_transaction(self, account_id, action, amount):
        account = self.accounts.get(account_id)
        if not account:
            raise ValueError(f"Account {account_id} not found.")

        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError(f"Invalid action: {action}")