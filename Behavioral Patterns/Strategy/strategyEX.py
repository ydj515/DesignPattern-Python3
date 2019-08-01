#-*- coding: utf-8 -*-

import abc

class Robot(metaclass=abc.ABCMeta):
    """
    context
    """
    
    @abc.abstractmethod
    def set_moving_strategy(self, moving_strategy):
        pass
    
    @abc.abstractmethod
    def set_attack_strategy(self, attack_strategy):
        pass


class Atom(Robot):
    """
    context 구현
    """

    def set_moving_strategy(self, moving_strategy):
        self._moving_strategy = moving_strategy
        self._moving_strategy.move()

    def set_attack_strategy(self, attack_strategy):
        self._attack_strategy = attack_strategy
        self._attack_strategy.attack()   


class TaekwonV(Robot):
    """
    context 구현
    """

    def set_moving_strategy(self, moving_strategy):
        self._moving_strategy = moving_strategy
        self._moving_strategy.move()

    def set_attack_strategy(self, attack_strategy):
        self._attack_strategy = attack_strategy
        self._attack_strategy.attack()  


class MovingStrategy(metaclass=abc.ABCMeta):
    """
    StrategyA
    """

    @abc.abstractmethod
    def move(self):
        pass


class WalkingStrategy(MovingStrategy):
    """
    ConcreteStrategyA1
    """

    def move(self):
        print("I can Walk")


class FlyingStrategy(MovingStrategy):
    """
    ConcreteStrategyA2
    """

    def move(self):
        print("I can fly")
        

class AttackStrategy(metaclass=abc.ABCMeta):
    """
    StrategyB
    """

    @abc.abstractmethod
    def attack(self):
        pass


class PunchAttackStrategy(AttackStrategy):
    """
    ConcreteStrategyB1
    """

    def attack(self):
        print("I can attack punch")


class KickAttackStrategy(AttackStrategy):
    """
    ConcreteStrategyB2
    """

    def attack(self):
        print("I can attack kick")


def main():
    flying_strategy = FlyingStrategy()
    moving_strategy = WalkingStrategy()

    punch_attack_strategy = PunchAttackStrategy()
    kick_attack_strategy = KickAttackStrategy()

    atom = Atom()
    atom.set_moving_strategy(flying_strategy)
    atom.set_attack_strategy(punch_attack_strategy)

    print("==============================")

    taekwonV = TaekwonV()
    taekwonV.set_moving_strategy(moving_strategy)
    taekwonV.set_attack_strategy(kick_attack_strategy)

if __name__ == "__main__":
    main()