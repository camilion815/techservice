from src.repositories.cliente_repository import listar
from src.repositories.cliente_repository import buscar_por_nome, buscar_por_email, buscar_por_codigo_postal
from src.repositories.equipamento_repository import listar_equipamentos, buscar_por_nome, buscar_por_tipo


def main():
    print("=== TechService - Sistema de Gestão de Assistência Técnica ===")

    print("\nClientes ativos:")

    clientes = listar()

    for item in clientes:
        print(
            item["id_cliente"],
            item["nome"],
            item["email"],
            item["telefone"],
            item["codigo_postal"]
        )
        
    print("\nEquipamentos ativos:")

    equipamento = listar_equipamentos()

    for item in equipamento:
        print(
            item["id_equipamento"],
            item["nome"],
            item["tipo"],
            item["descricao"]
        )
        




if __name__ == "__main__":
    main()