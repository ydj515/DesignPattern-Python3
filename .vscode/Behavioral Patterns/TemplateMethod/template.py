#-*- coding: utf-8 -*-

import abc

class AbstractClass(metaclass=abc.ABCMeta):
    """
    템플릿 메소드를 정의하는 클래스
    primitive 메소드나 hook 메소드 정의
    """

    def template_method(self):
        self._primitive_operation_1()
        self._primitive_operation_2()

    @abc.abstractmethod
    def _primitive_operation_1(self):
        pass

    @abc.abstractmethod
    def _primitive_operation_2(self):
        pass


class ConcreteClass(AbstractClass):
    """
    물려받은 primitive 메소드나 hook 메소드를 구현하는 클래스
    """

    def _primitive_operation_1(self):
        pass

    def _primitive_operation_2(self):
        pass


def main():
    concrete_class = ConcreteClass()
    concrete_class.template_method()


if __name__ == "__main__":
    main()