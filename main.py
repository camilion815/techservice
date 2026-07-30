from src.repositories import cliente_repository as cliente_repo
from src.repositories import equipamento_repository as equipamento_repo
from src.repositories import ordem_de_servico_repository as ordem_repo


def listar_clientes():
    clientes = cliente_repo.listar()

    if not clientes:
        print("\nNão existem clientes.")
        return

    for item in clientes:
        print(
            item["id_cliente"],
            item["nome"],
            item["email"],
            item["telefone"],
            item["codigo_postal"]
        )


def listar_equipamentos():
    equipamentos = equipamento_repo.listar()

    if not equipamentos:
        print("\nNão existem equipamentos.")
        return

    for item in equipamentos:
        print(
            item["id_equipamento"],
            item["nome"],
            item["tipo"],
            item["descricao"]
        )


def listar_ordens():
    ordens = ordem_repo.listar()

    if not ordens:
        print("\nNão existem ordens de serviço.")
        return

    for item in ordens:
        print(
            item["id_ordem"],
            item["id_cliente"],
            item["id_equipamento"],
            item["diagnostico"],
            item["solucao"],
            item["status"],
            item["prioridade"],
            item["custo_total"]
        )


def menu_clientes():
    while True:

        print("\n=== Clientes ===")
        print("1 - Pesquisar")
        print("2 - Inserir")
        print("3 - Listar")
        print("4 - Atualizar")
        print("5 - Eliminar")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\nPesquisar clientes ainda não implementado.")

        elif opcao == "2":
            print("\nInserção de clientes ainda não implementada.")

        elif opcao == "3":
            listar_clientes()

        elif opcao == "4":
            print("\nAtualização de clientes ainda não implementada.")

        elif opcao == "5":
            print("\nEliminação de clientes ainda não implementada.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_equipamentos():
    while True:

        print("\n=== Equipamentos ===")
        print("1 - Pesquisar")
        print("2 - Inserir")
        print("3 - Listar")
        print("4 - Atualizar")
        print("5 - Eliminar")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\nPesquisar equipamentos ainda não implementado.")

        elif opcao == "2":
            print("\nInserção de equipamentos ainda não implementada.")

        elif opcao == "3":
            listar_equipamentos()

        elif opcao == "4":
            print("\nAtualização de equipamentos ainda não implementada.")

        elif opcao == "5":
            print("\nEliminação de equipamentos ainda não implementada.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_ordens():
    while True:

        print("\n=== Ordens de Serviço ===")
        print("1 - Pesquisar")
        print("2 - Inserir")
        print("3 - Listar")
        print("4 - Atualizar")
        print("5 - Eliminar")
        print("0 - Voltar")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\nPesquisar ordens ainda não implementado.")

        elif opcao == "2":
            print("\nInserção de ordens ainda não implementada.")

        elif opcao == "3":
            listar_ordens()

        elif opcao == "4":
            print("\nAtualização de ordens ainda não implementada.")

        elif opcao == "5":
            print("\nEliminação de ordens ainda não implementada.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_principal():
    while True:

        print("\n=== TechService - Sistema de Assistência Técnica ===")
        print("1 - Clientes")
        print("2 - Equipamentos")
        print("3 - Ordens de Serviço")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_equipamentos()

        elif opcao == "3":
            menu_ordens()

        elif opcao == "0":
            print("\nPrograma terminado.")
            break

        else:
            print("Opção inválida.")


def main():
    menu_principal()


if __name__ == "__main__":
    main()