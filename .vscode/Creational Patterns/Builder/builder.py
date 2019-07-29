#-*- coding: utf-8 -*-

import abc

"""
복잡한 것을 만들 때는 전체를 한꺼번에 만들기보다는 작게 분리하여 만든 후 다시 합치는 것이 편리하다.
builder 패턴은 복잡한 인스턴스를 조립하여 만드는 구조로, 복합 객체를 생성할 때 객체를 생성하는 방법(과정)과 객체를 구현(표현)하는 방법을 분리한다.
따라서 이 패턴은 동일한 생성 절차에서 서로 다른 표현 결과를 만들 수 있다.
abstract method 패턴과 굉장히 유사한데 별도의 Director가 builder(추상클래스)를 갖고 builder를 통해서 세부적인 작업후 생성된 오브젝트를 리턴하는 패턴
복잡한 인스턴스 생성 및 세팅과정을 모두 Director에게 떠넘기고 Director는 내부적으로  builder를 갖고 이를 처리한다.
Director가 다양하게 구현된 builder를 갖을 수 있어서 동일한 Main클래스에서 builder만 다르게 세팅해줌으로 다양한 결과를 얻을 수 있다.
"""

class Director:
    """
    Builder 인터페이스를 사용하는 객체를 합성한다
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
    """
    Product 객체의 일부 요소들을 생성하기 위한 추상 인터페이스 제공
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Builder 클래스에 정의된 인터페이스를 구현하며, 제품의 부품들을 모아 빌더를 복합한다
    """

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class Product:
    """
    생성할 복합 객체를 표현
    """

    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product


if __name__ == "__main__":
    main()