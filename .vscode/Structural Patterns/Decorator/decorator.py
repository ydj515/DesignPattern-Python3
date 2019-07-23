#-*- coding: utf-8 -*-

import abc

class Component(metaclass=abc.ABCMeta):
    """
    기본 기능을 뜻하는 ConcreteComponent와 추가 기능을 뜻하는 Decorator의 공통 기능을 정의
    client는 Component를 통해 실제 객체를 사용
    """
    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    """
    실제 객체 구현
    """
    def operation(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    """
    많은 수가 존재하는 구체적인 Decorator의 공통 기능 제공
    """
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    """
    Decorator의 하위 클래스로 기본 기능에 추가되는 개별적인 기능
    """
    def operation(self):
        # ...
        self._component.operation()
        # ...


class ConcreteDecoratorB(Decorator):
    """
    Decorator의 하위 클래스로 기본 기능에 추가되는 개별적인 기능
    """
    def operation(self):
        # ...
        self._component.operation()
        # ...


def main():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()


if __name__ == "__main__":
    main()