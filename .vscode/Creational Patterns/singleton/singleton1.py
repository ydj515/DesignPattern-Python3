#-*- coding: utf-8 -*-

# __new__ 생성자를 이용해 구현
# __new__ 생성자는 __init__이 반환값을 가질 수 없는 점을 보완한 생성자
class Singleton(object):
    def __new__(self):
        if not hasattr(self,'instance'): # instance 라는 속성이 없다면
            self.instance = super(Singleton,self).__new__(self)
            return self.instance

def main():
    s = Singleton()
    s2 = Singleton()

    print(s)
    print(s2)

if __name__ == "__main__":
    main()