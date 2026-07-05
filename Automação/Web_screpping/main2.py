import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/'
resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, "html.parser")
    livros_articles = soup.find_all('article', attrs={'class':'product_pod'})
    for livro_article in livros_articles:
        titulo = livro_article.h3.text
        
        preco = livro_article.find('p', attrs={'class':'price_color'}).text
        link = livro_article.find('a')['href']

        print(f'Título: {titulo} - Preço: {preco} - Link: {link}')
else:
    print("Erro ao acessar a página:", resposta.status_code)