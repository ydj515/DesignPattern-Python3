#-*- coding: utf-8 -*-

import abc

class Duck(metaclass=abc.ABCMeta):
    """
    Target
    """
    @abc.abstractmethod
    def quack(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck):
    """
    Target 을 구현한 class
    """
    def quack(self):
        print("Quack")

    def fly(self):
        print("Fly fly fly!")


# And this is our new interace that all turkeys 
# will need to extend:
class Turkey(metaclass=abc.ABCMeta):
    """
    Target
    """

    @abc.abstractmethod
    def gobble(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass

# This is a concrete class that extends Turkey
class WildTurkey(Turkey):
    """
    Target을 구현한 class
    """

    def gobble(self):
        print("Gobble gobble..")

    def fly(self):
        print("Flying for a short distance")

class TurkeyAdapter(Duck):
    """
    Adapter
    """

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        self.turkey.fly()

class TestDuck():
    """
    test를 위한 class method
    """
    @classmethod
    def testDuck(cls, duck: Duck):
        duck.quack()
        duck.fly()

def main():

    duck = MallardDuck()
    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)

    print("============Turkey============")
    turkey.gobble()
    turkey.fly()

    print("=============Duck=============")
    TestDuck.testDuck(duck)

    print("=======Turkey Adapter=========")
    TestDuck.testDuck(turkeyAdapter)

if __name__ == "__main__":
    main()