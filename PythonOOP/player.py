class Player:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
    
    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    # Alternate syntax for getter and setter
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self) -> str:
        return f'Name: {self.name}, Lives: {self._lives}, Level: {self._level}, Score: {self._score}'
