

class Hero:

    def __init__(self,name ,age, speed, hp):
        self.hero_name = name
        self.hero_age = age
        self.hero_pace = speed
        self.hero_hp = hp

    def greetings(self):
        return  f"You chose a very cool name!!\nFrom now on it's you '{self.hero_name}'"

    def increase_in_speed(self):
        self.hero_pace += 10
        return f"For such a cool name,\nthe system gives you +10 to speed '{self.hero_pace}'"

    def improving_health(self):
        self.hero_hp += 40
        return f"Because you are a warrior,\nthe system has given you +40 to your HP '{self.hero_hp}'."


player = Hero('KingArtur', 20,30, hp=None)
player_2 = Hero('KnightInArmor', 25, 20, 70)

print(player.greetings())
print(player.increase_in_speed())


print(player_2.greetings())
print(player_2.improving_health())




