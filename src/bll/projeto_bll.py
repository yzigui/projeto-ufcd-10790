class ProjetoBLL:

    CATEGORIAS = [
        "Vendas",
        "Marketing",
        "Finanças",
        "Recursos Humanos",
        "Logística",
        "Educação",
        "Saúde",
        "Outro"
    ]

    def __init__(self, dal):
        self.dal = dal

    def listar_categorias(self):
        return self.CATEGORIAS

    def adicionar_projeto(self, nome, categoria, descricao, ferramentas, data_inicio, concluido, data_conclusao=""):
        if not nome.strip():
            raise ValueError("O nome do projeto é obrigatório.")

        if categoria not in self.CATEGORIAS:
            raise ValueError("Categoria inválida.")

        if not descricao.strip():
            raise ValueError("A descrição é obrigatória.")

        if not ferramentas.strip():
            raise ValueError("As ferramentas utilizadas são obrigatórias.")

        if not data_inicio.strip():
            raise ValueError("A data de início é obrigatória.")

        if concluido.upper() == "S":
            estado = "Concluído"

            if not data_conclusao.strip():
                raise ValueError("A data de conclusão é obrigatória para projetos concluídos.")

        elif concluido.upper() == "N":
            estado = "Em Desenvolvimento"
            data_conclusao = ""

        else:
            raise ValueError("Resposta inválida. Use S ou N.")

        projeto = {
            "nome": nome,
            "categoria": categoria,
            "descricao": descricao,
            "ferramentas": ferramentas,
            "data_inicio": data_inicio,
            "estado": estado,
            "data_conclusao": data_conclusao
        }

        projetos = self.dal.carregar_projetos()
        projetos.append(projeto)
        self.dal.guardar_projetos(projetos)

        return projeto
    
    def listar_projetos(self):
        return self.dal.carregar_projetos()
    
    def pesquisar_projeto(self, termo):
        projetos = self.dal.carregar_projetos()

        resultados = []

        for projeto in projetos:
            if termo.lower() in projeto["nome"].lower():
                resultados.append(projeto)

        return resultados
    
    def filtrar_por_categoria(self, categoria):
        projetos = self.dal.carregar_projetos()

        resultados = []

        for projeto in projetos:
            if projeto["categoria"] == categoria:
                resultados.append(projeto)

        return resultados

    def filtrar_por_estado(self, estado):
        projetos = self.dal.carregar_projetos()

        resultados = []

        for projeto in projetos:
            if projeto["estado"] == estado:
                resultados.append(projeto)

        return resultados