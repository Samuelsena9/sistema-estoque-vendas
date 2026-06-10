from produto import Produto
from estoque import Estoque
from arquivos import salvar, carregar

estoque = Estoque()
estoque.produtos = carregar()

while True:

    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar Produto")
    print("2 - Editar Produto")
    print("3 - Remover Produto")
    print("4 - Buscar por Código")
    print("5 - Buscar por Nome")
    print("6 - Registrar Venda")
    print("7 - Listar Produtos")
    print("8 - Listar por Categoria")
    print("9 - Estoque Baixo")
    print("10 - Salvar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        codigo = int(input("Código: "))
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        if preco <= 0:
            print("Preço inválido.")
            continue

        if quantidade < 0:
            print("Quantidade inválida.")
            continue

        produto = Produto(
            codigo,
            nome,
            categoria,
            preco,
            quantidade
        )

        estoque.cadastrar(produto)

    elif opcao == "2":

        codigo = int(input("Código: "))

        nome = input("Novo nome: ")
        categoria = input("Nova categoria: ")
        preco = float(input("Novo preço: "))
        quantidade = int(input("Nova quantidade: "))

        estoque.editar(
            codigo,
            nome,
            categoria,
            preco,
            quantidade
        )

    elif opcao == "3":

        codigo = int(input("Código: "))
        estoque.remover(codigo)

    elif opcao == "4":

        codigo = int(input("Código: "))

        produto = estoque.buscar_codigo(codigo)

        if produto:
            print(produto)
        else:
            print("Não encontrado.")

    elif opcao == "5":

        nome = input("Nome: ")

        resultado = estoque.buscar_nome(nome)

        for p in resultado:
            print(p)

    elif opcao == "6":

        codigo = int(input("Código: "))
        quantidade = int(input("Quantidade vendida: "))

        estoque.registrar_venda(
            codigo,
            quantidade
        )

    elif opcao == "7":

        estoque.listar()

    elif opcao == "8":

        categoria = input("Categoria: ")
        estoque.listar_categoria(categoria)

    elif opcao == "9":

        limite = int(input("Limite: "))
        estoque.estoque_baixo(limite)

    elif opcao == "10":

        salvar(estoque.produtos)
        print("Dados salvos.")

    elif opcao == "0":

        salvar(estoque.produtos)
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")