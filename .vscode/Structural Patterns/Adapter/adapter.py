#-*- coding: utf-8 -*-

"""
인터페이스 호환성을 위해 사용
클래스의 인터페이스를 다른 인터페이스로 변환할 수 있게 해주는 패턴
"""

import abc


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """

    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def request(self):
        pass


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def request(self):
        self._adaptee.specific_request()


class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self):
        pass


def main():
    adapter = Adapter()
    adapter.request()


if __name__ == "__main__":
    main()