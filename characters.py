"""

ALUMNOS que han realizado la práctica:
Antonio Andrés Pérez DNI: 47580369Q Titulacion: IST
Javier Zapatero Lera DNI: 54300753F Titulacion: IST
Hemos realizado el programa con implementación de color (solo compatible con distribuciones UNIX o macOS)

"""

import random

    # --------------------------------------------------------------------------------------------- #
                                 # CHARACTER CLASS (clase padre)
    # --------------------------------------------------------------------------------------------- #


class Character:
    def __init__(self, hp_max, dmg, hp):
        self.hp_max = hp_max
        self.dmg = dmg
        self.hp = hp

    def __str__(self):
        print(f"HP_MAX: {self.hp_max} HP: {self.hp} DMG: {self.dmg}")    # devolver información util para el juego

    def attack(self, enemy):
        dmg_attack = random.randint(1, self.dmg)
        enemy.decrease_hp(dmg_attack)
        return dmg_attack

    def increase_hp(self, c):
        self.hp += c
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def decrease_hp(self, n):
        self.hp -= n
        if self.hp <= 0:
            self.hp = 0

    def level_up(self):
        if self.hp > 0:
            self.increase_hp(0.25*self.hp_max)

    def display_attributes(self):
        print(f"{self.__class__.__name__}: Stats: {self.hp} HP and {self.dmg} DMG")

    # --------------------------------------------------------------------------------------------- #
                                # PLAYERS CLASS (clases hijas)
    # --------------------------------------------------------------------------------------------- #


class Bookworm(Character):
    HP_MAX = 25
    DMG = 9

    @staticmethod
    def print_info():   # Imprimir estadísticas del personaje (HP_MAX y DMG)
        print(f"BookWorm -> Stats: {Bookworm.HP_MAX} HP, {Bookworm.DMG} DMG")

    def __init__(self, hp=HP_MAX):
        super().__init__(Bookworm.HP_MAX, Bookworm.DMG, hp)  # super hace referencia al padre


class Worker(Character):
    HP_MAX = 40
    DMG = 10

    @staticmethod
    def print_info():
        print(f"Worker -> Stats: {Worker.HP_MAX} HP, {Worker.DMG} DMG")

    def __init__(self, hp=HP_MAX):
        super().__init__(Worker.HP_MAX, Worker.DMG, hp)


class Procrastinator(Character):
    HP_MAX = 30
    DMG = 6

    @staticmethod
    def print_info():
        print(f"Procrastinator -> Stats: {Procrastinator.HP_MAX} HP, {Procrastinator.DMG} DMG")

    def __init__(self, hp=HP_MAX):
        super().__init__(Procrastinator.HP_MAX, Procrastinator.DMG, hp)


class Whatsapper(Character):
    HP_MAX = 20
    DMG = 6

    @staticmethod
    def print_info():
        print(f"Whatsapper -> Stats: {Whatsapper.HP_MAX} HP, {Whatsapper.DMG} DMG")

    def __init__(self, hp=HP_MAX):
        super().__init__(Whatsapper.HP_MAX, Whatsapper.DMG, hp)


