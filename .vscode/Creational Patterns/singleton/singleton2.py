#-*- coding: utf-8 -*-

# 모든 객체가 같은 상태를 공유해서 다른 객체지만 싱글톤인것 처럼 사용 가능
# __dict__(객체의 속성을 저장) : 클래스 내 모든 객체의 상태를 저장
# b1, b2는 서로 다른 객체지만, 동일한 상태를 공유
class Singleton2:

    __shared_state={"1":"2"}

    def __init__(self):
        self.x=1
        self.__dict__=self.__shared_state
        pass


def main():
    b1 = Singleton2()
    b2 = Singleton2()

    b1.x=5

    print (b1)
    print (b2)

    print (b1.__dict__)
    print (b2.__dict__)

if __name__ == "__main__":
    main()