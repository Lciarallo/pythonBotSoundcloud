from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sclib import SoundcloudAPI, Track, Playlist
import time

# Chave da API do SoundCloud (gerada no site de desenvolvedores do SoundCloud)
client_id = 'SkNjMmSOqCCKdQohdskaTGJvEncaJpga'



url = "https://soundcloud.com/"
busca = "teste"

@given(u'acesso a pagina inicial do soundcloud')
def step_impl(context):
    context.driver.get(url)
    time.sleep(2)

@when(u'realizar a busca do nome da musica')
def step_impl(context):
    caixa_pesquisa = context.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form/input')
    caixa_pesquisa.send_keys(busca)
    caixa_pesquisa.send_keys(Keys.RETURN)
    time.sleep(10)

@when(u'clicar na primeira música')
def step_impl(context):
    # Localiza e clica na primeira música da lista
    primeira_musica = context.driver.find_element(By.XPATH, '(//*[@class="sound__content"])[1]')
    primeira_musica.click()
    time.sleep(5)  # Espera a página carregar

@when(u'obter a URL da música')
def step_impl(context):
    # Obtém a URL da música atualmente reproduzida
    url_musica = context.driver.current_url
    context.url_musica = url_musica  # Armazena a URL para uso posterior

@then(u'devo baixar o a musica em formato .mp3')
def step_impl(context):
    # Use a URL armazenada para baixar a música em formato .mp3 (implementação fictícia)
    print(f"Baixando música de URL: {context.url_musica}")
    # Implemente aqui a lógica para baixar a música em formato .mp3
    # Por exemplo, você pode usar bibliotecas ou ferramentas para fazer o download da música
