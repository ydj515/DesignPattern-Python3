#-*- coding: utf-8 -*-

# Metaclass를 사용하여 singleton 구현
# Metaclass : class 의 class

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

        
class Logger(metaclass=MetaSingleton): # python2 에서는  metaclass를 쓸 수 없다.
    pass


def main():
    logger1 = Logger()
    logger2 = Logger()

    print(logger1)
    print(logger2)

if __name__ == "__main__":
    main()