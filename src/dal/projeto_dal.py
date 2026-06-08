import json


class ProjetoDAL:

    def __init__(self, caminho_ficheiro):
        self.caminho_ficheiro = caminho_ficheiro

    def carregar_projetos(self):
        try:
            with open(self.caminho_ficheiro, "r", encoding="utf-8") as ficheiro:
                return json.load(ficheiro)

        except FileNotFoundError:
            return []

    def guardar_projetos(self, projetos):
        with open(self.caminho_ficheiro, "w", encoding="utf-8") as ficheiro:
            json.dump(projetos, ficheiro, ensure_ascii=False, indent=4)