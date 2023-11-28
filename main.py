import argparse
from bank_program.ContaFactory import ContaFactory

def main():
    """Função principal do programa"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--criar_conta", nargs="*", default=False,
                        help="Cria uma nova conta bancária")
    parser.add_argument("--acessar_conta", nargs="*", default=False,
                        help="Acessa uma conta bancária existente")
    parser.add_argument("--saque", nargs=2, default=False,
                        help="Realiza um saque em uma conta bancária")
    parser.add_argument("--deposito", nargs=2, default=False,
                        help="Realiza um depósito em uma conta bancária")
    parser.add_argument("--emprestimo", nargs=2, default=False,
                        help="Realiza um empréstimo em uma conta bancária")
    parser.add_argument("--proximo_mes", nargs=1, default=False,
                        help="Passa para o próximo mês em uma conta bancária")

    args = parser.parse_args()

    try:
        conta = ContaFactory()
        if args.criar_conta:
            conta.criar_conta(args.criar_conta[0], float(args.criar_conta[1]))
            
        elif args.acessar_conta:
            conta.acessar_conta(args.acessar_conta[0])

        elif args.saque:
            conta.realizar_saque(args.saque[0], float(args.saque[1]))

        elif args.deposito:
            conta.realizar_deposito(args.deposito[0], float(args.deposito[1]))

        elif args.emprestimo:
            conta.realizar_emprestimo(args.emprestimo[0], float(args.emprestimo[1]))

        elif args.proximo_mes:
            conta.proximo_mes(args.proximo_mes[0])
        
    except Exception as e:
        print(f"Erro: {e}.")


if __name__ == "__main__":
    main()
