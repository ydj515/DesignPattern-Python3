#-*- coding: utf-8 -*-

"""
구현부에서 추상층을 분리하여 각자 독립적으로 변형이 가능하고 확장이 가능하도록 함
즉 기능과 구현에 대해서 두 개를 별도의 클래스로 구현
"""

import abc


class Abstraction: # 기능
    """
    기능 계층의 최상위 클래스.
    구현 부분에 해당하는 클래스를 인스턴스를 가지고 해당 인스턴스를 통해 구현부분의 메서드를 호출
    """

    def __init__(self, imp):
        self._imp = imp

    def operation(self):
        self._imp.operation_imp()


class Implementor(metaclass=abc.ABCMeta): # 기능
    """
    Abstraction의 기능을 구현하기 위한 인터페이스 정의
    """

    @abc.abstractmethod
    def operation_imp(self):
        pass


class ConcreteImplementorA(Implementor): # 구현
    """
    실제 기능을 구현
    """

    def operation_imp(self):
        pass


class ConcreteImplementorB(Implementor): # 구현
    """
    실제 기능을 구현
    """

    def operation_imp(self):
        pass


def main():
    concrete_implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(concrete_implementor_a)
    abstraction.operation()


if __name__ == "__main__":
    main()