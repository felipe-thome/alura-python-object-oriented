from functools import total_ordering


@total_ordering
class Account:

    def __init__(self, number, holder, balance=0.0, limit=1000.0):
        self._number = number
        self._holder = holder
        self._balance = balance
        self._limit = limit

    def __str__(self):
        return f'A conta {self.number} possui um saldo de: {self.balance} reais'

    def __eq__(self, other):
        return self.bank_code() == other.bank_code()

    def __lt__(self, other):
        return self.number < other.number

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_code_list():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @property
    def number(self):
        return self._number

    @property
    def holder(self):
        return self._holder

    @property
    def balance(self):
        return self._balance

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value

    def statement(self):
        print("Account Balance: {}".format(self.balance))

    def deposit(self, amount):
        self._balance += amount
        self.statement()

    def _can_withdraw(self, withdraw_amount):
        available_amount = self.balance + self.limit
        return withdraw_amount <= available_amount

    def withdraw(self, amount):
        if self._can_withdraw(amount):
            self._balance -= amount
            print("Your account balance is now: {}".format(self.balance))
        else:
            print("The amount ({}) exceeds your limit of {}".format(amount, self.limit))

    def transfer(self, destination, amount):
        self.withdraw(amount)
        destination.deposit(amount)
