class User:
    def __init__(self):
        self.ranking = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.progress = 0

    def inc_progress(self, x):
        diff = self.ranking.index(x) - self.ranking.index(self.rank)

        if self.rank != 8:
            if diff >= -1:
                if diff == -1:
                    self.progress += 1
                elif diff == 0:
                    self.progress += 3
                else:
                    self.progress += 10 * diff ** 2

            while self.progress >= 100:
                self.progress -= 100
                self.rank = self.ranking[self.ranking.index(self.rank) + 1]
                if self.rank == 8:
                    self.progress = 0
