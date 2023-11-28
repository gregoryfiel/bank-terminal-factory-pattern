from bank_program.ContaFactory import ContaFactory
import unittest

class FakeContasJSON():
    def carregar_contas(self):
        return [{'nome': 'João', 'numero': 1234, 'saldo': 1000, 'divida': 0, 'juros': 0.03, 'data_emprestimo': "20/06/2024 14:58:33"}]

    def salvar_contas(self, contas):
        pass


class TestContaFactory(unittest.TestCase):
    def test_init(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        self.assertEqual(conta_factory.contas, [])
        self.assertIsInstance(conta_factory.contas_json, FakeContasJSON)

    def test_carregar_contas(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        self.assertEqual(len(conta_factory.contas), 1)
        self.assertEqual(conta_factory.contas[0].nome, 'João')
    
    def test_salvar_contas(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        conta_factory.salvar_contas()
        self.assertEqual(len(conta_factory.contas), 1)

    def test_criar_conta(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.criar_conta("Maria", 1000)
        self.assertEqual(len(conta_factory.contas), 2)
        self.assertEqual(conta_factory.contas[1].nome, 'Maria')

    def test_criar_conta_já_existente(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        with self.assertRaises(Exception):
            conta_factory.criar_conta("João", 1000)

    def test_acessar_conta(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        conta_factory.acessar_conta("João")
        self.assertEqual(len(conta_factory.contas), 1)
        self.assertEqual(conta_factory.contas[0].nome, 'João')

    def test_acessar_conta_inexistente(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        with self.assertRaises(Exception):
            conta_factory.acessar_conta("Maria")

    def test_realizar_saque(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        conta_factory.realizar_saque("João", 100)
        self.assertEqual(len(conta_factory.contas), 1)
        self.assertEqual(conta_factory.contas[0].nome, 'João')
        self.assertEqual(conta_factory.contas[0].saldo, 900)

    def test_realizar_saque_inexistente(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        with self.assertRaises(Exception):
            conta_factory.realizar_saque("Maria", 100)

    def test_deposito(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        conta_factory.realizar_deposito("João", 100)
        self.assertEqual(len(conta_factory.contas), 1)
        self.assertEqual(conta_factory.contas[0].nome, 'João')
        self.assertEqual(conta_factory.contas[0].saldo, 1100)

    def test_deposito_inexistente(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        with self.assertRaises(Exception):
            conta_factory.realizar_deposito("Maria", 100)

    def test_emprestimo_silver(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        with self.assertRaises(Exception):
            conta_factory.realizar_emprestimo("João", 100)

    def test_emprestimo_inexistente(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        with self.assertRaises(Exception):
            conta_factory.realizar_emprestimo("Maria", 100)

    def test_proximo_mes(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        conta_factory.carregar_contas()
        conta_factory.proximo_mes("João")
        self.assertEqual(len(conta_factory.contas), 1)
        self.assertEqual(conta_factory.contas[0].nome, 'João')
        self.assertEqual(conta_factory.contas[0].saldo, 1000)
        self.assertEqual(conta_factory.contas[0].divida, 0)
        self.assertEqual(conta_factory.contas[0].data_emprestimo, "20/07/2024 14:58:33")

    def test_proximo_mes_inexistente(self):
        conta_factory = ContaFactory(contas=FakeContasJSON())
        with self.assertRaises(Exception):
            conta_factory.proximo_mes("Maria")
