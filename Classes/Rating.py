from typing import Tuple

class Rating:
    def __init__(self, K = 20):
        self._K = K

    def calc_E(self, Ra: int, Rb: int) -> float:
        return 1 / (1 + 10 ** ((Rb - Ra) / 400))
    
    def calc_goal_index(self, goals: Tuple[int]) -> float:
        if goals[0] == goals[1] or (goals[0] - goals[1]) * -1 == 1:
            return 1
        
        if (goals[0] - goals[1]) * -1 == 2:
            return 3 / 2
        
        goal_difference = (goals[0] - goals[1]) * -1
        return (11 + goal_difference) / 8
    
    def calc_delta(self, old_rating: int, real_result: float, goals: Tuple[int], E: float) -> int:
        index_of_goals = self.calc_goal_index(goals)
        return int(self._K*index_of_goals*(real_result - E))
