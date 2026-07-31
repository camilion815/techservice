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

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    codigo_postal = input("Digite o código postal do cliente: ")

    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "codigo_postal": codigo_postal
    }

    cliente_repo.inserir(cliente)
    print("\nCliente inserido com sucesso!")
    
def atualizar_cliente():
    id_cliente = input("Digite o ID do cliente a ser atualizado: ")
    cliente = cliente_repo.buscar_por_id(id_cliente)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    nome = input(f"Digite o novo nome do cliente (atual: {cliente['nome']}): ")
    email = input(f"Digite o novo email do cliente (atual: {cliente['email']}): ")
    telefone = input(f"Digite o novo telefone do cliente (atual: {cliente['telefone']}): ")
    codigo_postal = input(f"Digite o novo código postal do cliente (atual: {cliente['codigo_postal']}): ")

    cliente_atualizado = {
        "id_cliente": id_cliente,
        "nome": nome or cliente["nome"],
        "email": email or cliente["email"],
        "telefone": telefone or cliente["telefone"],
        "codigo_postal": codigo_postal or cliente["codigo_postal"]
    }

    cliente_repo.atualizar(cliente_atualizado)
    print("\nCliente atualizado com sucesso!")
    
def eliminar_cliente():
    id_cliente = input("Digite o ID do cliente a ser eliminado: ")
    cliente = cliente_repo.buscar_por_id(id_cliente)

    if not cliente:
        print("\nCliente não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja eliminar o cliente {cliente['nome']}? (s/n): ")

    if confirmacao.lower() == "s":
        cliente_repo.eliminar(id_cliente)
        print("\nCliente eliminado com sucesso!")
    else:
        print("\nOperação cancelada.")

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

def criar_equipamento():
    nome = input("Digite o nome do equipamento: ")
    tipo = input("Digite o tipo do equipamento: ")
    descricao = input("Digite a descrição do equipamento: ")

    equipamento = {
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao
    }

    equipamento_repo.inserir(equipamento)
    print("\nEquipamento inserido com sucesso!")
    
def atualizar_equipamento():
    id_equipamento = input("Digite o ID do equipamento a ser atualizado: ")
    equipamento = equipamento_repo.buscar_por_id(id_equipamento)

    if not equipamento:
        print("\nEquipamento não encontrado.")
        return

    nome = input(f"Digite o novo nome do equipamento (atual: {equipamento['nome']}): ")
    tipo = input(f"Digite o novo tipo do equipamento (atual: {equipamento['tipo']}): ")
    descricao = input(f"Digite a nova descrição do equipamento (atual: {equipamento['descricao']}): ")

    equipamento_atualizado = {
        "id_equipamento": id_equipamento,
        "nome": nome or equipamento["nome"],
        "tipo": tipo or equipamento["tipo"],
        "descricao": descricao or equipamento["descricao"]
    }

    equipamento_repo.atualizar(equipamento_atualizado)
    print("\nEquipamento atualizado com sucesso!")
    
def eliminar_equipamento():
    id_equipamento = input("Digite o ID do equipamento a ser eliminado: ")
    equipamento = equipamento_repo.buscar_por_id(id_equipamento)

    if not equipamento:
        print("\nEquipamento não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja eliminar o equipamento {equipamento['nome']}? (s/n): ")

    if confirmacao.lower() == "s":
        equipamento_repo.eliminar(id_equipamento)
        print("\nEquipamento eliminado com sucesso!")
    else:
        print("\nOperação cancelada.")

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

def criar_ordem():
    id_cliente = input("Digite o ID do cliente: ")
    id_equipamento = input("Digite o ID do equipamento: ")
    diagnostico = input("Digite o diagnóstico: ")
    solucao = input("Digite a solução: ")
    status = input("Digite o status: ")
    prioridade = input("Digite a prioridade: ")
    custo_total = input("Digite o custo total: ")

    ordem = {
        "id_cliente": id_cliente,
        "id_equipamento": id_equipamento,
        "diagnostico": diagnostico,
        "solucao": solucao,
        "status": status,
        "prioridade": prioridade,
        "custo_total": custo_total
    }

    ordem_repo.inserir(ordem)
    print("\nOrdem de serviço inserida com sucesso!")
    
def atualizar_ordem():
    id_ordem = input("Digite o ID da ordem de serviço a ser atualizada: ")
    ordem = ordem_repo.buscar_por_id(id_ordem)

    if not ordem:
        print("\nOrdem de serviço não encontrada.")
        return

    id_cliente = input(f"Digite o novo ID do cliente (atual: {ordem['id_cliente']}): ")
    id_equipamento = input(f"Digite o novo ID do equipamento (atual: {ordem['id_equipamento']}): ")
    diagnostico = input(f"Digite o novo diagnóstico (atual: {ordem['diagnostico']}): ")
    solucao = input(f"Digite a nova solução (atual: {ordem['solucao']}): ")
    status = input(f"Digite o novo status (atual: {ordem['status']}): ")
    prioridade = input(f"Digite a nova prioridade (atual: {ordem['prioridade']}): ")
    custo_total = input(f"Digite o novo custo total (atual: {ordem['custo_total']}): ")

    ordem_atualizada = {
        "id_ordem": id_ordem,
        "id_cliente": id_cliente or ordem["id_cliente"],
        "id_equipamento": id_equipamento or ordem["id_equipamento"],
        "diagnostico": diagnostico or ordem["diagnostico"],
        "solucao": solucao or ordem["solucao"],
        "status": status or ordem["status"],
        "prioridade": prioridade or ordem["prioridade"],
        "custo_total": custo_total or ordem["custo_total"]
    }

    ordem_repo.atualizar(ordem_atualizada)
    print("\nOrdem de serviço atualizada com sucesso!")

def eliminar_ordem():
    id_ordem = input("Digite o ID da ordem de serviço a ser eliminada: ")
    ordem = ordem_repo.buscar_por_id(id_ordem)

    if not ordem:
        print("\nOrdem de serviço não encontrada.")
        return

    confirmacao = input(f"Tem certeza que deseja eliminar a ordem de serviço {id_ordem}? (s/n): ")

    if confirmacao.lower() == "s":
        ordem_repo.eliminar(id_ordem)
        print("\nOrdem de serviço eliminada com sucesso!")
    else:
        print("\nOperação cancelada.")
        
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