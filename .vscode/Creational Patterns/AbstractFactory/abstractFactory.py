#-*- coding: utf-8 -*-

import abc

class AbstractFactory(metaclass=abc.ABCMeta):
    """
    실제 팩토리 클래스의 공통 인터페이스.
    각 제품의 부품을 생성하는 기능을 추상메소드로 정의
    """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    구체적인 팩토리 클래스로 AbstractFacotry 클래스의 추사 메소드를 override함으로써 구체적인 제품을 생성
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    구체적인 팩토리 클래스로 AbstractFacotry 클래스의 추사 메소드를 override함으로써 구체적인 제품을 생성
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    제품의 공통 인터페이스
    """

    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    구체적인 팩토리 클래스에서 생성되는 구체적인 제품
    """

    def interface_a(self):
        pass


class ConcreteProductA2(AbstractProductA):
    """
    구체적인 팩토리 클래스에서 생성되는 구체적인 제품
    """

    def interface_a(self):
        pass


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    제품의 공통 인터페이스
    """

    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    """
   구체적인 팩토리 클래스에서 생성되는 구체적인 제품
    """

    def interface_b(self):
        pass


class ConcreteProductB2(AbstractProductB):
    """
    구체적인 팩토리 클래스에서 생성되는 구체적인 제품
    """

    def interface_b(self):
        pass


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()


if __name__ == "__main__":
    main()