import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from bll.projeto_bll import ProjetoBLL


class ProjetoDALMock:
    def __init__(self):
        self.projetos = []

    def carregar_projetos(self):
        return self.projetos

    def guardar_projetos(self, projetos):
        self.projetos = projetos


def criar_bll():
    dal = ProjetoDALMock()
    bll = ProjetoBLL(dal)
    return bll, dal


def test_adicionar_projeto_valido():
    bll, dal = criar_bll()

    projeto = bll.adicionar_projeto(
        "Dashboard de Vendas",
        "Vendas",
        "Análise de vendas mensais",
        "Python, Power BI",
        "01/06/2026",
        "S",
        "15/06/2026"
    )

    assert projeto["nome"] == "Dashboard de Vendas"
    assert projeto["categoria"] == "Vendas"
    assert projeto["estado"] == "Concluído"
    assert len(dal.carregar_projetos()) == 1

    print("✅ test_adicionar_projeto_valido passou")


def test_adicionar_projeto_em_desenvolvimento():
    bll, dal = criar_bll()

    projeto = bll.adicionar_projeto(
        "Análise de Clientes",
        "Marketing",
        "Análise do comportamento dos clientes",
        "Python",
        "01/06/2026",
        "N"
    )

    assert projeto["estado"] == "Em Desenvolvimento"
    assert projeto["data_conclusao"] == ""

    print("✅ test_adicionar_projeto_em_desenvolvimento passou")


def test_nome_vazio():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("", "Vendas", "Descrição", "Python", "01/06/2026", "N")
        print("❌ test_nome_vazio falhou")
    except ValueError:
        print("✅ test_nome_vazio passou")


def test_categoria_invalida():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("Projeto Teste", "Categoria Errada", "Descrição", "Python", "01/06/2026", "N")
        print("❌ test_categoria_invalida falhou")
    except ValueError:
        print("✅ test_categoria_invalida passou")


def test_descricao_vazia():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("Projeto Teste", "Vendas", "", "Python", "01/06/2026", "N")
        print("❌ test_descricao_vazia falhou")
    except ValueError:
        print("✅ test_descricao_vazia passou")


def test_ferramentas_vazias():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("Projeto Teste", "Vendas", "Descrição", "", "01/06/2026", "N")
        print("❌ test_ferramentas_vazias falhou")
    except ValueError:
        print("✅ test_ferramentas_vazias passou")


def test_data_inicio_vazia():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("Projeto Teste", "Vendas", "Descrição", "Python", "", "N")
        print("❌ test_data_inicio_vazia falhou")
    except ValueError:
        print("✅ test_data_inicio_vazia passou")


def test_concluido_invalido():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("Projeto Teste", "Vendas", "Descrição", "Python", "01/06/2026", "X")
        print("❌ test_concluido_invalido falhou")
    except ValueError:
        print("✅ test_concluido_invalido passou")


def test_data_conclusao_obrigatoria():
    bll, dal = criar_bll()

    try:
        bll.adicionar_projeto("Projeto Teste", "Vendas", "Descrição", "Python", "01/06/2026", "S", "")
        print("❌ test_data_conclusao_obrigatoria falhou")
    except ValueError:
        print("✅ test_data_conclusao_obrigatoria passou")


def test_pesquisar_projeto():
    bll, dal = criar_bll()

    bll.adicionar_projeto("Dashboard de Vendas", "Vendas", "Descrição", "Python", "01/06/2026", "N")
    bll.adicionar_projeto("Análise de Clientes", "Marketing", "Descrição", "Python", "01/06/2026", "N")

    resultados = bll.pesquisar_projeto("vendas")

    assert len(resultados) == 1
    assert resultados[0]["nome"] == "Dashboard de Vendas"

    print("✅ test_pesquisar_projeto passou")


def test_filtrar_por_categoria():
    bll, dal = criar_bll()

    bll.adicionar_projeto("Projeto 1", "Vendas", "Descrição", "Python", "01/06/2026", "N")
    bll.adicionar_projeto("Projeto 2", "Marketing", "Descrição", "Python", "01/06/2026", "N")

    resultados = bll.filtrar_por_categoria("Vendas")

    assert len(resultados) == 1
    assert resultados[0]["categoria"] == "Vendas"

    print("✅ test_filtrar_por_categoria passou")


def test_filtrar_por_estado():
    bll, dal = criar_bll()

    bll.adicionar_projeto("Projeto 1", "Vendas", "Descrição", "Python", "01/06/2026", "N")
    bll.adicionar_projeto("Projeto 2", "Marketing", "Descrição", "Python", "01/06/2026", "S", "15/06/2026")

    resultados = bll.filtrar_por_estado("Concluído")

    assert len(resultados) == 1
    assert resultados[0]["estado"] == "Concluído"

    print("✅ test_filtrar_por_estado passou")


def test_editar_projeto():
    bll, dal = criar_bll()

    bll.adicionar_projeto("Projeto Antigo", "Vendas", "Descrição", "Python", "01/06/2026", "N")

    projeto_editado = bll.editar_projeto(
        0,
        "Projeto Novo",
        "Marketing",
        "Nova descrição",
        "Python, Power BI",
        "02/06/2026",
        "S",
        "20/06/2026"
    )

    assert projeto_editado["nome"] == "Projeto Novo"
    assert projeto_editado["categoria"] == "Marketing"
    assert projeto_editado["estado"] == "Concluído"

    print("✅ test_editar_projeto passou")


def test_editar_projeto_indice_invalido():
    bll, dal = criar_bll()

    try:
        bll.editar_projeto(0, "Projeto", "Vendas", "Descrição", "Python", "01/06/2026", "N")
        print("❌ test_editar_projeto_indice_invalido falhou")
    except IndexError:
        print("✅ test_editar_projeto_indice_invalido passou")


def test_remover_projeto():
    bll, dal = criar_bll()

    bll.adicionar_projeto("Projeto Teste", "Vendas", "Descrição", "Python", "01/06/2026", "N")

    projeto_removido = bll.remover_projeto(0)

    assert projeto_removido["nome"] == "Projeto Teste"
    assert len(dal.carregar_projetos()) == 0

    print("✅ test_remover_projeto passou")


def test_remover_projeto_indice_invalido():
    bll, dal = criar_bll()

    try:
        bll.remover_projeto(0)
        print("❌ test_remover_projeto_indice_invalido falhou")
    except IndexError:
        print("✅ test_remover_projeto_indice_invalido passou")


def test_obter_estatisticas():
    bll, dal = criar_bll()

    bll.adicionar_projeto("Projeto 1", "Vendas", "Descrição", "Python", "01/06/2026", "N")
    bll.adicionar_projeto("Projeto 2", "Marketing", "Descrição", "Python", "01/06/2026", "S", "15/06/2026")
    bll.adicionar_projeto("Projeto 3", "Vendas", "Descrição", "Python", "01/06/2026", "S", "20/06/2026")

    estatisticas = bll.obter_estatisticas()

    assert estatisticas["total"] == 3
    assert estatisticas["concluidos"] == 2
    assert estatisticas["em_desenvolvimento"] == 1
    assert estatisticas["categorias"]["Vendas"] == 2
    assert estatisticas["categorias"]["Marketing"] == 1

    print("✅ test_obter_estatisticas passou")


if __name__ == "__main__":
    testes = [
        test_adicionar_projeto_valido,
        test_adicionar_projeto_em_desenvolvimento,
        test_nome_vazio,
        test_categoria_invalida,
        test_descricao_vazia,
        test_ferramentas_vazias,
        test_data_inicio_vazia,
        test_concluido_invalido,
        test_data_conclusao_obrigatoria,
        test_pesquisar_projeto,
        test_filtrar_por_categoria,
        test_filtrar_por_estado,
        test_editar_projeto,
        test_editar_projeto_indice_invalido,
        test_remover_projeto,
        test_remover_projeto_indice_invalido,
        test_obter_estatisticas
    ]

    for teste in testes:
        teste()

    print(f"\nTotal de testes executados: {len(testes)}")
    print("Todos os testes foram concluídos com sucesso.")