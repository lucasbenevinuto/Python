class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, nome, quantidade):
        if codigo in self.produtos:
            print("Produto já existe no estoque.")
        else:
            self.produtos[codigo] = {"nome": nome, "quantidade": quantidade}
            print("Produto adicionado ao estoque.")

    def remover_produto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            print("Produto removido do estoque.")
        else:
            print("Produto não encontrado.")

    def buscar_produto(self, codigo):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
        else:
            print("Produto não encontrado.")

estoque = Estoque()

estoque.adicionar_produto("001", "Camiseta", 10)
estoque.adicionar_produto("002", "Calça", 5)
estoque.adicionar_produto("003", "Tênis", 3)

print("\nBuscar produto:")
estoque.buscar_produto("001")

print("\nRemover produto:")
estoque.remover_produto("002")

print("\nBuscar produto novamente:")
estoque.buscar_produto("002")
