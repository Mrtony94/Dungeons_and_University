"""ALUMNOS que han realizado la práctica:Antonio Andrés Pérez DNI: 47580369Q Titulación: ISTJavier Zapatero Lera DNI: 54300753F Titulación: ISTHemos realizado el programa con implementación de color (solo compatible con distribuciones UNIX o macOS)"""from characters import *from enemies import *class bcolors:    CHARACTER = '\033[92m'  # GREEN    STAGE = '\033[93m'  # YELLOW    MONSTER = '\033[91m'  # RED    WON = '\033[33m'  # NARANJA    RESET = '\033[0m'  # RESET COLORclass Game:    PLAYERS = 2    ENEMIES_BY_STAGE = 3    MIN_STAGES = 1    MAX_STAGES = 10    FINALEXAM_LEVEL = 3    AVAILABLE_CHARACTERS = [Bookworm, Worker, Procrastinator, Whatsapper]    AVAILABLE_ENEMIES = [PartialExam, FinalExam, TheoricalClass, Teacher]    @staticmethod    def print_available_characters():        print(f"{bcolors.CHARACTER}************      AVAILABLE CHARACTERS      ************")        for index, character_class in enumerate(Game.AVAILABLE_CHARACTERS):            print(f"{index + 1}.- ", end="")            character_class.print_info()        print(f"********************************************************\n")    def __init__(self, file, stages):        self.file = file        self.stages = stages        self.current_stage = 1        self.players_list = []        self.enemies_list = []        self.enemies_turn = False        self.player_turn = 0  # index at players_list        self.end_game = False    # --------------------------------------------------------------------------------------------- #    # PRINT DEF    # --------------------------------------------------------------------------------------------- #    def print_stage(self):        print(f"{bcolors.STAGE}\n      ***********************\n"              f"      *       STAGE {self.current_stage}       *\n"              f"      ***********************\n")    def print_characters_selection(self):        print(f"{bcolors.CHARACTER}\n***************PLAYERS*******************")        for character in self.players_list:            character.display_attributes()        print(f"*****************************************")    def print_enemies(self):        print(f"{bcolors.MONSTER}     ---- CURRENT MONSTER ----")        print(f"+++++++++++++++++++++++++++++++++++++++++")        for enemy in self.enemies_list:            enemy.display_attributes()        print(f"+++++++++++++++++++++++++++++++++++++++++")        print(f"               .             ")        print(f"               .             ")        print(f"               .             ")        print(f"               .             ")    # --------------------------------------------------------------------------------------------- #    # CHARACTER DEF    # --------------------------------------------------------------------------------------------- #    def characters_selection(self):        for player_number in range(1, Game.PLAYERS + 1):            valid_character_selection = False            while not valid_character_selection:                try:                    characters_selection = int(                        input(f"{bcolors.CHARACTER}Player {player_number}, {bcolors.RESET}Please, choose a character "                              f"(1-{len(Game.AVAILABLE_CHARACTERS)}): "))                    if 1 <= characters_selection <= len(Game.AVAILABLE_CHARACTERS):                        self.players_list.append(Game.AVAILABLE_CHARACTERS[characters_selection - 1]())                    else:                        raise ValueError                except ValueError:                    print(f"Incorrect choice. Choice must be between (1-{len(Game.AVAILABLE_CHARACTERS)}).")                else:                    valid_character_selection = True    def play_characters_turn(self):        print(f"{bcolors.CHARACTER}\n     ----------------------\n"              "     -    PLAYERS TURN    -\n"              "     ----------------------\n")        for index, player in enumerate(self.players_list):            if self.player_turn == index:                correct = False                while not correct:                    to_do = input(                        f"{bcolors.CHARACTER}The {player.__class__.__name__} (Player {index + 1}). "                        f"{bcolors.RESET}What are you going to do?: ")                    if to_do == "a":                        self.enemies_random_attack(player)                        correct = True                    elif to_do == "s":                        self.save_file()                        correct = True                    else:                        print("Incorrect choice must write a, s")                    self.change_turn()                    if len(self.enemies_list) == 0:                        break    # --------------------------------------------------------------------------------------------- #    # ENEMIES DEF    # --------------------------------------------------------------------------------------------- #    def enemies_generate(self):        for _ in range(Game.ENEMIES_BY_STAGE):            valid_enemy = False            while not valid_enemy:                enemy_class = random.choice(Game.AVAILABLE_ENEMIES)                if enemy_class != FinalExam or (                        enemy_class == FinalExam and self.current_stage >= Game.FINALEXAM_LEVEL):                    self.enemies_list.append(enemy_class(self.current_stage))                    valid_enemy = True    def enemies_random_attack(self, character):        enemy = random.choice(self.enemies_list)        dmg_attack = character.attack(enemy)  # El jugador ataca al enemigo        if enemy.hp == 0:            self.enemies_list.remove(enemy)            print(                f"{bcolors.CHARACTER}The {character.__class__.__name__} (Player {self.player_turn + 1}) "                f"{bcolors.RESET}did {dmg_attack} damage to {bcolors.MONSTER}{enemy.__class__.__name__}."                f" {enemy.__class__.__name__} {bcolors.RESET}dead ")        else:            print(                f"{bcolors.CHARACTER}The {character.__class__.__name__} (Player {self.player_turn + 1}) "                f"{bcolors.RESET}did {dmg_attack} damage to {bcolors.MONSTER}{enemy.__class__.__name__}."                f" {enemy.__class__.__name__} {bcolors.RESET}has {enemy.hp} hp left ")    def play_enemies_turn(self):        print(f"{bcolors.MONSTER}\n     -----------------------\n"              "     -    MONSTERS TURN    -\n"              "     -----------------------\n")        for enemy in self.enemies_list:            player = random.choice(self.players_list)            dmg_attack = enemy.attack(player)            if player.hp > 0:                print(                    f"{bcolors.MONSTER}The {enemy.__class__.__name__} {bcolors.RESET}did {dmg_attack}DMG to "                    f"{bcolors.CHARACTER}{player.__class__.__name__} (Player {self.player_turn + 1})."                    f" {player.__class__.__name__} {bcolors.RESET} has {player.hp} hp left")            else:                print(                    f"{bcolors.MONSTER}The {enemy.__class__.__name__} {bcolors.RESET}did {dmg_attack}DMG to "                    f"{bcolors.CHARACTER}{player.__class__.__name__} (Player {self.player_turn + 1})."                    f" {player.__class__.__name__} {bcolors.RESET}left the game")                self.players_list.remove(player)            if len(self.players_list) == 0:                self.end_game = True                break    # --------------------------------------------------------------------------------------------- #    # PLAY GAME DEF    # --------------------------------------------------------------------------------------------- #    def change_turn(self):        if self.player_turn == 0 and len(self.enemies_list) > 0:  # turno 1            if len(self.players_list) == Game.PLAYERS:                self.player_turn = 1        else:  # turno 2            self.player_turn = 0    def play_level(self):        if self.file is None:            self.enemies_generate()        self.print_stage()        self.print_characters_selection()        self.print_enemies()        finish = False        while not finish:            if not self.enemies_turn:                self.play_characters_turn()                if len(self.enemies_list) == 0:                    finish = True                else:                    self.enemies_turn = True            else:                self.play_enemies_turn()                if len(self.players_list) == 0:                    finish = True                    print("Game Finished")                    self.end_game = True                else:                    self.enemies_turn = False    def play_game(self):        if self.file is None:            print(                f"\nA game with {bcolors.STAGE}{self.stages} stage "                f"{bcolors.RESET}will be set up for {self.PLAYERS} players.\n ")            Game.print_available_characters()            self.characters_selection()            self.print_characters_selection()        else:            self.load_file()        while not self.end_game and self.current_stage <= self.stages:            self.play_level()            self.current_stage += 1            for player in self.players_list:                player.level_up()        if len(self.players_list) == 0:            print("\n All characters have been defeated. Try again.")        else:            print(f"{bcolors.WON}\nAll the stages have been cleared. You won the game!{bcolors.RESET}")    # --------------------------------------------------------------------------------------------- #    # FILE DEF    # --------------------------------------------------------------------------------------------- #    def save_file(self):        global player_info        global enemy_info        import json        correct = False        file = input("Where do you want the save the game (the file name must end with .txt or .json): ")        while not correct:            if file == "cancel":                print("The game was not saved.")                correct = True            elif file.endswith(".txt") or file.endswith(".json"):                game_info = {'stages': self.stages, 'current_stage': self.current_stage,                             'player_turn': self.player_turn}                players_info = []                enemies_info = []                for player in self.players_list:                    player_info = {'class': player.__class__.__name__, 'hp': player.hp}                    players_info.append(player_info)                game_info['players_list'] = players_info                for enemy in self.enemies_list:                    enemy_info = {'class': enemy.__class__.__name__, 'hp': enemy.hp}                    enemies_info.append(enemy_info)                game_info['enemies_list'] = enemies_info                with open(file, 'w') as f:                    f.write(json.dumps(game_info))                correct = True                print("The game has been saved!!\n")            else:                file = input(                    "The format of the file name is incorrect (the file name must end with .txt or .json). Try again: ")    def load_file(self):        global enemy_info        global player_info        import json        with open(self.file) as f:            str_data = f.read()        game_info = json.loads(str_data)        print("A game has been loaded...")        self.stages = game_info['stages']        self.current_stage = game_info['current_stage']        self.player_turn = game_info['player_turn']        players_info = game_info['players_list']        enemies_info = game_info['enemies_list']        for player_info in players_info:            if player_info['class'] == Bookworm.__name__:                self.players_list.append(Bookworm(player_info['hp']))            elif player_info['class'] == Worker.__name__:                self.players_list.append(Worker(player_info['hp']))            elif player_info['class'] == Whatsapper.__name__:                self.players_list.append(Whatsapper(player_info['hp']))            elif player_info['class'] == Procrastinator.__name__:                self.players_list.append(Procrastinator(player_info['hp']))        for enemy_info in enemies_info:            if enemy_info['class'] == PartialExam.__name__:                self.enemies_list.append(PartialExam(enemy_info['hp']))            elif enemy_info['class'] == FinalExam.__name__:                self.enemies_list.append(FinalExam(enemy_info['hp']))            elif enemy_info['class'] == TheoricalClass.__name__:                self.enemies_list.append(TheoricalClass(enemy_info['hp']))            elif enemy_info['class'] == Teacher.__name__:                self.enemies_list.append(Teacher(enemy_info['hp']))