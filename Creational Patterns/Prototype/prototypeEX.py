#-*- coding: utf-8 -*-

import copy, sys

class Point:
    __slot__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)

def main():

    # Point 클래스 객체를 생성자를 활용해 생성 (정적생성)
    p1 = Point(1,2)
    print(p1)
    print("========================")

    # eval() 을 사용해 클래스 이름을 매개변수로 전달 (동적생성)
    p2 = eval("{}({}, {})".format("Point", 2, 4))
    print(p2)
    print("========================")

    # gettattr() 을 사용해 클래스 이름을 매개변수로 전달 (동적생성)
    p3 = getattr(sys.modules[__name__], "Point")(3, 6)
    print(p3)
    print("========================")

    # globals() 을 사용해 클래스 이름을 매개변수로 전달 (동적생성) - point3 과 동일한 방식
    p4 = globals()["Point"](4, 8)
    print(p4)
    print("========================")

    # point5는 클래스 객체와 필요한 인자를 받는 제네릭 함수를 통해 생성
    p5 = make_object(Point, 5, 10)
    print(p5)
    print("========================")

    # 고전적인 프로토타입 접근법을 생성
    # 먼저 copy.deepcopy()를 사용해 기존 객체를 복제
    # 복제된 객체를 초기화하거나 애트리뷰트를 재설정
    p6 = copy.deepcopy(p5)
    p6.x = 6
    p6.y = 12
    print(p6)
    print("========================")

    # 파이썬은 어떤 객체의 클래스 객체 (__class__)에 접근할 수 있다
    # 기존 객체를 복제한 다음 복제본을 수정하는 대신 클래스 객체를 활용해 바로 새로운 객체를 만들 수 있다.
    p7 = p1.__class__(7, 14)
    print(p7)
    print("========================")

if __name__ == "__main__":
    main()