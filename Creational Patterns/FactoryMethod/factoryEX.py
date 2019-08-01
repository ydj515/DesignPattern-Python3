#-*- coding: utf-8 -*-

import abc

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

        if pizzaType == 'Peporoni':
            pizza = NYStylePeporoniPizza()
        elif pizzaType == 'Cheese':
            pizza = NYStyleCheesePizza()
        else:
            print("No matching pizza found in the NY pizza store...")
        
        return pizza

class ChicagoPizzaStore(PizzaStore):

    """
    ConcreteCreator2
    """
    def _createPizza(self, pizzaType: str):
        if pizzaType == 'Peporoni':
            pizza = ChicagoStylePeporonikPizza()
        elif pizzaType == 'Cheese':
            pizza = ChicagoStyleCheesePizza()
        else:
            print("No matching pizza found in the Chicago pizza store...")
        
        return pizza



class Pizza(metaclass=abc.ABCMeta):
    """
    Product
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


class NYStyleCheesePizza(Pizza):
    """
    ConcreteProduct1
    """
    def prepare(self):
        print("뉴욕 치즈 피자 준비중")

class ChicagoStyleCheesePizza(Pizza):
    """
    ConcreteProduct2
    """
    def prepare(self):
        print("시카고 치즈 피자 준비중")

class NYStylePeporoniPizza(Pizza):
    """
    ConcreteProduct3
    """
    def prepare(self):
        print("뉴욕 페퍼로니 피자 준비중")

class ChicagoStylePeporonikPizza(Pizza):
    """
    ConcreteProduct4
    """
    def prepare(self):
        print("시카고 페퍼로니 피자 준비중")



def main():
    nyPizzaStore = NYPizzaStore()
    chPizzaStore = ChicagoPizzaStore()

    nyPizzaStore.orderPizza('Peporoni')
    print("\n")
    chPizzaStore.orderPizza('Cheese')

if __name__ == "__main__":
    main()







