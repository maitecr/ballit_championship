from Phase import *
from Squad import *
import random

class Championship:
    def __init__(self):
        self._squad_list = []
        self._phases_list = []

    def __str__(self):
        return '%s' % (self._squad_list)

    @property
    def squad_list(self):
        return self._squad_list

    @squad_list.setter
    def squad_list(self, item):
        self._squad_list.append(item)

    @property
    def phases_list(self):
        return self._phases_list

    @phases_list.setter
    def phases_list(self, item):
        self._phases_list.append(item)

    def get_squad_list_len(self):
        return len(self._squad_list)

    def register_squad(self):
        while True:
            print("Cadastre novo time")
            set_name = input('Nome do time: ')
            set_battle_cry = input('Grito de guerra: ')
            set_year = input('Ano de criação: ')

            self.squad_list = Squad(set_name, set_battle_cry, set_year)

            print('==================================================')

            get_out = input(print('Deseja sair? S/N: '))

            if get_out == 's' and self.get_squad_list_len() < 8:
                print('Insira no mínimo 8 times')

            if get_out == 's' and self.get_squad_list_len() >= 8:
                break

            if get_out == 's' and self.get_squad_list_len() % 2 != 0:
                print('Quantidade de times deve ser valor par')

            if self.get_squad_list_len() == 16:
                print('16 times cadastrados! Já podemos iniciar o campeonato')
                break

        return self.squad_list

    def start_competition(self):
        self.squad_list = self.register_squad()
        shuffled_squad_list = random.sample(self.squad_list, len(self.squad_list))
        phase = Phase(shuffled_squad_list)
        while True:
            selected_match = phase.start_phase()


