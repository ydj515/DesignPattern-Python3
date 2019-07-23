#-*- coding: utf-8 -*-

import abc

class Component(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):

    def operation(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):

    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):

    def operation(self):
        # ...
        self._component.operation()
        # ...


class ConcreteDecoratorB(Decorator):

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