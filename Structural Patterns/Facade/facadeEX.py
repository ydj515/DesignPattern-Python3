#-*- coding: utf-8 -*-

class HomeTheaterFacade:
    """
    Facade
    """
    def __init__(self):
        self.dvdPlayer = DvdPlayer()
        self.cdPlayer = CdPlayer()
        self.screen = Screen()
        self.projector = Projector()

    def turnOnOperationTvMode(self):
        self.screen.down()
        self.projector.tvMode()
        self.cdPlayer.stop()
        self.dvdPlayer.play()

    def turnOffOperationWideScreen(self):
        self.screen.up()
        self.projector.wideScreenMode()
        self.cdPlayer.play()
        self.dvdPlayer.stop()


class DvdPlayer:
    def on(self):
        print("DvdPlayer On")

    def off(self):
        print("DvdPlayer Off")

    def play(self):
        print("DvdPlayer Play")

    def stop(self):
        print("DvdPlayer Stop")

    def pause(self):
        print("DvdPlayer Pause")


class CdPlayer:
    def on(self):
        print("CdPlayer On")

    def off(self):
        print("CdPlayer Off")

    def play(self):
        print("CdPlayer Play")

    def stop(self):
        print("CdPlayer Stop")

    def pause(self):
        print("CdPlayer Pause")


class Screen:
    def up(self):
        print("Screen Up")
    def down(self):
        print("Screen Down")


class Projector:
    def on(self):
        print("Projector On")

    def off(self):
        print("Projector Off")

    def wideScreenMode(self):
        print("Projector WideScreenMode")

    def tvMode(self):
        print("Projector TvMode")


def main():
    facade = HomeTheaterFacade()

    facade.turnOnOperationTvMode()
    print("====================")
    facade.turnOffOperationWideScreen()


if __name__ == "__main__":
    main()