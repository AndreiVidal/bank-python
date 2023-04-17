import abc


class Account(abc.ABC):
    def __init__(self, agency: int, account: int, balance: int | float) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance
        
        
    @abc.abstractmethod
    def withdrawal(self, amount: float) -> None: ...
