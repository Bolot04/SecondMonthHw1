# import random
# import string
#
#
#
# class BankAccount:
#     def __init__(self, name, balance, password):
#         self.name = name                 # открытый
#         self._balance = balance          # защищённый
#         self.__password = password       # приватный
#
#     def deposit(self,amount ,password):
#         if self.__password != password:
#             return "Неверный пароль!"
#         self._balance += amount
#         return self._balance
#
#
#     def withdraw(self,amount , password):
#         if self.__password == password:
#             amount = self._balance
#             amount -= 100
#             return f"Ваш новый баланс: {self._balance}"
#         else:
#             return "Неверный пароль"
#
#     def change_password(self,old_password, new_password):
#         if old_password != self.__password:
#             return "Пароль изменен"
#         self.__password = new_password
#         return "Пароль изменен"
#
#     def get_balance(self, password):
#         if self.__password == password:
#             return f"Ваш баланс {self._balance}"
#         elif self.__password != password:
#             return f"Ваш баланс {self._balance}"
#         else:
#             return "Неверный пароль!"
#
#     def reset_pin(self, password):
#         if  password != self.__password:
#             return "Неверный пароль!"
#         new_pin = self.__generate_pin()
#         self.__password = new_pin
#         return f"Ваш новый PIN:{new_pin}"
#
#     def __generate_pin(self):
#         return ''.join(str(random.randint(0,9))for _ in range(4))
#
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

    def send(self, recipient):
        return f"Email sent to {recipient}"

class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, recipient):
        return f"SMS sent to {recipient}"

class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, recipient):
        return f"Push sento to {recipient}"

if __name__ == "__main__":
    email = EmailSender()
    sms = SmsSender()
    push = PushSender()

    print(email.send("Привет", "john@mail.ru"))
    print(email.get_service())

    print(sms.send("+996778228900"))
    print(sms.get_service())

    print(push.send("John"))
    print(push.get_service())


