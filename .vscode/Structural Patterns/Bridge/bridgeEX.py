#-*- coding: utf-8 -*-

import abc

class Display:
    """
    Abstraction
    기능 : 표시하다
    """

    def __init__(self, imp):
        self._imp = imp

    def myOpen(self):
        self._imp.raw_open()

    def myPrint(self):
        self._imp.raw_print()

    def myClose(self):
        self._imp.raw_close()

    def display(self):
        self.myOpen()
        self.myPrint()
        self.myClose()


class CountDisplay(Display):
    """
    기능 : 지정 횟수만큼 표시
    """
    def __init__(self, imp):
        super().__init__(imp)
    
    def multi_display(self, num):
        super().myOpen()
        for i in range(num):
            super().myPrint()
        super().myClose()


class DisplayImplementor():
    """
    Implementor
    구현 : 표시
    """

    @abc.abstractmethod
    def raw_open(self):
        pass
    
    @abc.abstractmethod
    def raw_print(self):
        pass
    
    @abc.abstractmethod
    def raw_close(self):
        pass


class StringDisplay(DisplayImplementor):
    """
    ConcreteImplementorA
    구현 : 문자열을 이용해 표시
    """

    def __init__(self, input_str):
        self._str = input_str
        self._width = len(input_str)

    @abc.abstractmethod
    def raw_open(self):
        self._print_line()
    
    @abc.abstractmethod
    def raw_print(self):
        # print(self._str)
        print("|" + self._str + "|")
    
    @abc.abstractmethod
    def raw_close(self):
        self._print_line()


    def _print_line(self):
        print("+",end="")
        for i in range(self._width):
            print("-",end="")
        print("+")


class ConcreteImplementorB(DisplayImplementor):
    """
    ConcreteImplementorB
    """

    def operation_imp(self):
        pass


def main():

    concrete_implementor_a = StringDisplay("hello, korea")
    d1 = Display(concrete_implementor_a)
    d1.display()
    print("========================")

    concrete_implementor_b = StringDisplay("Hello, World!")
    d2 = CountDisplay(concrete_implementor_b)
    d2.display()
    print("========================")

    concrete_implementor_c = StringDisplay("Hello, Universe!")
    d3 = CountDisplay(concrete_implementor_c)
    d3.display()
    print("========================")

    d3.multi_display(5)


if __name__ == "__main__":
    main()