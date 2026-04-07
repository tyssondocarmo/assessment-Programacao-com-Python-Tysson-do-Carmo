# Projeto Final: O Robô da Livraria

> Assessment de Web Scraping da disciplina **Programação com Python**

## Sobre o projeto

Este projeto tem como objetivo criar um pequeno robô em Python capaz de acessar o site [Books to Scrape](http://books.toscrape.com/), coletar informações dos livros exibidos na página principal e gerar um relatório em formato CSV.

O script realiza um fluxo simples de ETL:

- **Extração**: acessa a página da livraria online
- **Transformação**: lê o HTML e extrai título e preço de cada livro
- **Carga**: salva os dados em um arquivo CSV

## Objetivo da atividade

Aplicar, na prática, conceitos fundamentais de Python, como:

- requisições HTTP com `requests`
- leitura de HTML com `BeautifulSoup`
- uso de listas e dicionários
- estruturas de repetição
- escrita de arquivos CSV com a biblioteca nativa `csv`

## Tecnologias utilizadas

| Tecnologia       | Finalidade                        |
| ---------------- | --------------------------------- |
| `Python`         | Linguagem principal do projeto    |
| `requests`       | Realizar a requisição para o site |
| `beautifulsoup4` | Interpretar o HTML da página      |
| `csv`            | Gerar o relatório final em CSV    |

## Estrutura do projeto

```bash
assessment/
├── main.py
├── readme.md
├── requirements.txt
└── relatorio_livros.csv
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/tyssondocarmo/assessment-Programacao-com-Python-Tysson-do-Carmo.git
cd assessment-Programacao-com-Python-Tysson-do-Carmo/
```

### 2. Criar e ativar o ambiente virtual

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o script

```bash
python main.py
```

## O que o script faz

Ao ser executado, o programa:

1. acessa a página principal do site
2. verifica se a conexão foi bem-sucedida
3. converte o HTML em um objeto `BeautifulSoup`
4. encontra os 20 livros exibidos na primeira página
5. extrai o título e o preço de cada livro
6. organiza os dados em uma lista de dicionários
7. gera o arquivo `relatorio_livros.csv`

## Exemplo de dados coletados

| Título               | Preço  |
| -------------------- | ------ |
| A Light in the Attic | £51.77 |
| Tipping the Velvet   | £53.74 |
| Soumission           | £50.10 |

## Arquivo gerado

Após a execução, o projeto cria o arquivo:

```bash
relatorio_livros.csv
```

Com estrutura semelhante a esta:

```csv
titulo,preco
A Light in the Attic,£51.77
Tipping the Velvet,£53.74
Soumission,£50.10
```

## Aprendizados praticados

- manipulação de dados vindos da web
- navegação em estruturas HTML
- organização de dados com Python
- geração de relatórios simples

## Informações acadêmicas

- **Instituição:** Instituto INFNET
- **Disciplina:** Programação com Python
- **Professor:** Tiago Silva
- **Aluno:** Tysson do Carmo

## Licença

Projeto desenvolvido para fins acadêmicos.
