from dal.projeto_dal import ProjetoDAL

dal = ProjetoDAL("src/dados/projetos.json")

projetos = dal.carregar_projetos()
print("Projetos carregados:", projetos)

projetos.append({
    "nome": "Projeto Teste",
    "categoria": "Vendas",
    "descricao": "Teste da DAL",
    "ferramentas": "Python",
    "data_inicio": "08/06/2026",
    "estado": "Em Desenvolvimento",
    "data_conclusao": ""
})

dal.guardar_projetos(projetos)

print("Projeto guardado com sucesso!")