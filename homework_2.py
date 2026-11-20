"""домашняя работа №2"""
import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


warrior = Warrior("Воин", 5, 100, 10, 80)
mage = Mage("Маг", 4, 80, 8, 100)
assassin = Assassin("Ассасин", 6, 90, 9, 90)


heroes = {
    "Warrior": warrior,
    "Mage": mage,
    "Assassin": assassin
}

print("Выберите героя:")
print("Warrior")
print("Mage")
print("Assassin")

choice = input("Ваш выбор: ")

if choice not in heroes:
    print("Такого героя нет!")
else:
    player = heroes[choice]
    enemy_name = random.choice(list(heroes.keys()))

    while enemy_name == choice:
        enemy_name = random.choice(list(heroes.keys()))

    enemy = heroes[enemy_name]

    print(f"\nВы выбрали: {choice}")
    print(f"Противник: {enemy_name}")

    player.attack()
    enemy.attack()

    if choice == enemy_name:
        print("Ничья!")
    elif (
        (choice == "Warrior" and enemy_name == "Assassin") or
        (choice == "Assassin" and enemy_name == "Mage") or
        (choice == "Mage" and enemy_name == "Warrior")
    ):
        print(f"{choice} победил!")
    else:
        print(f"{enemy_name} победил!")