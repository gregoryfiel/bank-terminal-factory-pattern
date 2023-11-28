from bank_program.ContasJSON import ContasJSON
import unittest
from unittest.mock import patch

class TestContasJSON(unittest.TestCase):
    def test_verifica_pasta(self):
        contas_json = ContasJSON()
        path = contas_json.verifica_pasta()
        self.assertEqual(path, "bank_program\\arquivos_json")

    @patch('bank_program.ContasJSON.json.dump')
    def test_salvar_contas(self, mock_dump):
        contas_json = ContasJSON()
        contas = [{'nome': 'João', 'numero': 1234, 'saldo': 1000, 'divida': 0, 'juros': 0.03, 'data_emprestimo': None}]
        contas_json.salvar_contas(contas)
        mock_dump.assert_called_once()

    @patch('bank_program.ContasJSON.ContasJSON.verifica_pasta')
    def test_salvar_contas_erro(self, mock_verifica_pasta):
        contas_json = ContasJSON()
        mock_verifica_pasta.side_effect = Exception("Erro ao gerar arquivo contas.json")
        contas = [{'nome': 'João', 'numero': 1234, 'saldo': 1000, 'divida': 0, 'juros': 0.03, 'data_emprestimo': None}]
        contas_json.salvar_contas(contas)
        mock_verifica_pasta.assert_called_once()

    @patch('bank_program.ContasJSON.json.load')
    def test_carregar_contas(self, mock_load):
        contas_json = ContasJSON()
        contas_json.carregar_contas()
        mock_load.called_once_with("bank_program\\arquivos_json\\contas.json")
