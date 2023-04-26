"""
    módulo principal
"""

import person
import accounts

checking_account1 = accounts.CheckingAccount(111, 222, 100, 20)
checking_account1.details()
# output: O seu saldo atual é de R$ 100.00
checking_account1.withdrawal(1000)
# output: Saldo insuficiente!
#         Saldo: R$ 100.00.00
#         Limite disponivel: R$ 20.00
checking_account1.deposit(1000)
# output: Deposito de R$ 1000.00
#        O seu saldo atual é de R$ 1100.00
checking_account1.withdrawal(1120)
# output: Voçê efetuou um saque no valor de R$ 1120.00 com sucesso
# O seu saldo atual é de R$ -20.00


print("#"*3)

c1 = person.Client('Andrei', 31)
c1.account = accounts.SavingsAccount(125, 2525, 2500)
print(c1)
# output: Classe Client (Nome: 'Andrei'| Idade 31)
print(c1.account)
# output: Classe SavingsAccount (Agencia: 125| Conta 2525) |
# Saldo R$ 2500.00)
