#-*- coding: utf-8 -*-

import abc

class PizzaIngredientFactory(metaclass=abc.ABCMeta):
    """
    AbstractFactory
    """

    @abc.abstractmethod
    def createDough(self):
        pass

    @abc.abstractmethod
    def createSauce(self):
        pass

    @abc.abstractmethod
    def createCheese(self):
        pass

    @abc.abstractmethod
    def createPepperoni(self):
        pass

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """
    ConcreteFactory1
    """
    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return ReggianoCheese()

    def createPepperoni(self):
        return SlicedPepperoni()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """
    ConcreteFactory2
    """
    def createDough(self):
        return ThickCrispyDough()

    def createSauce(self):
        return TomatoSauce()

    def createCheese(self):
        return MozzaCheese()

    def createPepperoni(self):
        return TongPepperoni()

class Dough(metaclass=abc.ABCMeta):
    """
    AbstractProductA
    """
    @abc.abstractmethod
    def print_info(self):
        pass

class ThinCrustDough(Dough):
    """
    ConcreteProductA1
    """
    def print_info(self):
        print("ThinCrustDough")

class ThickCrispyDough(Dough):
    """
    ConcreteProductA2
    """
    def print_info(self):
        print("ThickCrispyDough")

class Sauce(metaclass=abc.ABCMeta):
    """
    AbstractProductB
    """
    @abc.abstractmethod
    def print_info(self):
        pass

class MarinaraSauce(Sauce):
    """
    ConcreteProductB1
    """
    def print_info(self):
        print("MarinaraSauce")

class TomatoSauce(Sauce):
    """
    ConcreteProductB2
    """
    def print_info(self):
        print("TomatoSauce")

class Cheese(metaclass=abc.ABCMeta):
    """
    AbstractProductC
    """
    @abc.abstractmethod
    def print_info(self):
        pass

class ReggianoCheese(Cheese):
    """
    ConcreteProductC1
    """
    def print_info(self):
        print("ReggianoCheese")

class MozzaCheese(Cheese):
    """
    ConcreteProductC2
    """
    def print_info(self):
        print("MozzaCheese")

class Pepperoni(metaclass=abc.ABCMeta):
    """
    AbstractProductD
    """
    @abc.abstractmethod
    def print_info(self):
        pass

class SlicedPepperoni(Pepperoni):
    """
    ConcreteProductD1
    """
    def print_info(self):
        print("SlicedPepperoni")

class TongPepperoni(Pepperoni):
    """
    ConcreteProductD2
    """
    def print_info(self):
        print("TongPepperoni")


class Pizza(metaclass=abc.ABCMeta):
    """
    product
    bake, cut, box는 동일 로직이라 abstract로 구현하지 않았따
    """

    @abc.abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("피자 굽기")

    def cut(self):
        print("피자 자르기")

    def box(self):
        print("피자 포장")

class CheesePizza(Pizza):
    """
    ConcreteProductA1
    """

    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()

class PeporoniPizza(Pizza):
    """
    ConcreteProductA2
    """

    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
    

class PizzaStore(metaclass=abc.ABCMeta):
    """
    Creator
    """

    @abc.abstractmethod
    def _createPizza(self, pizzaType: str):
        pass

    def orderPizza(self, pizzaType):

        pizza = self._createPizza(pizzaType)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

class NYPizzaStore(PizzaStore):

    """
    ConcreteCreator1
    """
    def _createPizza(self, pizzaType: str):
        ingredientFactory = NYPizzaIngredientFactory()

        print("====NY factory 정보출력====")
        ingredientFactory.createCheese().print_info()
        ingredientFactory.createDough().print_info()
        ingredientFactory.createPepperoni().print_info()
        ingredientFactory.createSauce().print_info()
        print("===========================")

        if pizzaType == 'Peporoni':
            pizza = PeporoniPizza(ingredientFactory)
        elif pizzaType == 'Cheese':
            pizza = CheesePizza(ingredientFactory)
        else:
            print("wrong")
        
        return pizza

class ChicagoPizzaStore(PizzaStore):

    """
    ConcreteCreator2
    """
    def _createPizza(self, pizzaType: str):
        ingredientFactory = ChicagoPizzaIngredientFactory()

        print("====Chicago factory 정보출력====")
        ingredientFactory.createCheese().print_info()
        ingredientFactory.createDough().print_info()
        ingredientFactory.createPepperoni().print_info()
        ingredientFactory.createSauce().print_info()
        print("================================")

        if pizzaType == 'Peporoni':
            pizza = PeporoniPizza(ingredientFactory)
        elif pizzaType == 'Cheese':
            pizza = CheesePizza(ingredientFactory)
        else:
            print("wrong")
        
        return pizza


def main():
    store = NYPizzaStore()
    store.orderPizza('Peporoni')
    print("\n")
    store2 = ChicagoPizzaStore()
    store2.orderPizza('Cheese')

if __name__ == "__main__":
    main()
