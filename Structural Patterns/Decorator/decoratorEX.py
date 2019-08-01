#-*- coding: utf-8 -*-

import abc

class Pizza(metaclass=abc.ABCMeta):
    """
    component
    """

    @abc.abstractmethod
    def info(self):
        pass

    @abc.abstractmethod
    def cost(self):
        pass


class PlainPizza(Pizza):
    """
    ConcreteComponent
    """

    def info(self):
        print("Plain Pizza : 1000")

    def cost(self):
        return 1000


class PizzaDecorator(Pizza, metaclass=abc.ABCMeta):
    """
    Decorator
    """

    def __init__(self, pizza):
        self._pizza = pizza

    @abc.abstractmethod
    def info(self):
        self._pizza.info()

    @abc.abstractmethod
    def cost(self):
       return self._pizza.cost()


class Mushroom(PizzaDecorator):
    """
    ConcreteDecoratorA
    """
    
    def info(self):
        super().info()
        print("Mushroom : 500")

    def cost(self):
        return 500 + super().cost()


class Onion(PizzaDecorator):
    """
    ConcreteDecoratorB
    """

    def info(self):
        self._pizza.info()
        print("Onion : 800")

    def cost(self):
        return 800 + self._pizza.cost()


def main():
    plainPizza = PlainPizza()
    plainPizza.info()
    print(plainPizza.cost())
    print("=========================")

    mushroomPizza = Mushroom(plainPizza)
    mushroomPizza.info()
    print(mushroomPizza.cost())
    print("=========================")

    onionPizza = Onion(plainPizza)
    onionPizza.info()
    print(onionPizza.cost())
    print("=========================")

    onionAndMushroomPizza = Onion(mushroomPizza)
    onionAndMushroomPizza.info()
    print(onionAndMushroomPizza.cost())


if __name__ == "__main__":
    main()