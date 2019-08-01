#-*- coding: utf-8 -*-

"""
최소 지식 원칙(Principle of Least Knowledge = Law of Demeter)을 사용하는 패턴
퍼사드는 소프트웨어 라이브러리를 쉽게 이해할 수 있게 해주며, 사용할 수 있게 해줌
퍼사드는 공통적인 작업에 대해 간편한 메소드들을 제공
퍼사드는 라이브러리를 사용하는 코드들을 좀 더 읽기 쉽게 해줌
퍼사드는 라이브러리 바깥쪽의 코드가 라이브러리의 안쪽 코드에 의존하는 일을 감소시켜줌
(대부분이 바깥쪽의 코드가 퍼사드를 이용하기 때문에 시스템을 개발하는데 있어 유연성이 향상)

복잡한 객체를 쉽고 단순한 인터페이스로 이용하고 싶을 경우에 사용
"""

class Facade:

    def __init__(self):
        self._subsystem_1 = Subsystem1()
        self._subsystem_2 = Subsystem2()

    def operation(self):
        self._subsystem_1.operation1()
        self._subsystem_1.operation2()
        self._subsystem_2.operation1()
        self._subsystem_2.operation2()


class Subsystem1:

    def operation1(self):
        pass

    def operation2(self):
        pass


class Subsystem2:

    def operation1(self):
        pass

    def operation2(self):
        pass


def main():
    facade = Facade()
    facade.operation()

if __name__ == "__main__":
    main()