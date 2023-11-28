from datetime import datetime, timedelta

class Conta():
    """Classe que representa uma conta bancária"""
    def __init__(self, nome, numero, saldo, divida=0, juros=0.03, data_emprestimo=None):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.divida = divida
        self.juros = juros
        self.data_emprestimo = data_emprestimo
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            return print(f'Saldo insuficiente para realizar o saque de R$ {valor:.2f}.')
    
    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    
    def emprestimo(self, valor):
        self.saldo += valor
        self.divida += valor * (1 + self.juros)
        self.data_emprestimo = datetime.now()
        self.data_emprestimo = self.data_emprestimo.strftime("%d/%m/%Y %H:%M:%S")
        print(f'Empréstimo de R$ {valor:.2f} realizado com sucesso.')

    def proximo_mes(self):
        if self.data_emprestimo is not None:
            self.data_emprestimo = datetime.strptime(self.data_emprestimo, "%d/%m/%Y %H:%M:%S")
            self.data_emprestimo += timedelta(days=30)
            self.data_emprestimo = self.data_emprestimo.strftime("%d/%m/%Y %H:%M:%S")
            self.divida *= (1 + self.juros)
            print(f'Dívida atualizada para R$ {self.divida:.2f} na data {self.data_emprestimo}.')
        
        else:
            print('Não há empréstimos para serem atualizados.')

    def imprimir_saldo(self):
        print("-" * 50)
        print(f'Conta: {self.nome} | Número {self.numero} | Saldo: R$ {self.saldo:.2f}')
        print("-" * 50)

    def to_dict(self):
        return {'nome': self.nome, 'numero': self.numero, 'saldo': self.saldo, 'divida': self.divida, 'juros': self.juros, 'data_emprestimo': self.data_emprestimo}
    

class ContaSilver(Conta):
    """Classe que representa uma conta Silver, que não permite empréstimos"""
    def __init__(self, nome, numero, saldo, divida=0, juros=0.03, data_emprestimo=None):
        super().__init__(nome, numero, saldo, divida, juros, data_emprestimo)
    
    def saque(self, valor):
        super().saque(valor)
    
    def deposito(self, valor):
        super().deposito(valor)
    
    def emprestimo(self, valor):
        raise Exception('Conta Silver não permite empréstimos')
    
    def proximo_mes(self):
        super().proximo_mes()
    
    def imprimir_saldo(self):
        print("-" * 75)
        print(f'Conta: {self.nome} | Número {self.numero} | Saldo: R$ {self.saldo:.2f} | Conta Silver')
        print("-" * 75)
    
    def to_dict(self):
        return super().to_dict()
    

class ContaGold(Conta):
    """Classe que representa uma conta Gold, que permite empréstimos"""
    def __init__(self, nome, numero, saldo, divida=0, juros=0.03, data_emprestimo=None):
        super().__init__(nome, numero, saldo, divida, juros, data_emprestimo)

    def saque(self, valor):
        super().saque(valor)
        
    def deposito(self, valor):
        super().deposito(valor)
    
    def emprestimo(self, valor):
        super().emprestimo(valor)

    def proximo_mes(self):
        super().proximo_mes()

    def imprimir_saldo(self):
        print("-" * 80)
        print(f'Conta: {self.nome} | Número {self.numero} | Saldo: R$ {self.saldo:.2f} | Dívida: R$ {self.divida:.2f} | Conta Gold')
        print("-" * 80)
    
    def to_dict(self):
        return super().to_dict()
