import random
import string



class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name                 # открытый
        self._balance = balance          # защищённый
        self.__password = password       # приватный

    def deposit(self,amount):
        # if self.__password != password:
        #     return "Неверный пароль!"
        self._balance += amount
        return self._balance


    def withdraw(self,amount , password):
        if self.__password == password:
            amount = self._balance
            amount -= 100
            return f"Ваш новый баланс: {self._balance}"
        else:
            return "Неверный пароль"

    def change_password(self,old_password, new_password):
        if old_password != self.__password:
            return "Пароль изменен"
        self.__password = new_password
        return "Пароль изменен"

    def get_balance(self, password):
        if self.__password == password:
            return f"Ваш баланс {self._balance}"
        elif self.__password != password:
            return f"Ваш баланс {self._balance}"
        else:
            return "Неверный пароль!"

    def reset_pin(self, password):
        if  password != self.__password:
            return "Неверный пароль!"
        new_pin = self.__generate_pin()
        self.__password = new_pin
        return f"Ваш новый PIN:{new_pin}"

    def __generate_pin(self):
        return ''.join(str(random.randint(0,9))for _ in range(4))

# john = BankAccount("John", 100, "123qwerty")
# print(john.deposit(50, "123qwerty"))
# print(john.withdraw(200, "123qwerty"))
# print(john.get_balance("123qwerty"))
# print(john.change_password("wrong", "new"))
# new_pin = john.reset_pin("123qwerty")
# print(new_pin)
# print(john.get_balance(new_pin))
#

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    def __init__(self, service):
        self._service = service

    @abstractmethod
    def send(self,recipient):
        pass

    def get_service(self):
        return f"Сервис: {self._service}"

class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    @property
    def service(self):
        return self._service

    def send(self, message, recipient):
        return f"Email sent {message} to {recipient}"

class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    @property
    def service(self):
        return self._service

    def send(self, recipient):
        return f"SMS sent to {recipient}"

class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, recipient):
        return f"Push sento to {recipient}"

# if __name__ == "__main__":
#     email = EmailSender()
#     sms = SmsSender()
#     push = PushSender()
#
#     print(email.send("Привет", "john@mail.ru"))
#     print(email.get_service())
#
#     print(sms.send("+996778228900"))
#     print(sms.get_service())
#
#     print(push.send("John"))
#     print(push.get_service())


class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        if isinstance(self.account.get_balance(password), (int, float)):
            self.notifier.send(f"Успешный вход: {self.username}", "system")
            return True
        else:
            return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        if self.account.get_balance(password) is None:
            print("Ошибка: неверный пароль.")
            return False

        if self.account.withdraw(amount, password) is None:
            print("Ошибка при списании средств.")
            return False

        recipient_account._balance += amount

        self.notifier.send(f"Перевод {amount} отправлен", "system")
        self.notifier.send(f"Получено {amount} от {self.username}", "system")




if __name__ == "__main__":
    print("=== Тест BankAccount ===")
    acc = BankAccount("John", 200, "secret")
    print(acc.deposit(50))       # 250
    print(acc.withdraw(100, "secret"))  # 150
    print(acc.get_balance("secret"))    # 150
    acc.change_password("wrong", "newpass")  # Старый пароль неверный
    acc.change_password("secret", "newpass")  # Пароль изменён
    acc._balance = 5832
    print(acc._balance)
    print(acc.get_balance("newpass"))

    print("\n=== Тест NotificationSender ===")
    email = EmailSender()
    print(email.send("Test", "test@mail.ru"))
    print(email.service)
    sms = SmsSender()
    print(sms.service)

    print("\n=== Тест UserAuth ===")
    john = BankAccount("John", 150, "secret")
    alice = BankAccount("Alice", 50, "pass123")
    notifier = SmsSender()
    auth = UserAuth("john_doe", john, notifier)

    auth.login("secret")
    auth.transfer(70, "secret", alice)

    print(f"John balance: {john._balance}")
    print(f"Alice balance: {alice._balance}")
