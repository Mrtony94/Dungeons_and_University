"""

ALUMNOS que han realizado la practica
Antonio Andres Perez DNI: 47580369Q Titulacion: IST
Javier Zapatero Lera DNI: 54300753F Titulacion: IST
Hemos realizado el programa con implementacion de color (solo compatible con distribuciones UNIX o macOS)

"""

import getopt
import sys
import os

import game
from game import *

class UsageError(Exception):
    def __init__(self):
        super().__init__(f"{Game.bcolors.MONSTER}[ERROR]: python main [-f n] [-s n]")


    # --------------------------------------------------------------------------------------------- #
                                         # ARGUMENTOS DEF
    # --------------------------------------------------------------------------------------------- #

def parse_args():
    args, trash = getopt.getopt(sys.argv[1:], 'f:s:', ["file=", "stages="])     # version corta - y version larga --

    file = None
    stages = 1
    for o, v in args:
        if o in ('-f', '--file'):
            file = v
        elif o in ('-s', '--stages'):
            stages = v

    return file, stages


def check_args(file, stages):
    file_ok = True
    stages_ok = True

    if file is not None and (not(file.endswith(".txt") or file.endswith(".json")) or not os.path.isfile(file)):
        # comprobamos que el archivo es .txt o .json
        file_ok = False

    try:
        stages = int(stages)
        if stages < Game.MIN_STAGES or stages > Game.MAX_STAGES:    # comprobamos que los estados estan dentro del rango
            stages_ok = False
    except ValueError:
        stages_ok = False

    return file_ok, stages_ok


    # --------------------------------------------------------------------------------------------- #
                                               # MAIN
    # --------------------------------------------------------------------------------------------- #


try:
    file, stages = parse_args()
    file_ok, stages_ok = check_args(file, stages)
    if file_ok and stages_ok:
        game = Game(file, int(stages))
        game.play_game()
    else:
        if not stages_ok:
            print(f"{Game.bcolors.STAGE}The number of stages must be between 1 and 10.")
        if not file_ok:
            print(f"{Game.bcolors.RESET}The format of the chosen file is incorrect. You must provide a filename that ends "
                  "either with .txt .json. Finishing program")
except getopt.GetoptError:
    raise UsageError
except KeyboardInterrupt:
    pass

print(f"\nFinishing program...")
