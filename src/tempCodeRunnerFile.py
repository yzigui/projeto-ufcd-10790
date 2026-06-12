from dal.projeto_dal import ProjetoDAL
from bll.projeto_bll import ProjetoBLL
from ui.menu import Menu


dal = ProjetoDAL("src/dados/projetos.json")

bll = ProjetoBLL(dal)

menu = Menu(bll)

menu.iniciar()