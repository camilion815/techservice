from src.models.cliente import Cliente
from src.models.equipamento import Equipamento
from src.models.ordem_de_servico import ordem_de_servico

from src.repositories import cliente_repository as cliente_repo
from src.repositories import equipamento_repository as equipamento_repo
from src.repositories import ordem_de_servico_repository as ordem_repo


def menu_principal():
    while True:
        print("\n===== MENU =====")
        print("1 - Clientes")
        print("2 - Equipamentos")
        print("3 - Ordens de Serviço")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_equipamentos()
        elif opcao == "3":
            menu_ordens()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")



def menu_clientes():
    while True:
        print("\n--- CLIENTES ---")
        print("1 - Listar")
        print("2 - Adicionar")
        print("3 - Atualizar")
        print("4 - Eliminar")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            clientes = cliente_repo.listar(None)
            for c in clientes:
                print(c)

        elif op == "2":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            codigo = input("Código Postal: ")

            cliente = Cliente(
                nome=nome,
                email=email,
                telefone=telefone,
                codigo_postal=codigo
            )

            cliente_repo.criar(cliente)
            print("Cliente criado.")

        elif op == "3":
            id_cliente = int(input("ID do cliente: "))
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            codigo = input("Código Postal: ")

            cliente = Cliente(
                id_cliente=id_cliente,
                nome=nome,
                email=email,
                telefone=telefone,
                codigo_postal=codigo
            )

            cliente_repo.atualizar(cliente)
            print("Cliente atualizado.")

        elif op == "4":
            id_cliente = int(input("ID do cliente: "))

            cliente = Cliente(
                id_cliente=id_cliente,
                nome="",
                email=""
            )

            cliente_repo.deletar(cliente)
            print("Cliente eliminado.")

        elif op == "0":
            break



def menu_equipamentos():
    while True:
        print("\n--- EQUIPAMENTOS ---")
        print("1 - Listar")
        print("2 - Adicionar")
        print("3 - Atualizar")
        print("4 - Eliminar")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            for e in equipamento_repo.listar(None):
                print(e)

        elif op == "2":
            print("Pedir todos os campos...")
            nome = input("Nome: ")
            tipo = input("Tipo: ")
            descricao = input("Descrição: ")
            
            
            equipamento = Equipamento(
                nome=nome,
                tipo=tipo,
                descricao=descricao,
                
            )
            equipamento_repo.criar(equipamento)
            
            
        elif op == "3":
            print("Pedir ID e restantes campos...")
            id_eq = int(input("ID: "))
            nome = input("Nome: ")
            tipo = input("Tipo: ")
            descricao = input("Descrição: ")
            
            equipamento = Equipamento(
                id_equipamento=id_eq,
                nome=nome,
                tipo=tipo,
                descricao=descricao,
            )
            equipamento_repo.atualizar(equipamento)
            

        elif op == "4":
            id_eq = int(input("ID: "))
            equipamento_repo.deletar(id_eq)

        elif op == "0":
            break



def menu_ordens():
    while True:
        print("\n--- ORDENS DE SERVIÇO ---")
        print("1 - Listar")
        print("2 - Adicionar")
        print("3 - Atualizar")
        print("4 - Eliminar")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            for ordem in ordem_repo.listar(None):
                print(ordem)

        elif op == "2":
            print("Pedir todos os campos...")
            id_cliente = int(input("ID do cliente: "))
            id_equipamento = int(input("ID do equipamento: "))
            diagnostico = input("Diagnóstico: ")
            solucao = input("Solução: ")
            status = input("Status: ")
            prioridade = input("Prioridade: ")
            custo_total = float(input("Custo total: "))

            ordem = ordem_de_servico(
                id_cliente=id_cliente,
                id_equipamento=id_equipamento,
                diagnostico=diagnostico,
                solucao=solucao,
                status=status,
                prioridade=prioridade,
                custo_total=custo_total
            )

            ordem_repo.criar(ordem)

        elif op == "3":
            print("Pedir ID e restantes campos...")
            id_ordem = int(input("ID da ordem: "))
            id_cliente = int(input("ID do cliente: "))
            id_equipamento = int(input("ID do equipamento: "))
            diagnostico = input("Diagnóstico: ")
            solucao = input("Solução: ")
            status = input("Status: ")
            prioridade = input("Prioridade: ")
            custo_total = float(input("Custo total: "))
            
            ordem = ordem_de_servico(
                id=id_ordem,
                cliente_id=id_cliente,
                equipamento_id=id_equipamento,
                diagnostico=diagnostico,
                solucao=solucao,
                status=status,
                prioridade=prioridade,
                custo_total=custo_total
            )
            ordem_repo.atualizar(ordem)

        elif op == "4":
            id_ordem = int(input("ID da ordem: "))
            ordem = ordem_de_servico(
                id=id_ordem,
                cliente_id=None,
                equipamento_id=None,
                diagnostico="",
                solucao="",
                status="",
                prioridade="",
                custo_total=0
            )
            ordem_repo.deletar(ordem)

        elif op == "0":
            break


def main():
    menu_principal()


if __name__ == "__main__":
    main()