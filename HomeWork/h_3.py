import random
import string



class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name                 # открытый
        self._balance = balance          # защищённый
        self.__password = password       # приватный

    def deposit(self,amount ,password):
        if self.__password == password:
            amount = self._balance
            amount += 100
            return f"Ваш баланс увеличен c {self._balance} на {amount}"
        else:
            return "Неверный пароль!"


    def withdraw(self,amount , password):
        if self.__password == password:
            amount = self._balance
            amount -= 100
            return f"Ваш новый баланс: {self._balance}"
        else:
            return "Неверный пароль"

    def change_password(self,old_password, new_password):
        if old_password == self.__password:
            self.__password == new_password
            return "Пароль изменен"
        else:
            return "Старый пароль неверный"

    def get_balance(self, password):
        if self.__password == password:
            return f"Ваш баланс {self._balance}"
        else:
            return "Неверный пароль!"

    def __generate_pin(self):
            first_digit = random.choice(string.digits[1:])
            other_digits = ''.join(random.choice(string.digits) for _ in range(3))
            return first_digit + other_digits

    def reset_pin(self, password):
        if self.__password == password:
            new_pin = self.__generate_pin()
            self.__password == new_pin
            return f"Ваш новый PIN:{new_pin}"
        else:
            return "Неверный пароль"

    def show_balance(self, password):
        if self.__password == password:
            return f"Ваш баланс: {self._balance}₽"
        else:
            return "Неверный пароль"


john = BankAccount("John", 100, "123456")
print(john.deposit(100, "123456"))
print(john.withdraw(100, "123456"))
print(john.change_password("123456", "654321"))
print(john.reset_pin("123456"))
print(john.get_balanc)


