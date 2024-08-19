import random
import time

class Match:
    def __init__(self, squads):
        self.squadA = squads[0]
        self.squadB = squads[1]
        self.finished = False

    def grusht_battle(self):
        start_time = time.time()
        while time.time() - start_time < 5:
            print(self.squadA.battle_cry)
            print(self.squadB.battle_cry)

    def call_debicelmeter(self):
        self.squadA.decibelmeter += random.uniform(1, 500)
        self.squadB.decibelmeter += random.uniform(1, 500)

        if self.squadA.decibelmeter > self.squadB.decibelmeter:
            return self.squadA
        else:
            return self.squadB

    def play_match(self):
        winner = ''
        loser = ''

        while True:
            print('TIME A')
            print(self.squadA.name)
            print(self.squadA.score)
            print('VS')
            print('TIME B')
            print(self.squadB.name)
            print(self.squadB.score)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

            print('Registrar um "blot" para o time A - Digite 1')
            print('Registrar um "plif" para o time A - Digite 2')
            print('Registrar um "blot" para o time B - Digite 3')
            print('Registrar um "pluf" para o time B - Digite 4')
            print('Encerrar a partida - Digite X')
            value = input('Informar ação: ')

            if value == "1":
                self.squadA.blot()

            if value == "2":
                self.squadB.plif()

            if value == "3":
                self.squadB.blot()

            if value == "4":
                self.squadB.plif()

            if self.squadA.score == 0:
                winner = self.squadB
                loser = self.squadA
                break

            if self.squadB.score == 0:
                winner = self.squadA
                loser = self.squadB
                break

            if value == "x" and self.squadA.score == self.squadB.score:
                print('Grusht!')
                self.grusht_battle()
                higher_cry = self.call_debicelmeter()
                higher_cry.grusht()
                print(f"HIGHEST CRY: {higher_cry}")

            if value == "x":
                if self.squadA.score > self.squadB.score:
                    self.squadB.score_total += self.squadB.score
                    self.squadA.score_total += self.squadA.score

                    winner = self.squadA
                    loser = self.squadB
                    self.finished = True
                    break
                else:
                    self.squadB.score_total += self.squadB.score
                    self.squadA.score_total += self.squadA.score

                    winner = self.squadB
                    loser = self.squadA
                    self.finished = True
                    break
        print("WINNER - LOSER")
        print(winner.name, loser.name)
        return [winner.name, loser.name]
