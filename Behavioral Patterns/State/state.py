#-*- coding: utf-8 -*-

import abc


class Context:
    """
    State를 이용하는 역할을 수행
    현재 시스템의 상태를 나타내는 상태 변수(state)와 실제 시스템의 상태를 구성하는 여러 가지 변수가 있다.
    또한 각 상태 클래스에서 상태 변경을 요청해 상태를 바꿀 수 있도록 하는 메소드(set_state)가 제공됨.
    Context 요소를 구현한 클래스의 request 메소드는 실제 행위를 실행하는 대신 해당 상태 객체에 행위 실행을 위임.
    """

    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()


class State(metaclass=abc.ABCMeta):
    """
    시스템의 모든 상태에 공통의 인터페이스를 제공.
    이 인터페이스를 실체화한 어떤 상태 클래스도 기존 상태클래스를 대신해 교체해서 사용할 수 있음
    """

    @abc.abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    """
    state를 실체화한 클래스
    Context 객체가 요청한 작업을 자신의 방식으로 실제 실행함.
    대부분의 경우 다음 상태를 결정해 상태 변경을 Context 객체에 요청하는 역할도 수행
    """

    def handle(self):
        pass


class ConcreteStateB(State):
    """
    state를 실체화한 클래스
    Context 객체가 요청한 작업을 자신의 방식으로 실제 실행함.
    대부분의 경우 다음 상태를 결정해 상태 변경을 Context 객체에 요청하는 역할도 수행
    """

    def handle(self):
        pass


def main():
    concrete_state_a = ConcreteStateA()
    context = Context(concrete_state_a)
    context.request()


if __name__ == "__main__":
    main()