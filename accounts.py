"""
    Este módulo contém a implementação da classe Account, que define uma conta
    bancária.
"""
import abc


class Account(abc.ABC):
    """
    Classe abstrata que define uma conta bancária.
    """

    def __init__(self,
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
    def withdrawal(self, amount: float) -> float:
        """
        Método abstrato para realizar um saque na conta.

        Parâmetros:
        :amount (float): valor a ser sacado.
        """

    def deposit(self, value: float = None) -> float:  # type: ignore
        """
        Método para realizar um depósito na conta.

        Parâmetros:
        :value (float): valor a ser depositado.
        """
        if value == None:

            value = input('Qual valor para depósito ')
            if not value.isdigit():
                print('digit apenas numeros')
            else:
                value = float(value)
                self.balance += value
                self.details(f'Deposito de R$ {value:.2f} ')

    def details(self, msg: str = '') -> str:  # type: ignore
        """
        Método para mostrar detalhes do que foi feito.

        Parâmetros:
        :msg (str): mensagem que vai aparecer na ação.
        """
        print(f'{msg}\nO seu saldo atual é de R$ {self.balance:.2f}')

    def __repr__(self) -> str | float:
        type_class = type(self).__name__
        class_name = f'Classe {type_class}'
        attrs = f'(Agencia: {self.agency!r}| Conta {self.account!r})'\
                f' | Saldo R$ {self.balance:.2f})'
        return f'{class_name} {attrs}'


class SavingsAccount(Account):
    """
    Classe que define uma conta poupança.
    """

    def withdrawal(self, amount: float) -> float:  # type: ignore
        """
        Realiza um saque na conta poupança.

        Parâmetros:
        :amount (float): valor a ser sacado.
        """

        if amount <= self.balance:
            self.balance -= amount
            self.details(f'Saque de R$ {amount:.2f} efetuado com sucesso.')
            return self.balance

        print('Não é possível sacar. Saldo insuficiente.')


class CheckingAccount(Account):
    """
    Classe que define uma conta corrente.
    """

    def __init__(self,
                 agency: int,
                 account: int,
                 balance: int | float,
                 limit: int | float

                 ) -> None:
        """
        Inicializa uma instância de CheckingAccount.

        Parâmetros:
        :agency (int): número da agência.
        :account (int): número da conta.
        :balance (int ou float): saldo inicial da conta.
        :limit (float): limite de cheque especial.
        """
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdrawal(self, amount: int | float) -> None:
        """
        Realiza um saque na conta corrente.

        Parâmetros:
        :amount (float): valor a ser sacado.
        """

        if amount <= self.balance + self.limit:
            self.balance -= amount
            self.details(
                f'Voçê efetuou um saque no valor de R$ {amount:.2f}'
                f' com sucesso')
            return
        print(
            f'Saque no valor de R$ {amount:.2f} Recusado !\n'
            f'Saldo insuficiente!\nSaldo: R$ {self.balance:.2f}\n'
            f'Limite disponivel: R$ {self.limit:.2f}'
        )


# verificando o funcionamento
if __name__ == '__main__':
    checking_account1 = CheckingAccount(111, 222, 100, 20)
    checking_account1.details()
    # output: O seu saldo atual é de R$ 100.00
    checking_account1.withdrawal(1000)
    # output: Saldo insuficiente!
    #         Saldo: R$ 100.00.00
    #         Limite disponivel: R$ 20.00
    checking_account1.deposit()
    # output: Deposito de R$ 1000.00
    #        O seu saldo atual é de R$ 1100.00
    checking_account1.withdrawal(1120)
    # output: Voçê efetuou um saque no valor de R$ 1120.00 com sucesso
    # O seu saldo atual é de R$ -20.00
