#-*- coding: utf-8 -*-

import abc

class Invoker:
    """
    기능의 실행을 요청하는 호출자 클래스
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


class Command(metaclass=abc.ABCMeta):
    """
    실행될 기능에 대한 인터페이스.
    실행될 기능을 execute 메소드로 선언함
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    실제로 실행되는 기능을 구현.
    Command라는 인터페이스를 구현.
    """

    def execute(self):
        self._receiver.action()


class Receiver:
    """
    ConcreteCommand에서 execute 메소드를 구현할 때 필요한 클래스
    Concrete Command의 기능을 실행하기 위해 사용하는 수신자 클래스
    """

    def action(self):
        pass


def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.execute_commands()


if __name__ == "__main__":
    main()