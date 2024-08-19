class Squad:
    def __init__(self, name, battle_cry, year):
        self.name = name
        self.battle_cry = battle_cry
        self.year = year
        self.score = 50
        self._score_total = 0
        self._blot_count = 0
        self._plif_count = 0
        self.decibelmeter = 0

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.name, self.battle_cry, self.year, self.score, self.score_total, self._blot_count, self._plif_count)

    @property
    def score_total(self):
        return self._score_total

    @property
    def count_blot(self):
        return self.blot_count

    @property
    def count_plif(self):
        return self.plif_count

    @property
    def battle_count(self):
        return self.score

    @score_total.setter
    def score_total(self, score):
        self._score_total += score

    def blot(self):
        self.score -= 5
        self._blot_count += 1

    def plif(self):
        self.score += 1
        self._plif_count += 1

    def grusht(self):
        self.score += 3