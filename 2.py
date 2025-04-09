class BankAccount:
    def __init__(self, initial_balance=500):
        self._balance = initial_balance
        self._total_withdrawn = 0

    @property
    def balance(self):
        return self._balance

    @property
    def total_withdrawn(self):
        return self._total_withdrawn

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Сумма депозита должна быть положительной")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self._balance >= amount:
            self._balance -= amount
            self._total_withdrawn += amount
        else:
            raise ValueError("Недостаточно средств на счете")

    def __str__(self):
        return f"Баланс: {self._balance}, Всего снято: {self._total_withdrawn}"



if __name__ == "__main__":
    bank = BankAccount()
    bank.deposit(500)
    print(bank.balance)

    try:
        bank.withdraw(300)
        print(bank.balance)
        print(bank.total_withdrawn)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print(bank)