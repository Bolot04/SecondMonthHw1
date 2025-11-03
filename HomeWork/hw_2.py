class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health      # очки здоровья

    def info(self) -> str:
        return f"{self.name}, {self.age} лет, здоровье {self.health}"

    def use_ability(self) -> str:
        """Переопределяется в наследниках"""
        return f"{self.name} использует базовую способность."

class Flyable:
    def __init__(self, fly):
        self.fly = fly

    def flyable(self):
        return 'летает.'

class Swimmable:
    def __init__(self, swimm):
        self.swimm = swimm

    def swimmable(self):
        return 'умеет плавать.'

class Invisible:
    def __init__(self, invis):
        self.invis = invis

    def invisible(self):
        return 'становится невидемым.'


class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(animal.info())

    def perform_show(self):
        for animal in self.animals:
            print(animal.use_ability())


class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name: str, age: int, health: int):
        Animal.__init__(self, name, age, health)
        Flyable.__init__(self, True)
        Swimmable.__init__(self, True)

    def use_ability(self) -> str:
        """Переопределяется в наследниках"""
        return f"{self.name} использует базовую способность. {self.flyable()}{self.swimmable()}."


    def swimmable(self):
        return 'умеет плавать.'

class Bat(Animal, Flyable, Invisible):
    def __init__(self, name: str, age: int, health: int):
        Animal.__init__(self, name, age, health)
        Flyable.__init__(self, True)
        Invisible.__init__(self, True)

    def use_ability(self) -> str:
        """Переопределяется в наследниках"""
        return f"{self.name} использует базовую способность. {self.flyable()}{self.invisible()}"

class Frog(Animal, Swimmable):
    def __init__(self, name: str, age: int, health: int):
        Animal.__init__(self, name, age, health)
        Swimmable.__init__(self, True)

    def use_ability(self) -> str:
        """Переопределяется в наследниках"""
        return f"{self.name} использует базовую способность. {self.swimmable()}"

class Phoenix(Animal, Flyable, Invisible):
    def __init__(self, name: str, age: int, health: int):
        Animal.__init__(self, name, age, health)
        Flyable.__init__(self, True)
        Invisible.__init__(self, True)

    def use_ability(self) -> str:
        """Переопределяется в наследниках"""
        return f"{self.name} использует базовую способность. {self.flyable()}{self.invisible()}"

if __name__ == "__main__":
   zoo = Zoo()

   duck = Duck("Дональд", 3, 80)
   bat = Bat("Бэтти", 5, 60)
   frog = Frog("Кермит", 2, 50)
   phoenix = Phoenix("Феникс", 100, 200)

   for animal in (duck, bat, frog, phoenix):
       zoo.add_animal(animal)

   print("=== Информация о животных ===")
   zoo.show_all()

   print("\n=== Шоу суперспособностей ===")
   zoo.perform_show()

   print("\nMRO для Duck:", Duck.__mro__)
   print("MRO для Phoenix:", Phoenix.__mro__)








