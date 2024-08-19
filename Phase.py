import itertools
from Match import *

class Phase:
    def __init__(self, shuffled_squads):
        self.squads = shuffled_squads
        self.pairs = list(itertools.batched(shuffled_squads, 2))
        self.squad_len = len(self.squads)
        self.match_list = []

    def select_match(self):
        print("INICIAR CAMPEONATO")
        for i,pair in enumerate(self.pairs):
            print(f"=========== Escolher Partida {i + 1} ===========")
            print(f"Time A: {pair[0]}")
            print(f"Time B: {pair[1]}")

        select = input(print("Informe o número da partida a iniciar: "))
        selected_to_int = int(select)

        if select == str(selected_to_int):
            return self.pairs[selected_to_int - 1]

    def start_phase(self):
        choosen_match = self.select_match()
        match = Match(choosen_match)

        while True:
            if choosen_match in self.match_list:
                print("=============================================")
                print("A partida não pode ser disputada novamente")
                print("=============================================")
                break
            if choosen_match not in self.match_list:
                self.match_list.append(choosen_match)
                print("**************************************")
                print("PARTIDA INICIADA")
                print("**************************************")
                squad_results = match.play_match()
                print(squad_results)