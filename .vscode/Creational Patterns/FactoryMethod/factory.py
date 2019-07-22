#-*- coding: utf-8 -*-

import abc

class Creator(metaclass=abc.ABCMeta):
    """
    팩토리 메소드를 갖는 클래스
    """

    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod # 추상화 된 메소드 -> Creator 클래스를 상속받은 클래스가 이 메소드를 구현하지 않으면 에러를 발생
    def _factory_method(self): # private
        pass

    def some_operation(self):
        self.product.interface()


class ConcreteCreator1(Creator):
    """
    팩토리 메소드를 구현하는 클래스.
    ConcreteProduct 객체 생성
    """

    def _factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
    팩토리 메소드를 구현하는 클래스.
    ConcreteProduct 객체 생성
    """

    def _factory_method(self):
        return ConcreteProduct2()


class Product(metaclass=abc.ABCMeta):
    """
    팩토리 메소드로 생성될 객체의 공통 인터페이스
    """

    @abc.abstractmethod # 추상화 된 메소드 -> Product 클래스를 상속받은 클래스가 이 메소드를 구현하지 않으면 에러를 발생
    def interface(self):
        pass


class ConcreteProduct1(Product):
    """
    구체적으로 객체가 생성되는 클래스
    """

    def interface(self):
        pass


class ConcreteProduct2(Product):
    """
    구체적으로 객체가 생성되는 클래스
    """
    def interface(self):
        pass