"""домашняя работа №1"""
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
        print(f"{self.name} отдыхает…")
        self.health += 1


hero1 = Hero("Алекс", 5, 100, 10)
hero2 = Hero("Макс", 3, 80, 7)

hero1.greet()
hero1.attack()
hero1.rest()

print("Здоровье:", hero1.health)
print("Сила:", hero1.strength)

print()

hero2.greet()
hero2.attack()
hero2.rest()

print("Здоровье:", hero2.health)
print("Сила:", hero2.strength)