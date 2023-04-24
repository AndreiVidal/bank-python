"""
    Este módulo contém a implementação da classe Person, que define uma pessoa
    genérica
"""

import accounts


class Person:
    """
        classe pessoa genérica
    """

    def __init__(self, name: str, age: int) -> None:
        """Inicializa uma instância de Pessoa.

        Parâmetros:
        :name (str): nome da pessoa
        :age (int): idade da pessoa.
        """
        self.name = name
        self.age = age

    # getters e setters criados afim de treinamento e estudo !!
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

    def __repr__(self) -> str:
        type_class = type(self).__name__
        class_name = f'Classe {type_class}'
        attrs = f'(Nome: {self.name!r}| Idade {self.age!r})'
        return f'{class_name} {attrs}'


class Client(Person):
    """
        Classe Cliente que herda de Pessoa
    """

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None


if __name__ == '__main__':
    c1 = Client('Andrei', 31)
    c1.account = accounts.SavingsAccount(125, 2525, 2500)
    print(c1)
    print(c1.account)
