from src.repositories import cliente_repository as cliente_repo
from src.repositories import equipamento_repository as equipamento_repo
from src.repositories import ordem_de_servico_repository as ordem_repo


REPOSITORIOS = {
    "1": ("Cliente", cliente_repo),
    "2": ("Equipamento", equipamento_repo),
    "3": ("Ordem de Serviço", ordem_repo),
}


def menu_crud(nome, repo):
    while True:
        print(f"\n===== {nome.upper()} =====")
        print("1 - Listar")
        print("2 - Criar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                resultado = repo.listar(None)
                if resultado:
                    for item in resultado:
                        print(item)
                else:
                    print("Nenhum registo encontrado.")
            except Exception as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("\nA criação é efetuada pelo método:")
            print(f"{repo.__name__}.criar(objeto)")

        elif opcao == "3":
            print("\nA atualização é efetuada pelo método:")
            print(f"{repo.__name__}.atualizar(objeto)")

        elif opcao == "4":
            print("\nA eliminação é efetuada pelo método:")
            print(f"{repo.__name__}.deletar(...)")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\n========== TECHSERVICE ==========")
        print("1 - Clientes")
        print("2 - Equipamentos")
        print("3 - Ordens de Serviço")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Programa terminado.")
            break

        if opcao in REPOSITORIOS:
            nome, repo = REPOSITORIOS[opcao]
            menu_crud(nome, repo)
        else:
            print("Opção inválida.")


def main():
    menu_principal()


if __name__ == "__main__":
    main()