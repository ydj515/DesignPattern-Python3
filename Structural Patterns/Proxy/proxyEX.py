#-*- coding: utf-8 -*-

import abc

class SubjectInterface(metaclass=abc.ABCMeta):
    """
    subject
    """
    @abc.abstractmethod
    def add(self, a, b):
        pass

    @abc.abstractmethod
    def sub(self, a, b):
        pass


class Proxy(SubjectInterface):
    """
    proxy
    add와 sub는 request method
    """

    def __init__(self, realSubject):
        self._realSubject = realSubject

    def add(self, a, b):
        """
        request
        """
        return self._realSubject.add(a, b)

    def sub(self, a, b):
        """
        request
        """
        return self._realSubject.sub(a, b)


class RealSubject(SubjectInterface):
    """
    realsubject
    """

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


def main():
    realSubject = RealSubject()
    proxy = Proxy(realSubject)

    print(proxy.add(100, 25)) # 125
    print(proxy.sub(100, 25)) # 75


if __name__ == "__main__":
    main()