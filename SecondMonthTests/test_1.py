class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        Hero.__init__(self, name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        MageHero.__init__(self, name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    bank_name = "Simba"  # атрибут класса

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance      # защищённый
        self.__password = password   # приватный

    def login(self, password):
        if password != self.__password:
            return print("Вы вошли в аккаунт!!")
        else:
            return print("Пароль не вернный!!")

    @property
    def full_info(self):
        return self.bank_name, self.hero, self._balance

    @classmethod
    def get_bank_name(cls):
        return f"Ваш банк: {cls.bank_name}"

    @staticmethod
    def bonus_for_level(lvl):
        if 10 <= lvl < 50:
            return f"Бонус за {lvl} уровень: 300 SOM"
        elif 50 <= lvl <= 100:
            return f"Бонус за {lvl} уровень: 500 SOM"
        else:
            return False

    def __str__(self):
        return f"Имя: {self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self,other):
        if isinstance(other, BankAccount):
            return "ОК"
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self._balance == other._balance
        return False



from abc import ABC, abstractmethod

class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):

    def send(self, text, phone):
        pass

    def send_otp(self):
        text = "<text>1234</text>"
        phone = "<phone>+996777123456</phone>"
        print(f"{text}<phone>{phone}</phone>")

class RUSsms(SmsService):
    def __init__(self, text):
        self.text = text

    def sms_send(self, data):
        print(f"<text>Код: {data['Код']}</text><phone>{data['phone']}</phone>")

    def send_otp(self):
        data = {
            "Код": "1234",
            "phone": "+7925"
        }
        self.sms_send(data)

# magic_hero = BankAccount("Mage",5000, 123456,"Merlin", 89, 150)
# warrior_hero = BankAccount("Warrior",3000,123456, "Conan",50,100 )
#
# print(magic_hero.action())


if __name__ == "__main__":
    magic_hero = MageHero("Merlin", 89, 150, 150)
    warrior_hero = WarriorHero("Conan", 50, 100, 80)
    magic_acc = BankAccount(magic_hero, 5000, 123456)
    warrior_acc = BankAccount(warrior_hero, 3000, 123456)
    print(warrior_hero.action())
    print(magic_acc)
    print(warrior_acc)
    print(BankAccount.get_bank_name())
    print(BankAccount.bonus_for_level(warrior_hero.lvl))
    kg_sms = KGSms()
    kg_sms.send_otp()