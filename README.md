# Portfólio de Dados

> Breve descrição do projeto numa ou duas frases. O que faz a aplicação? Para quem?

Aplicação em Python para registar e gerir projetos de análise de dados, permitindo armazenar informações sobre projetos, ferramentas utilizadas, datas e estado de conclusão.
---

## Informação do Projeto

| Campo            | Detalhe                              |
|------------------|--------------------------------------|
| **Curso**        | UFCD 10790 – Projeto de Programação  |
| **Formando**     | [Yasmim Guimaraes]                |
| **Formador**     | [Carlos Barata]                   |
| **Instituição**  | [IEFP]      |
| **Data de início** | [03/06/2026]                       |
| **Data de entrega** | [dd/mm/aaaa]                      |
| **Versão**       | 1.0                                  |

---

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Como Instalar e Executar](#como-instalar-e-executar)
- [Base de Dados](#base-de-dados)
- [Arquitetura](#arquitetura)
- [Documentação](#documentação)
- [Estado do Projeto](#estado-do-projeto)

---

## Descrição

O Portfólio de Dados é uma aplicação desenvolvida em Python para registar e gerir projetos de análise de dados.

O sistema permite armazenar informações sobre cada projeto, incluindo nome, categoria, descrição, ferramentas utilizadas, datas e estado de conclusão.

- Qual o problema que resolve? Permite organizar projetos de análise de dados num único local, facilitando o acompanhamento da evolução e a construção de um portfólio profissional.
- Quem são os utilizadores? Profissionais da area que desejam organizar os seus projetos.
- Qual a abordagem técnica? 
Aplicação de consola em Python com armazenamento de dados em ficheiro JSON.

---

## Funcionalidades

Lista as principais funcionalidades implementadas:

- [x] Funcionalidade 1 — Adicionar projeto
- [x] Funcionalidade 2 — Listar projetos
- [x] Funcionalidade 3 — Pesquisar projeto
- [x] Funcionalidade 4 — Filtrar projetos
- [x] Funcionalidade 5 — Editar projeto
- [x] Funcionalidade 6 — Remover projeto

> As checkboxes ficam marcadas (`[x]`) à medida que implementas cada funcionalidade.

---

## Estrutura do Repositório

```
projeto_ufcd10790/
│
├── README.md               ← Este ficheiro — apresentação do projeto
├── .gitignore              ← Ficheiros a ignorar pelo Git
│
├── src/                    ← Código fonte Python
│   ├── main.py             ← Ponto de entrada da aplicação
│   ├── dal/                ← Data Access Layer
│   │   └── ...
│   ├── bll/                ← Business Logic Layer
│   │   └── ...
│   └── ui/                 ← Interface com o utilizador
│       └── ...
│
├── sql/                    ← Scripts SQL (opcional)
│   ├── criar_tabelas.sql   ← DDL — criação do esquema
│   └── dados_exemplo.sql   ← Dados iniciais de teste
│
├── docs/                   ← Toda a documentação do projeto
│   ├── relatorio.docx      ← Relatório final do projeto
│   ├── requisitos.xlsx     ← Levantamento de requisitos (RF e RNF)
│   ├── manual_utilizador.docx  ← Manual de utilização da aplicação
│   └── manual_tecnico.docx     ← Manual de instalação e configuração
│
├── assets/                 ← Recursos visuais e apresentação
│   ├── apresentacao.pptx   ← Apresentação final
│   ├── diagrama_arquitetura.png  ← Diagrama de arquitetura do sistema
│   └── diagrama_bd.png          ← Diagrama da base de dados (se aplicável)
│
└── tests/                  ← Testes (opcional mas recomendado)
    └── test_bll.py         ← Testes à camada de negócio
```

---


## Requisitos Técnicos

* Python 3.10 ou superior

Bibliotecas utilizadas:

* `json` — incluída no Python

Não são necessárias instalações adicionais.

---

## Como Instalar e Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/yzigui/projeto-ufcd-10790.git
cd projeto-ufcd-10790
```

### 2. (Opcional) Criar ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Executar a aplicação

```bash
cd src
python main.py
```

---

## Base de Dados

> Preenche esta secção se o projeto usa base de dados.

O projeto utiliza persistência de dados através de um ficheiro JSON.

### Sistema

JSON

### Ficheiro

```text
src/dados/projetos.json
```

### Estrutura

Exemplo de registo:

```json
[
  {
    "nome": "Dashboard de Vendas",
    "categoria": "Vendas",
    "descricao": "Análise de vendas mensais",
    "ferramentas": "Python, Power BI",
    "data_inicio": "01/06/2026",
    "estado": "Concluído",
    "data_conclusao": "15/06/2026"
  }
]
```

---

## Arquitetura

O projeto segue uma arquitetura em três camadas:

```text
┌─────────────────────────────┐
│     UI — Interface          │  Interação com o utilizador
├─────────────────────────────┤
│     BLL — Lógica de Negócio │  Regras e validações
├─────────────────────────────┤
│     DAL — Acesso a Dados    │  Leitura e escrita de dados
├─────────────────────────────┤
│     Ficheiro JSON           │  Persistência dos dados
└─────────────────────────────┘
```

### Responsabilidade de cada camada

**UI (User Interface)**

* Interação com o utilizador
* Menus e apresentação de informação

**BLL (Business Logic Layer)**

* Regras de negócio
* Validações
* Processamento de dados

**DAL (Data Access Layer)**

* Leitura e escrita do ficheiro JSON
* Persistência dos dados

---


---

## Documentação

| Documento                  | Localização                        | Descrição                              |
|----------------------------|------------------------------------|----------------------------------------|
| Relatório do Projeto       | `docs/relatorio.docx`              | Relatório completo do projeto          |
| Levantamento de Requisitos | `docs/requisitos.xlsx`             | Requisitos funcionais e não funcionais |
| Manual do Utilizador       | `docs/manual_utilizador.docx`      | Como usar a aplicação                  |
| Manual Técnico             | `docs/manual_tecnico.docx`         | Instalação e configuração              |
| Apresentação               | `assets/apresentacao.pptx`         | Slides da apresentação final           |

---

## Estado do Projeto

```
## Estado do Projeto

```text
Sessão 1 — Requisitos        ✅ Concluído
Sessão 2 — Arquitetura       ✅ Concluído
Sessão 3 — Desenvolvimento 1 ✅ Concluído
Sessão 4 — Desenvolvimento 2 ✅ Concluído
Sessão 5 — Melhorias         🔄 Em curso
Sessão 6 — Apresentação      ⏳ Pendente
```

---

*UFCD 10790 – Projeto de Programação | 2026*

```

