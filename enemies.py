import random

class Enemy:
    def __init__(self, hp, dmg, stage):    # debemos conocer el daño, la vida maxima y la vida actual
        self.hp = hp
        self.dmg = dmg
        self.stage = stage
    # Devolver el nombre de su tipo(clase)

    def __str__(self):
        print(f"HP: {self.hp} DMG: {self.dmg}")
        #  informacion util para el juego, daño que ha echo o lo que queda de vida por cada jugador

    def attack(self, character):
        dmg_attack = random.randint(1, self.dmg)
        character.decrease_hp(dmg_attack)
        return dmg_attack

    def decrease_hp(self, n):
        self.hp -= n
        if self.hp <= 0:
            self.hp = 0
            # Como podemos saber cual es el enemigo que murió
        else:
            print(f"{self.__class__.__name__} ...")
        return self.hp  # ???

    def display_attributes(self):
        print(f"{self.__class__.__name__}: Stats: {self.hp}HP and {self.dmg}DMG")


class PartialExam(Enemy):
    HP_MAX = 20
    DMG = 6

    def __init__(self, stage, hp=HP_MAX):
        super().__init__(hp, PartialExam.DMG, stage)


class FinalExam(Enemy):
    HP_MAX = 40
    DMG = 12

    def __init__(self, stage, hp=HP_MAX):
        super().__init__(hp, FinalExam.DMG, stage)


class TheoricalClass(Enemy):
    HP_MAX = 8
    DMG = 4

    def __init__(self, stage, hp=HP_MAX):
        super().__init__(hp, TheoricalClass.DMG, stage)

    def attack(self, character):
        dmg_attack = random.randint(1, self.DMG) + self.stage
        character.decrease_hp(dmg_attack)
        return dmg_attack


class Teacher(Enemy):
    HP_MAX = 15
    DMG = 7

    def __init__(self, stage, hp=HP_MAX):
        super().__init__(hp, Teacher.DMG, stage)

    def attack(self, character):
        dmg_attack = random.randint(1, self.DMG)
        if dmg_attack == 7:
            dmg_attack = 14
        character.decrease_hp(dmg_attack)
        return dmg_attack
