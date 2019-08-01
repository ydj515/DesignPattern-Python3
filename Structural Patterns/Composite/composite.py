#-*- coding: utf-8 -*-

import abc

class Component(metaclass=abc.ABCMeta):
    """
    구체적인 부분
    Leaf 클래스와 전체에 해당하는 Composite 클래스에 공통 인터페이스 정의
    """

    @abc.abstractmethod
    def operation(self):
        pass


class Composite(Component):
    """
    전체 클래스로 여러 개의 Component를 갖도록 정의
    여러 개의 Leaf, Component 객체를 부분으로 가질 수 있다.
    """

    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class Leaf(Component):
    """
    구체적인 부분 클래스로 Composite 객체의 부품으로 설정
    """

    def operation(self):
        pass


def main():
    leaf = Leaf()
    composite = Composite()
    composite.add(leaf)
    composite.operation()


if __name__ == "__main__":
    main()