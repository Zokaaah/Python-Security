from bs4 import BeautifulSoup
import requests
#obj site recebendo conteudo da requisição http do site 
site = requests.get("http://dbobreakdown.com.br/dbobreak/").content

soup = BeautifulSoup(site, 'html.parser')
#obj soup baixando do site o html


print(soup.prettify())
#transforma Html em string e o print exibe o html