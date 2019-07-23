#-*- coding: utf-8 -*-

import abc

class Component(metaclass=abc.ABCMeta):
    """
    Component
    """
    
    @abc.abstractmethod
    def printInfo(self): # 정보 출력
        pass
    
    @abc.abstractmethod
    def getSize(self): # size 출력
        pass
        
    @abc.abstractmethod
    def getName(self): # 이름만 출력
        pass
    

class Directory(Component):
    """
    Composite
    """

    def __init__(self, name):
        self._children = []
        self._name = name

    def printInfo(self):
        self._sum = 0
        print("============" + self._name + "============")
        for i in range(0, len(self._children)):
            print(self._children[i].getName() + " : " + str(self._children[i].getSize()))
            self._sum += self._children[i].getSize()

        print("Directory total size : " + str(self._sum))
        

    def getName(self):
        return self._name
        
    def getSize(self):
        return self._sum
        
    def addEntry(self, component):
        self._children.append(component)

    def removeEntry(self, component):
        self._children.remove(component)

    
class File(Component):
    """
    Leaf
    """

    def __init__(self, name, size):
        self._name = name
        self._size = size

    def printInfo(self):
        print(self._name)

    def getSize(self):
        return self._size
    
    def getName(self):
        return self._name


def main():

    dir1 = Directory("root")
    dir2 = Directory("sub")

    f1 = File("f1", 100)
    f2 = File("f2",50)
    f3 = File("f3", 200)
    f4 = File("f4", 10)
    f5 = File("f5", 70)

    dir1.addEntry(f3)
    dir1.addEntry(f4)
    dir1.addEntry(f5)
    dir1.printInfo()

    dir2.addEntry(f1)
    dir2.addEntry(f2)
    dir2.printInfo()

    dir1.addEntry(dir2)
    dir1.printInfo()

if __name__ == "__main__":
    main()