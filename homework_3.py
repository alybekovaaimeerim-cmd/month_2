from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1
        print(f"Здоровье: {self.__health}")

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")


class Mage(Hero):
    def attack(self):
        print("Маг использует магию")


class Saitama(Hero):
    def attack(self):
        print("Сайтама наносит один сокрушительный удар!")


warrior = Warrior("Воин", 5, 100, 10)
mage = Mage("Маг", 4, 80, 8)
saitama = Saitama("Сайтама", 100, 1000, 999)


warrior.greet()
warrior.attack()
warrior.rest()

print()

mage.greet()
mage.attack()
mage.rest()

print()

saitama.greet()
saitama.attack()
saitama.rest()