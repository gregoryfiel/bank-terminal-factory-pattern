from bank_program.Conta import ContaSilver, ContaGold, Conta
import unittest
from unittest.mock import patch, MagicMock
import io
import sys

class TestConta(unittest.TestCase):
    suppress_text = io.StringIO()
    sys.stdout = suppress_text

    def test_init(self):
        conta = Conta("João", 1234, 1000)
        self.assertEqual(conta.nome, "João")
        self.assertEqual(conta.numero, 1234)
        self.assertEqual(conta.saldo, 1000)
        self.assertEqual(conta.divida, 0)
        self.assertEqual(conta.juros, 0.03)
        self.assertEqual(conta.data_emprestimo, None)

    def test_saque(self):
        conta = Conta("João", 1234, 1000)
        conta.saque(100)
        self.assertEqual(conta.saldo, 900)

    def test_saque_sem_saldo(self):
        conta = Conta("João", 1234, 1000)
        conta.saque(1100)
        self.assertEqual(conta.saldo, 1000)

    def test_deposito(self):
        conta = Conta("João", 1234, 1000)
        conta.deposito(100)
        self.assertEqual(conta.saldo, 1100)

    def test_emprestimo(self):
        conta = Conta("João", 1234, 1000)
        conta.emprestimo(100)
        self.assertEqual(conta.divida, 103.0)
    
    def test_proximo_mes(self):
        conta = Conta("João", 1234, 1000)
        conta.emprestimo(100)
        conta.proximo_mes()
        self.assertEqual(conta.divida, 106.09)

    @patch('bank_program.Conta.print')
    def test_imprimir_saldo(self, mock_print):
        conta = Conta("João", 1234, 1000)
        conta.imprimir_saldo()
        mock_print.assert_called()

    def test_to_dict(self):
        conta = Conta("João", 1234, 1000)
        self.assertEqual(conta.to_dict(), {'nome': 'João', 'numero': 1234, 'saldo': 1000, 'divida': 0, 'juros': 0.03, 'data_emprestimo': None})


class TestContaSilver(unittest.TestCase):
    def test_init(self):
        conta = ContaSilver("João", 1234, 1000)
        self.assertEqual(conta.nome, "João")
        self.assertEqual(conta.numero, 1234)
        self.assertEqual(conta.saldo, 1000)
        self.assertEqual(conta.divida, 0)
        self.assertEqual(conta.juros, 0.03)
        self.assertEqual(conta.data_emprestimo, None)
    
    def test_saque(self):
        conta = ContaSilver("João", 1234, 1000)
        conta.saque(100)
        self.assertEqual(conta.saldo, 900)

    def test_saque_sem_saldo(self):
        conta = ContaSilver("João", 1234, 1000)
        conta.saque(1100)
        self.assertEqual(conta.saldo, 1000)

    def test_deposito(self):
        conta = ContaSilver("João", 1234, 1000)
        conta.deposito(100)
        self.assertEqual(conta.saldo, 1100)

    def test_emprestimo(self):
        conta = ContaSilver("João", 1234, 1000)
        with self.assertRaises(Exception):
            conta.emprestimo(100)

    @patch('bank_program.Conta.print')
    def test_imprimir_saldo(self, mock_print):
        conta = ContaSilver("João", 1234, 1000)
        conta.imprimir_saldo()
        mock_print.assert_called()

    def test_to_dict(self):
        conta = ContaSilver("João", 1234, 1000)
        self.assertEqual(conta.to_dict(), {'nome': 'João', 'numero': 1234, 'saldo': 1000, 'divida': 0, 'juros': 0.03, 'data_emprestimo': None})


class TestContaGold(unittest.TestCase):
    def test_init(self):
        conta = ContaGold("João", 1234, 1000)
        self.assertEqual(conta.nome, "João")
        self.assertEqual(conta.numero, 1234)
        self.assertEqual(conta.saldo, 1000)
        self.assertEqual(conta.divida, 0)
        self.assertEqual(conta.juros, 0.03)
        self.assertEqual(conta.data_emprestimo, None)

    def test_saque(self):
        conta = ContaGold("João", 1234, 1000)
        conta.saque(100)
        self.assertEqual(conta.saldo, 900)

    def test_saque_sem_saldo(self):
        conta = ContaGold("João", 1234, 1000)
        conta.saque(1100)
        self.assertEqual(conta.saldo, 1000)

    def test_deposito(self):
        conta = ContaGold("João", 1234, 1000)
        conta.deposito(100)
        self.assertEqual(conta.saldo, 1100)

    def test_emprestimo(self):
        conta = ContaGold("João", 1234, 1000)
        conta.emprestimo(100)
        self.assertEqual(conta.divida, 103.0)

    def test_proximo_mes(self):
        conta = ContaGold("João", 1234, 1000)
        conta.emprestimo(100)
        conta.proximo_mes()
        self.assertEqual(conta.divida, 106.09)

    @patch('bank_program.Conta.print')
    def test_imprimir_saldo(self, mock_print):
        conta = ContaGold("João", 1234, 1000)
        conta.imprimir_saldo()
        mock_print.assert_called()

    def test_to_dict(self):
        conta = ContaGold("João", 1234, 1000)
        self.assertEqual(conta.to_dict(), {'nome': 'João', 'numero': 1234, 'saldo': 1000, 'divida': 0, 'juros': 0.03, 'data_emprestimo': None})

if __name__ == "__main__":
    unittest.main()
