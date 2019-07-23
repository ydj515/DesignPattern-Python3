#-*- coding: utf-8 -*-

import abc

class Subject:
    """
    추상화된 변경 관심 대상 데이터
    """
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        """
        통보대상 추가. observer 추가
        """
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        """
        통보대상 제거. observer 제거
        """
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        """
        옵저버에게 변경을 통보
        """
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        """
        데이터 상태 return
        """
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        """
        데이터 상태 setter
        notify도 같이 해줌
        """
        self._subject_state = arg
        self._notify()


class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    """
    observer 구현
    """
    def update(self, arg):
        self._observer_state = arg


def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.attach(concrete_observer)

    subject.subject_state = 123 # notify도 같이 실행해줌
    print(subject._subject_state)
    
    print("===========================")

    subject.subject_state = 255 # notify도 같이 실행해줌
    print(subject._subject_state)


if __name__ == "__main__":
    main()