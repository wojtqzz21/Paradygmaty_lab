from abc import ABC, abstractmethod

class Samochod:
    def __init__(self, marka, model, rok):
        self.__marka = marka # prywatny
        self._model = model # chroniony
        self.rok = rok # publiczny


    def wypisz(self):
        return f"{self.marka} {self.model} {self.rok}"

class Pojazd(Samocod):
    def __init__(self, marka, model, rok, a):
        super().__init__(marka, model, rok)
        self.a = a

class Zwierze(ABC):
    @abstractmethod
    def dzwiek(self):
        pass

class Kot(Zwierze):
    def dzwiek(self):
        return "Miau"

class Pies(Zwierze):
    def dzwiek(self):
        return "Hau"
