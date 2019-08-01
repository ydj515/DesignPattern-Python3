#-*- coding: utf-8 -*-

import abc

class Button:
    """
    Invoker
    """

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        self._command.execute()
    

class Command(metaclass=abc.ABCMeta):
    """
    Command
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class LampOffCommand(Command):
    """
    ConcreteCommand1
    """

    def execute(self):
        self._receiver.turnOff()


class LampOnCommand(Command):
    """
    ConcreteCommand2
    """

    def execute(self):
        self._receiver.turnOn()


class Lamp:
    """
    Receiver
    """

    def turnOn(self):
        print("lamp turn on")

    def turnOff(self):
        print("lamp turn off")

    def action(self):
        pass


def main():
    button = Button()
    lamp = Lamp()

    offCommand = LampOffCommand(lamp) # 램프를 끄는 커맨드를 설정
    onCommand = LampOnCommand(lamp) # 램프를 키는 커맨드를 설정

    button.set_command(onCommand) # on 커맨드를 설정
    button.execute_command()

    print("=================")
    
    button.set_command(offCommand) # off 커맨드를 설정
    button.execute_command()

if __name__ == "__main__":
    main()