#-*- coding: utf-8 -*-

import abc

class Director:
    """
    director
    """

    def __init__(self):
        self._builder = None

    def make(self, builder):
        self._builder = builder
        self._builder._make_header()
        self._builder._make_body()
        self._builder._make_footer()


class Builder(metaclass=abc.ABCMeta):
    """
    builder
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _make_header(self):
        pass

    @abc.abstractmethod
    def _make_body(self):
        pass

    @abc.abstractmethod
    def _make_footer(self):
        pass


class PlainTextBuilder(Builder):
    """
    ConcreteBuilderA
    """

    def _make_header(self):
        print("hh")

    def _make_body(self):
        print("bb")

    def _make_footer(self):
        print("ff")


class HtmlBuilder(Builder):
    """
    ConcreteBuilderB
    """

    def _make_header(self):
        print("<html>")
        print("<title>")
        print("</title>")

    def _make_body(self):
        print("<body>")
        print("</body")

    def _make_footer(self):
        print("<footer>")
        print("</footer")
        print("</html>")


class Product:
    """
    product
    """

    pass


def main():
    plain_text_builder = PlainTextBuilder()
    html_builder = HtmlBuilder()
    director = Director()
    director.make(plain_text_builder)
    product = plain_text_builder.product

    print("==================================")

    director.make(html_builder)
    product = html_builder.product


if __name__ == "__main__":
    main()