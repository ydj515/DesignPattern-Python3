#-*- coding: utf-8 -*-

import abc

class Robot(metaclass=abc.ABCMeta):
    """
    스트래티지 패턴을 이용하는 역할을 수행
    """
    
    @abc.abstractmethod
    def set_moving_strategy(self, moving_strategy):
        pass
    
    @abc.abstractmethod
    def set_attack_strategy(self, attack_strategy):
        pass


class Atom(Robot):

    def set_moving_strategy(self, moving_strategy):
        self._moving_strategy = moving_strategy
        self._moving_strategy.move()

    def set_attack_strategy(self, attack_strategy):
        self._attack_strategy = attack_strategy
        self._attack_strategy.attack()   


class TaekwonV(Robot):

    def set_moving_strategy(self, moving_strategy):
        self._moving_strategy = moving_strategy
        self._moving_strategy.move()

    def set_attack_strategy(self, attack_strategy):
        self._attack_strategy = attack_strategy
        self._attack_strategy.attack()  


class MovingStrategy(metaclass=abc.ABCMeta):
    """
    인터페이스나 추상 클래스로 외부에서 동일한 방식으로 알고리즘을 호출하는 방법을 명시
    """

    @abc.abstractmethod
    def move(self):
        pass


class WalkingStrategy(MovingStrategy):
    """
    스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
    """

    def move(self):
        print("I can Walk")


class FlyingStrategy(MovingStrategy):
    """
    스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
    """

    def move(self):
        print("I can fly")
        

class AttackStrategy(metaclass=abc.ABCMeta):
    """
    인터페이스나 추상 클래스로 외부에서 동일한 방식으로 알고리즘을 호출하는 방법을 명시
    """

    @abc.abstractmethod
    def attack(self):
        pass


class PunchAttackStrategy(AttackStrategy):
    """
    스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
    """

    def attack(self):
        print("I can attack punch")


class KickAttackStrategy(AttackStrategy):
    """
    스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
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