#-*- coding: utf-8 -*-

import abc


class PagePrinter(metaclass=abc.ABCMeta):
    """
    AbstractClass
    """

    def page_print(self, page_num, want_page_num, page_content):
        print("----- This is default page print Header -----")
        self._print_header()
        self._print_content(page_content)
        self._print_footer()

        if(want_page_num):
            print("my page num : " + str(page_num))

        print("----- This is default page print Footer -----")

    @abc.abstractmethod
    def _print_header(self):
        pass

    @abc.abstractmethod
    def _print_content(self, page_content):
        pass

    @abc.abstractmethod
    def _print_footer(self):
        pass


class MyPagePrinter(PagePrinter):
    """
    ConcreteClassA
    """

    def _print_header(self):
        print("=== my page printer Header ===")

    def _print_content(self, page_content):
        print(page_content)

    def _print_footer(self):
        print("=== my page printer Footer ===")


class YourPagePrinter(PagePrinter):
    """
    ConcreteClassB
    """

    def _print_header(self):
        print("*** your page printer Header ***")

    def _print_content(self, page_content):
        print(page_content)

    def _print_footer(self):
        print("*** your page printer Footer ***")


def main():
    my_page_printer = MyPagePrinter()
    my_page_printer.page_print(10, True, "Design Pattern")

    print("")

    your_page_printer = YourPagePrinter()
    your_page_printer.page_print(10, False, "Hororok")


if __name__ == "__main__":
    main()