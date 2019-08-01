#-*- coding: utf-8 -*-

import abc

"""
어떤 객체에 대한 접근을 제어하기 위한 용도로 대리인이나 대변인에 해당하는 객체를 제공하는 패턴

원격 프록시(다른 JVM에 들어있는 객체의 대변인에 해당하는 로컬 객체)를 써서 원격 객체에 대한 접근을 제어할 수 있음
가상 프록시(생서앟는데 많은 비용이 드는 객체를 대신하는 역할을 맡음)를 써서 생성하기 힘든 자원에 대한 접근을 제어할 수 있음
보호 프록시를 써서 접근 권한이 필요한 자원에 대한 접근을 제어할 수 있음

cf) 데코레이터 패턴은 새로운 행동을 추가하기 위한 용도이지, 프록시는 어떤 class에 대한 접근을 제어하기 위한 용도
"""


class Subject(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Subject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ...
        self._real_subject.request()
        # ...


class RealSubject(Subject):
    """
    실제 작업을 처리하는 객체
    proxy는 이 객체에 대한 접근을 제어
    """

    def request(self):
        pass


def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()


if __name__ == "__main__":
    main()