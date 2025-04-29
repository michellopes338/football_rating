class Time:
    def __init__(self, name: str, rating=1000) -> None:
        self._name = name
        self._rating = rating

    @property
    def rating(self) -> int:
        return self._rating
    
    @property
    def name(self) -> str:
        return self._name

    @rating.setter
    def rating(self, new_rating: int) -> None:
        print(f'O rating de  {self._name} foi atualizado de {self._rating} para {new_rating}')
        self._rating = int(new_rating)

    def __repr__(self) -> str:
        return f'{self._name},{self._rating}'
    
    def __eq__(self, value) -> bool:
        if isinstance(value, Time):
            return self._rating == value.rating
        
        elif isinstance(value, str):
            return self._name == value
        
        else:
            NotImplementedError
    
    def __lt__(self, value) -> bool:
        return self.rating < value.rating
    
    def __le__(self, value) -> bool:
        return self.rating <= value.rating

    def __gt__(self, value) -> bool:
        return self.rating > value.rating
    
    def __ge__(self, value) -> bool:
        return self.rating >= value.rating
