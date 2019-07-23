#-*- coding: utf-8 -*-

import abc


class Light:
    """
    context
    """

    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def switch_on(self):
        self._state.on_button_push()
    
    def switch_off(self):
        self._state.off_button_push()


class State(metaclass=abc.ABCMeta):
    """
    state
    """
        
    @abc.abstractmethod
    def on_button_push(self):
        pass

        
    @abc.abstractmethod
    def off_button_push(self):
        pass


class Off(State):
    """
    ConcreteStateA
    """

    def __init__(self):
        pass

    def on_button_push(self):
        print("switch on")
        # light.set_state(Off())     

    def off_button_push(self):
        print("staying")

class On(State):
    """
    ConcreteStateB
    """

    def on_button_push(self):
        print("staying")


    def off_button_push(self):
        print("switch off")
        # self._state = Off()


def main():
    off = Off()
    on = On()

    light = Light(off) # 초기 상태는 off

    light.switch_on()
    light.set_state(on) ###### 애바임 여기 수정해야함!

    light.switch_off()
    light.switch_on()
    light.switch_on()


if __name__ == "__main__":
    main()