class Estoque:

    def __init__(self):
        self.produtos = []

    def ordenar(self):
        self.produtos.sort(key=lambda p: p.codigo)

    def cadastrar(self, produto):

        if self.buscar_codigo(produto.codigo):
            print("Código já cadastrado.")
            return

        self.produtos.append(produto)
        self.ordenar()

    def remover(self, codigo):

        produto = self.buscar_codigo(codigo)

        if produto:
            self.produtos.remove(produto)
            print("Produto removido.")
        else:
            print("Produto não encontrado.")

    def editar(self, codigo, nome, categoria, preco, quantidade):

        produto = self.buscar_codigo(codigo)

        if produto:
            produto.nome = nome
            produto.categoria = categoria
            produto.preco = preco
            produto.quantidade = quantidade

    def buscar_codigo(self, codigo):

        inicio = 0
        fim = len(self.produtos) - 1

        while inicio <= fim:

            meio = (inicio + fim) // 2

            if self.produtos[meio].codigo == codigo:
                return self.produtos[meio]

            if codigo < self.produtos[meio].codigo:
                fim = meio - 1
            else:
                inicio = meio + 1

        return None

    def buscar_nome(self, nome):

        resultado = []

        for produto in self.produtos:

            if nome.lower() in produto.nome.lower():
                resultado.append(produto)

        return resultado

    def registrar_venda(self, codigo, quantidade):

        produto = self.buscar_codigo(codigo)

        if not produto:
            print("Produto não encontrado.")
            return

        if produto.quantidade < quantidade:
            print("Estoque insuficiente.")
            return

        produto.quantidade -= quantidade

        print("Venda registrada com sucesso.")

    def listar(self):

        for produto in self.produtos:
            print(produto)

    def listar_categoria(self, categoria):

        for produto in self.produtos:

            if produto.categoria.lower() == categoria.lower():
                print(produto)

    def estoque_baixo(self, limite):

        for produto in self.produtos:

            if produto.quantidade < limite:
                print(produto)

    def maior_preco(self):

        if self.produtos:
            return max(self.produtos, key=lambda p: p.preco)

    def menor_preco(self):

        if self.produtos:
            return min(self.produtos, key=lambda p: p.preco)