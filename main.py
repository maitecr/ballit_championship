from Championship import *
from Phase import *
import random

championship = Championship()
#championship.start_competition()

squad_list = championship.register_squad()

shuffled_squad_list = random.sample(squad_list, len(squad_list))

phase = Phase(shuffled_squad_list)

while True:
    selected_match = phase.start_phase()
