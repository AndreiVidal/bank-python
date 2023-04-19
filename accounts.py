"""
    Este módulo contém a implementação da classe Account, que define uma conta bancária.
"""
import abc


class Account(abc.ABC):
    """
    Classe abstrata que define uma conta bancária.
    """

    def __init__(
        self,
        agency: int,
        account: int,
        balance: int | float
    ) -> None:
        """
        Inicializa uma instância de Account.

        Parâmetros:
        :agency (int): número da agência.
        :account (int): número da conta.
        :balance (int ou float): saldo inicial da conta.
        """

        self.agency = agency
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def withdrawal(
        self,
        amount: float
    ) -> None:
        """
        Método abstrato para realizar um saque na conta.

        Parâmetros:
        :amount (float): valor a ser sacado.
        """

    def deposit(
        self,
        value: float
    ) -> None:
        """
        Método para realizar um depósito na conta.

        Parâmetros:
        :value (float): valor a ser depositado.
        """
        self.balance += value
        self.details(f'Deposito de R$ {value:.2f} ')
    
    def details(
        self,
        msg: str = ''
    ) -> str :
        print(f'O seu saldo é R$ {self.balance:.2f} {msg}')
        