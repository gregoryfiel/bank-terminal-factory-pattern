from bank_program.Conta import ContaSilver, ContaGold
from bank_program.ContasJSON import ContasJSON
import random

class ContaFactory():
    """Classe que representa uma fábrica de contas bancárias"""
    def __init__(self, contas=ContasJSON()):
        self.contas = []
        self.contas_json = contas

    def carregar_contas(self):
        dados_json = self.contas_json.carregar_contas()
        self.contas = [ContaSilver(**conta) if conta['saldo'] < 5000 else ContaGold(**conta) for conta in dados_json]

        return self.contas
    
    def salvar_contas(self):
        lista_contas = [conta.to_dict() for conta in self.contas]
        self.contas_json.salvar_contas(lista_contas)

    def criar_conta(self, nome, saldo_inicial):
        self.carregar_contas()

        if nome not in [conta.nome for conta in self.contas]:
            numero_conta = random.randrange(1000, 9999, 1)

            if saldo_inicial < 5000:
                nova_conta = ContaSilver(nome, numero_conta, saldo_inicial)
            else:
                nova_conta = ContaGold(nome, numero_conta, saldo_inicial)

            self.contas.append(nova_conta)
            print(f"\nConta criada com sucesso.")
            nova_conta.imprimir_saldo()

            self.salvar_contas()

        else:
            raise Exception("Já existe uma conta com esse nome")
        
    def acessar_conta(self, nome):
        self.carregar_contas()

        for conta in self.contas:
            if conta.nome == nome:
                return conta.imprimir_saldo()
        
        raise Exception("Conta não encontrada")
        
    def realizar_saque(self, nome, valor):
        self.carregar_contas()

        for conta in self.contas:
            if conta.nome == nome:
                conta.saque(valor)
                self.salvar_contas()
                
                return conta.imprimir_saldo()

        raise Exception("Conta não encontrada")

    def realizar_deposito(self, nome, valor):
        self.carregar_contas()

        for conta in self.contas:
            if conta.nome == nome:
                conta.deposito(valor)
                self.salvar_contas()

                return conta.imprimir_saldo()
            
        raise Exception("Conta não encontrada")

    def realizar_emprestimo(self, nome, valor):
        self.carregar_contas()

        for conta in self.contas:
            if conta.nome == nome:
                conta.emprestimo(valor)
                self.salvar_contas()

                return conta.imprimir_saldo()
            
        raise Exception("Conta não encontrada")

    def proximo_mes(self, nome):
        self.carregar_contas()

        for conta in self.contas:
            if conta.nome == nome:
                conta.proximo_mes()
                self.salvar_contas()

                return conta.imprimir_saldo()
        
        raise Exception("Conta não encontrada")
