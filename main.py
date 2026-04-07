# PASSO 1: importar as bibliotecas
import csv
import requests
from bs4 import BeautifulSoup

# PASSO 2: guardar o endereço do site em uma variável
url = "http://books.toscrape.com/"

# PASSO 3: fazer a requisição GET para o site
resposta = requests.get(url)

# PASSO 3.1: ajustar a codificação da resposta para UTF-8
resposta.encoding = "utf-8"

# PASSO 4: verificar se a conexão foi bem-sucedida
if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print("Erro ao acessar o site.")
    quit()

# PASSO 5: transformar o HTML da resposta em um objeto BeautifulSoup
soup = BeautifulSoup(resposta.text, "html.parser")

# PASSO 6: imprimir o título da página para testar
print(f"Imprimindo título da página: {soup.title.text}")

# PASSO 7: encontrar todos os artigos que representam livros
livros_html = soup.find_all("article", class_="product_pod")

# PASSO 8: imprimir a quantidade de livros encontrados
print(f"Quantidade de livros encontrados: {len(livros_html)}")

# PASSO 9: criar uma lista vazia para guardar os dados extraídos
dados_extraidos = []

# PASSO 10: percorrer cada livro encontrado no HTML
for livro in livros_html:
    # PASSO 11: encontrar o título do livro no atributo title da tag <a>
    titulo = livro.find("h3").find("a")["title"]

    # PASSO 12: encontrar o preço do livro
    preco = livro.find("p", class_="price_color").text

    # PASSO 13: criar um dicionário com os dados do livro atual
    livro_dados = {
        "titulo": titulo,
        "preco": preco
    }

    # PASSO 14: adicionar o dicionário na lista de dados extraídos
    dados_extraidos.append(livro_dados)

# PASSO 15: imprimir a lista completa no final
for item in dados_extraidos:
    print(item)

# PASSO 16: abrir o arquivo CSV em modo de escrita
with open("relatorio_livros.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    # PASSO 17: criar o gravador do CSV com os nomes das colunas
    gravador = csv.DictWriter(arquivo_csv, fieldnames=["titulo", "preco"])

    # PASSO 18: escrever o cabeçalho do arquivo
    gravador.writeheader()

    # PASSO 19: escrever todas as linhas com os dados dos livros
    gravador.writerows(dados_extraidos)

# PASSO 20: informar que o relatório foi gerado com sucesso
print("Relatório CSV gerado com sucesso!")
