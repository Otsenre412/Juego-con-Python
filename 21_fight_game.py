""" 
juego del demonio
"""
from colorama import init, Fore, Back, Style
import requests
import msvcrt
import random
init()

class Player:
    def __init__(self, player_id, name, gender, power, lives, gems=0):
        self.player_id = player_id
        self.name = name
        self.gender = gender
        self.power = power
        self.lives = lives
        self.gems = gems
    def __str__(self):
        return self.name

class FightGame:
    def __init__(self, auhtor, default_lives, default_power):
        self.auhtor = auhtor
        self.last_player_id = 0
        self.default_lives = default_lives
        self.default_power = default_power
        self.players = []

    def run(self):
        print(Fore.CYAN + """
        ______  _         _      _     _____                         
        |  ___|(_)       | |    | |   |  __ \                        
        | |_    _   __ _ | |__  | |_  | |  \/  __ _  _ __ ___    ___ 
        |  _|  | | / _` || '_ \ | __| | | __  / _` || '_ ` _ \  / _ \
        | |    | || (_| || | | || |_  | |_\ \| (_| || | | | | ||  __/
        \_|    |_| \__, ||_| |_| \__|  \____/ \__,_||_| |_| |_| \___|
                    __/ |                                            
                    |___/  by {}""".format(self.auhtor))
        print(Fore.WHITE)

        self.__get_players()
        self.__menu()
        #self.__status()

        while True: 
            option = msvcrt.getch()
            #print(option)
            if option == b'\x1b': # esc
                break
            elif option == b'0':
                self.__menu()
            elif option == b'1':
                self.__status()
            elif option == b'2':
                self.__fight()
            elif option == b'3':
                self.add_player()

    def __menu(self):
        print('\nAyuda:\n')
        print('0. Mostar ayuda')
        print('1. Status')
        print('2. Luchar')
        print('3. Añadir jugador')
        print('Esc. Salir\n')
    
    def __status(self):
        print('----------------------------------------------------------------------------')
        print(Fore.WHITE + 'Id'.ljust(5) 
        + ' | ' + 'Nombre'.ljust(22) 
        + ' | ' + 'Gender'.ljust(10) 
        + ' | ' + 'Vidas'.ljust(7) 
        + ' | ' + 'Poder'.ljust(7) 
        + ' | ' + 'Gems'.ljust(7))
        print('----------------------------------------------------------------------------')

        players_sorted = sorted(self.players, key=lambda x: x.power, reverse=True)
        players_sorted = sorted(players_sorted, key=lambda x: x.lives, reverse=True)

        for p in players_sorted:
            color = Fore.RED if p.lives <= 0 else Fore.WHITE
            print('{} | {} | {} | {} | {} | {}'.format(
                str(p.player_id).ljust(5),
                p.name.ljust(22), 
                p.gender.ljust(10), 
                str(p.lives).ljust(7),      # str para convertir un entero en string y poder usar el ljust sin errores
                str(p.power).ljust(7), 
                str(p.gems).ljust(7)
                ))
        print(Fore.WHITE + '----------------------------------------------------------------------------')

    def __fight(self):

        """ lo mismo que la linea de abajo:
        current_players = []
        for x in self.players:
            if x.lives > 0:
                current_players.appends(x)
        """

        #comprensive list de python:

        current_players = [x for x in self.players if x.lives > 0]

        # hay más de un jugador?

        if len(current_players) < 2:
            print(Fore.RED + 'No hay suficientes jugadores' + Fore.WHITE)
            return

        fighters = random.sample(current_players, k=2)

        player1 = fighters[0]
        player2 = fighters[1]

        damage = random.randint(1, 6)

        player2.power -= damage
        print(Fore.CYAN + '==> {} ha zurrado a {}'.format(player1, player2))

        if player2.power <= 0: # ha perdido una vidas
            player2.lives -= 1
            player2.power = self.default_power if player2.lives > 0 else 0

            if player2.lives > 0: 
                print(Fore.YELLOW + '{} ha perdido una vida (Le quedan {} pa palmar)'.format(player2, player2.lives))

            else: # ha muerto
                print(Fore.RED + '{} ha muerto por desgracia, o no'. format(player2))
                if len(current_players) == 2:
                     print(Fore.LIGHTYELLOW_EX + '{} HA GANADO EL JUEGO Y ES EL/LA PUTO/A AMO/A'.format(player1))
                return

            player1.gems += 1
            print(Fore.LIGHTGREEN_EX + '{} te ha tangado una gema (tiene {})'. format(player1, player1.gems) + Fore.WHITE)

            if player1.gems == 2:
                player1.lives += 1
                player1.gems = 0
                print(Fore.MAGENTA + 'Ha ganado 1 vida'.format(player1))

        # comprobar si alguien ha ganado el juego, o lo que es lo mismo
        # si solo hay un jugador con vida

           #  if player2.lives == 0:


    def __get_players(self):
        print('Obteniendo jugadores desde la api de Star Wars...')
        response = requests.get('https://swapi.co/api/people')
        people = response.json()['results']

        for person in people:
            self.last_player_id +=1
            player = Player(
                self.last_player_id,
                person['name'],
                person['gender'],
                self.default_power,
                self.default_lives
            )

            self.players.append(player)

    def add_player(self):
        name = ''
        while len(name) < 4:
            name = input('\nEscribe el nombre del jugador: ')

        gender= ''
        while len(gender) < 4:
            gender = input('\nIntroduce tu sexo (male/female): ')

        self.last_player_id +=1
        player = Player(
                self.last_player_id,
                name,
                gender,
                self.default_power,
                self.default_lives
            )

        self.players.append(player)

        print(Fore.YELLOW + '{} se ha añadido a la lista de jugadores'.format(player))

        print('lista de jugadores preparada')

FightGame('Ernesto', 3, 10).run()