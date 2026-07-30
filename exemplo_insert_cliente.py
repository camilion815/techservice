from src.models.cliente import Cliente
from src.repositories.cliente_repository import inserir, listar

def main():
    print("=== TechService - Sistema de Gestão de Assistência Técnica ===")

    cliente = Cliente(
        nome="Cliente Teste",
        email="teste@email.pt",
        telefone="910000000",
        codigo_postal="0000-000"
    )

    cliente = inserir(cliente)
    print(f"Cliente gravado na base de dados. ID: {cliente.id_cliente}")

    print("\nClientes ativos:")
    for item in listar():
        print(item["id_cliente"], item["nome"], item["email"], item["telefone"], item["codigo_postal"])

if __name__ == "__main__":
    main()
