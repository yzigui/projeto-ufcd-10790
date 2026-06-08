class Menu:

    def __init__(self, bll):
        self.bll = bll

    def iniciar(self):
        while True:

            print("\n===== PORTFÓLIO DE DADOS =====")
            print("1 - Adicionar Projeto")
            print("2 - Listar Projetos")
            print("3 - Pesquisar Projeto")
            print("4 - Filtrar Projetos")
            print("5 - Editar Projeto")
            print("6 - Remover Projeto")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Funcionalidade ainda não implementada.")