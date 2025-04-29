from .Times import Time
from .Rating import Rating
from typing import Tuple

class Partida:
    def __init__(self, timeA: Time, timeB: Time, S: float, goals: Tuple[int]):
        self._timeA = timeA
        self._timeB = timeB
        self._goals = goals
        self._S = S
        self._rating = Rating(30)

    def atribute_new_rating(self):
        E = self._rating.calc_E(self._timeA.rating, self._timeB.rating)
        
        rating_diference = self._rating.calc_delta(self._timeA._rating, self._S, self._goals, E)

        self._timeA.rating += rating_diference
        self._timeB.rating -= rating_diference