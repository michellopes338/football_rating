from typing import Tuple

class Parser:
    def result(self, result: str) -> float:
        timeA, timeB = result.split('x')

        if timeA == timeB:
            return 0.5
        
        if int(timeA) > int(timeB):
            return 1
        
        return 0
    
    def goals(self, result: str) -> Tuple[int]:
        return tuple(map(lambda x: int(x), result.split('x')))
