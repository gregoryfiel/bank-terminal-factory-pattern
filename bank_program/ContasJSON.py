import os
import json

class ContasJSON():
    """Classe que gerencia um arquivo JSON de contas bancárias"""
    def verifica_pasta(self):
        path = os.path.join("bank_program", "arquivos_json")
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        return path
    
    def salvar_contas(self, lista_contas):
        try:
            path = self.verifica_pasta()
            
            with open(f"{path}/contas.json", "w") as outfile:
                json.dump(lista_contas, outfile, indent=4)
        
        except Exception as e:
            print(f"Erro ao gerar arquivo ranking.json: {e}")
    
    def carregar_contas(self):
        path = self.verifica_pasta()
        contas_path = os.path.join(path, 'contas.json')

        if os.path.exists(contas_path) and os.path.getsize(contas_path) > 0:
            with open(contas_path, 'r') as file:
                contas = json.load(file)
        else:
            contas = []

        return contas
