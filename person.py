"""
    Este módulo contém a implementação da classe Person, que define uma pessoa
    genérica
"""


class Person:
    """
        classe pessoa genérica
    """

    def __init__(self, name: str, age: int) -> None:
        """Inicializa uma instância de Account.

        Parâmetros:
        :name (str): nome da pessoa
        :age (int): idade da pessoa.
        """
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age
