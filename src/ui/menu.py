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
                
            elif opcao == "3":
                 self.pesquisar_projeto()
                 
            elif opcao == "4":
                 self.filtrar_projetos()
                 
            elif opcao == "5":
                 self.editar_projeto()
                 
            elif opcao == "6":
                 self.remover_projeto()

            else:
                  print("\nErro: opção inválida.")

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
            
    def pesquisar_projeto(self):
        termo = input("Digite o nome ou parte do nome do projeto: ")

        resultados = self.bll.pesquisar_projeto(termo)

        if not resultados:
            print("\nNenhum projeto encontrado.")
            return

        print("\n===== RESULTADOS DA PESQUISA =====")

        for i, projeto in enumerate(resultados, start=1):
            print(f"\nProjeto {i}")
            print(f"Nome: {projeto['nome']}")
            print(f"Categoria: {projeto['categoria']}")
            print(f"Descrição: {projeto['descricao']}")
            print(f"Ferramentas: {projeto['ferramentas']}")
            print(f"Data de início: {projeto['data_inicio']}")
            print(f"Estado: {projeto['estado']}")
            print(f"Data de conclusão: {projeto['data_conclusao']}")
            
    def filtrar_projetos(self):
        print("\n===== FILTRAR PROJETOS =====")
        print("1 - Filtrar por Categoria")
        print("2 - Filtrar por Estado")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            categorias = self.bll.listar_categorias()

            print("\nCategorias:")
            for i, categoria in enumerate(categorias, start=1):
                print(f"{i} - {categoria}")

            try:
                opcao_categoria = int(input("Escolha a categoria: "))
                categoria = categorias[opcao_categoria - 1]

                resultados = self.bll.filtrar_por_categoria(categoria)
                self.mostrar_resultados(resultados)

            except ValueError:
                print("\nErro: escolha um número válido.")

            except IndexError:
                print("\nErro: categoria inválida.")

        elif opcao == "2":
            print("\nEstados:")
            print("1 - Em Desenvolvimento")
            print("2 - Concluído")

            estado_opcao = input("Escolha o estado: ")

            if estado_opcao == "1":
                estado = "Em Desenvolvimento"
            elif estado_opcao == "2":
                estado = "Concluído"
            else:
                print("\nErro: estado inválido.")
                return

            resultados = self.bll.filtrar_por_estado(estado)
            self.mostrar_resultados(resultados)

        else:
            print("\nErro: opção inválida.")
            
    def mostrar_resultados(self, resultados):

        if not resultados:
            print("\nNenhum projeto encontrado.")
            return

        for i, projeto in enumerate(resultados, start=1):
            print(f"\nProjeto {i}")
            print(f"Nome: {projeto['nome']}")
            print(f"Categoria: {projeto['categoria']}")
            print(f"Descrição: {projeto['descricao']}")
            print(f"Ferramentas: {projeto['ferramentas']}")
            print(f"Data de início: {projeto['data_inicio']}")
            print(f"Estado: {projeto['estado']}")
            print(f"Data de conclusão: {projeto['data_conclusao']}")
            
    def editar_projeto(self):
        projetos = self.bll.listar_projetos()

        if not projetos:
            print("\nNenhum projeto registado.")
            return

        print("\n===== EDITAR PROJETO =====")

        for i, projeto in enumerate(projetos, start=1):
            print(f"\nProjeto {i}")
            print(f"Nome: {projeto['nome']}")
            print(f"Categoria: {projeto['categoria']}")
            print(f"Estado: {projeto['estado']}")

        try:
            escolha = int(input("\nDigite o número do projeto que deseja editar: "))

            if escolha < 1 or escolha > len(projetos):
                print("\nErro: projeto inválido.")
                return

            indice = escolha - 1

            while True:
                projetos = self.bll.listar_projetos()
                projeto = projetos[indice]

                print("\nProjeto selecionado:")
                print(f"Nome: {projeto['nome']}")
                print(f"Categoria: {projeto['categoria']}")
                print(f"Descrição: {projeto['descricao']}")
                print(f"Ferramentas: {projeto['ferramentas']}")
                print(f"Data de início: {projeto['data_inicio']}")
                print(f"Estado: {projeto['estado']}")
                print(f"Data de conclusão: {projeto['data_conclusao']}")

                print("\nO que deseja editar?")
                print("1 - Nome")
                print("2 - Categoria")
                print("3 - Descrição")
                print("4 - Ferramentas")
                print("5 - Data de início")
                print("6 - Estado")
                print("0 - Voltar")

                campo = input("Escolha uma opção: ")

                nome = projeto["nome"]
                categoria = projeto["categoria"]
                descricao = projeto["descricao"]
                ferramentas = projeto["ferramentas"]
                data_inicio = projeto["data_inicio"]

                if projeto["estado"] == "Concluído":
                    concluido = "S"
                else:
                    concluido = "N"

                data_conclusao = projeto["data_conclusao"]

                if campo == "0":
                    print("\nVoltando ao menu principal.")
                    break

                elif campo == "1":
                    nome = input("Novo nome: ")

                elif campo == "2":
                    categorias = self.bll.listar_categorias()

                    print("\nCategorias:")
                    for i, cat in enumerate(categorias, start=1):
                        print(f"{i} - {cat}")

                    opcao_categoria = int(input("Escolha a nova categoria: "))
                    categoria = categorias[opcao_categoria - 1]

                elif campo == "3":
                    descricao = input("Nova descrição: ")

                elif campo == "4":
                    ferramentas = input("Novas ferramentas: ")

                elif campo == "5":
                    data_inicio = input("Nova data de início: ")

                elif campo == "6":
                    concluido = input("O projeto foi concluído? (S/N): ")

                    if concluido.upper() == "S":
                        data_conclusao = input("Data de conclusão: ")
                    else:
                        data_conclusao = ""

                else:
                    print("\nErro: opção inválida.")
                    continue

                self.bll.editar_projeto(
                    indice,
                    nome,
                    categoria,
                    descricao,
                    ferramentas,
                    data_inicio,
                    concluido,
                    data_conclusao
                )

                print("\nProjeto editado com sucesso!")

                continuar = input("Deseja modificar outro campo deste projeto? (S/N): ")

                if continuar.upper() != "S":
                    print("\nVoltando ao menu principal.")
                    break

        except ValueError as erro:
            print(f"\nErro: {erro}")

        except IndexError:
            print("\nErro: opção inválida.")
            
    def remover_projeto(self):
        projetos = self.bll.listar_projetos()

        if not projetos:
            print("\nNenhum projeto registado.")
            return

        print("\n===== REMOVER PROJETO =====")

        for i, projeto in enumerate(projetos, start=1):
            print(f"\nProjeto {i}")
            print(f"Nome: {projeto['nome']}")
            print(f"Categoria: {projeto['categoria']}")
            print(f"Estado: {projeto['estado']}")

        try:
            escolha = int(input("\nDigite o número do projeto que deseja remover: "))

            if escolha < 1 or escolha > len(projetos):
                print("\nErro: projeto inválido.")
                return

            indice = escolha - 1

            confirmacao = input(
                "\nTem a certeza que deseja remover este projeto? (S/N): "
            )

            if confirmacao.upper() != "S":
                print("\nRemoção cancelada.")
                return

            projeto = self.bll.remover_projeto(indice)

            print(
                f"\nProjeto '{projeto['nome']}' removido com sucesso!"
            )

        except ValueError:
            print("\nErro: introduza um número válido.")

        except IndexError:
            print("\nErro: projeto inválido.")