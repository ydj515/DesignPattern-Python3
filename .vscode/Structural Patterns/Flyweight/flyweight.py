

"""
동일한 것을 공유해서 (메모리)낭비를 없애기
객체를 가볍게 하기
"""

import abc


class FlyweightFactory:
    """
    플라이급 객체를 생성하고 관리하며, 플라이급 객체가 제대로 공유되도록 보장
    사용자가 플라이급 객체를 요청하면 FlyweightFactory객체는 이미 존재하는 인스턴스를 제공하거나 생성
    관리는 Hashmap을 사용하여 객체들의 pool을 만들어 사용
    보통 싱글톤으로 만듬
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):
    """
    Flyweight가 받아들일 수 있고, 부가적 상태에서 동작해야 하는 인터페이스를 선언
    """

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Flyweight인터페이스를 구현하고 내부적으로 갖고 있어야 하는 본질적 상태에 대한 저장소를 의미
    ConcreteFlyweight객체는 공유할 수 있어야 함
    """

    def operation(self, extrinsic_state):
        pass


def main():
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("key")
    concrete_flyweight.operation(None)


if __name__ == "__main__":
    main()