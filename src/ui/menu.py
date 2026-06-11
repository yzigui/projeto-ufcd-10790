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

            elif opcao == "1":
                self.adicionar_projeto()
            
            elif opcao == "2":
                self.listar_projetos()

            else:
                print("Funcionalidade ainda não implementada.")

    def adicionar_projeto(self):
        try:
            nome = input("Nome do projeto: ")

            print("\nCategorias:")
            categorias = self.bll.listar_categorias()

            for i, categoria in enumerate(categorias, start=1):
                print(f"{i} - {categoria}")

            opcao_categoria = int(input("Escolha a categoria: "))
            categoria = categorias[opcao_categoria - 1]

            descricao = input("Descrição do projeto: ")
            ferramentas = input("Ferramentas utilizadas: ")
            data_inicio = input("Data de início: ")
            concluido = input("O projeto foi concluído? (S/N): ")

            data_conclusao = ""

            if concluido.upper() == "S":
                data_conclusao = input("Data de conclusão: ")

            projeto = self.bll.adicionar_projeto(
                nome,
                categoria,
                descricao,
                ferramentas,
                data_inicio,
                concluido,
                data_conclusao
            )

            print(f"\nProjeto '{projeto['nome']}' adicionado com sucesso!")

        except ValueError as erro:
            print(f"\nErro: {erro}")

        except IndexError:
            print("\nErro: categoria inválida.")
            
    def listar_projetos(self):
        projetos = self.bll.listar_projetos()

        if not projetos:
            print("\nNenhum projeto registado.")
            return

        print("\n===== LISTA DE PROJETOS =====")

        for i, projeto in enumerate(projetos, start=1):
            print(f"\nProjeto {i}")
            print(f"Nome: {projeto['nome']}")
            print(f"Categoria: {projeto['categoria']}")
            print(f"Descrição: {projeto['descricao']}")
            print(f"Ferramentas: {projeto['ferramentas']}")
            print(f"Data de início: {projeto['data_inicio']}")
            print(f"Estado: {projeto['estado']}")
            print(f"Data de conclusão: {projeto['data_conclusao']}")