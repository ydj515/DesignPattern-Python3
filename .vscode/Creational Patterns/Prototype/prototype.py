#-*- coding: utf-8 -*-

import copy

"""
동일한 객체를 여러 번 생성해야 하는 비용을 줄이기 위해 고안된 패턴
객체에 의해 생성될 객체의 타입이 결정
새로운 객체를 생성하기 위해 clone(복제)을 이용

"""

class Prototype:
    """
    Example class to be copied.
    """

    pass


def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)


if __name__ == "__main__":
    main()