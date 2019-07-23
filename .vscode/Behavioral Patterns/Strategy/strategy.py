#-*- coding: utf-8 -*-

import abc


class Context:
    """
    스트래티지 패턴을 이용하는 역할을 수행
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):
    """
    인터페이스나 추상 클래스로 외부에서 동일한 방식으로 알고리즘을 호출하는 방법을 명시
    """

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):
    """
    스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
    """

    def algorithm_interface(self):
        pass


class ConcreteStrategyB(Strategy):
    """
    스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
    """

    def algorithm_interface(self):
        pass


def main():
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()


if __name__ == "__main__":
    main()