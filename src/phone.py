from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0 and isinstance(number_of_sim, int):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __add__(self, other):
        if type(other) != self.__class__:
            return TypeError('Нельзя сложить эти объекты')
        if self.name != other.name:
            return TypeError('Имена должны совпадать')
        if self.price != other.price:
            return TypeError('Цена должна совпадать')
        return self.__class__(
            name=self.name,
            price=self.price,
            quantity=self.quantity + other.quantity,
            number_of_sim=self.number_of_sim
            )
