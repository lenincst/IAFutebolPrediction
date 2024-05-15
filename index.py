from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Crie uma instância do Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

base1 = "#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.Box.Flex.ggRYVx.cQgcrM.sc-d8bc48b6-1.kYWPFe > div.Box.clAhaB.sc-d8bc48b6-2.eYMsrH > div.Box.kZzrBS > div > div.sc-4430bda6-4.dtXRIp > div > div.sc-dhKdcB.bOsUiC > div >"
seletor1 = "#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.Box.Flex.ggRYVx.cQgcrM.sc-d8bc48b6-1.kYWPFe > div.Box.clAhaB.sc-d8bc48b6-2.eYMsrH > div.Box.kZzrBS > div > div.sc-4430bda6-4.dtXRIp > div > div.Box.Flex.eSXzoW.MHPeY > div.Box.Flex.ggRYVx.gaIyWq > div.Box.klGMtt.sc-4430bda6-5.hHaqvO > div > button"
seletor2 = "#__next > main > div > div.fresnel-container.fresnel-greaterThanOrEqual-mdMin > div > div.Box.Flex.ggRYVx.cQgcrM.sc-d8bc48b6-1.kYWPFe > div.Box.clAhaB.sc-d8bc48b6-2.eYMsrH > div.Box.kZzrBS > div > div.sc-4430bda6-4.dtXRIp > div > div.Box.Flex.eSXzoW.MHPeY > div.Box.Flex.ggRYVx.gaIyWq > div.Box.klGMtt.sc-4430bda6-5.hHaqvO > div > div > div > div:nth-child(1) > ul > li.DropdownItem.biIPch"

# Lista de URLs para cada ano
urls = [
    'https://www.sofascore.com/tournament/football/brazil/brasileirao-serie-a/325#id:58766',  # URL para 2024
    'https://www.sofascore.com/tournament/football/brazil/brasileirao-serie-a/325#id:48982', # URL para 2023
    # Adicione as URLs para os outros anos aqui...
]


for url in urls:
# Navegue até o site
    driver.get(url)
    time.sleep(2)
    
    try:   
# Busque o nome do campeonato
        campeonato = driver.find_element(By.CSS_SELECTOR, 'h2.Text.jtCOc').text
        print(f"{campeonato}")
    except NoSuchElementException:
        print("Erro ao buscar o nome do campeonato.")
        
    try:
# Busque o ano do campeonato
        ano = driver.find_element(By.CSS_SELECTOR, 'div.Text.gXUapN').text
        #print(f"{ano}")
    except NoSuchElementException:
        print("Erro ao buscar o ano do campeonato.")
        
# Busque o nome do time
    for i in range(3, 23):
        try:
            nome = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div.Box.ljKzDM > div > div').text            
            #print(f"{nome} - {nome}")
        except NoSuchElementException:
            print(f"Erro ao buscar nome do time")
            
# Busque a quantidade de partida do time
        try:
            partidas = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div:nth-child(4) > bdi > div').text            
            #print(f"{nome} - {partidas}")
        except NoSuchElementException:
            print(f"Erro ao buscar partida do time {nome}")
            
# Busque a posição do time
        try:
            posicao = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div:nth-child(1) > div').text
            #print(f"{nome} - {posicao}")
        except NoSuchElementException:
            print(f"Erro ao buscar a posição do time {nome}")
            
#Busque o número de vitórias do time
        try:
            vitorias = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div:nth-child(5) > bdi > div').text
            #print(f"{nome} - {vitorias}")
        except NoSuchElementException:
            print(f"Erro ao buscar as vitorias do time {nome}")
        
# Busque o número de empates do time
        try:
            empates = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div:nth-child(6) > bdi > div').text
            #print(f"{nome} - {empates}")
        except NoSuchElementException:
            print(f"Erro ao buscar os empates do time {nome}")
            
# Busque o número de derrotas do time
        try:
            derrotas = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div:nth-child(7) > bdi > div').text
            #print(f"{nome} - {derrotas}")
        except NoSuchElementException:
            print(f"Erro ao buscar as derrotas do time {nome}")
        
        except NoSuchElementException:
            print(f"!!ERRO!!")
            
# Busque o número de pontos do time         
        try:
            pontuacao = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child({i}) > div > div:nth-child(10) > bdi > div').text
            #print(f"{nome} - {pontuacao}")
        except NoSuchElementException:
            print(f"Erro ao buscar a pontuação do time {nome}")
            
# Busque a média de gol no campeonato       
        try:
            mediagol = driver.find_element(By.CSS_SELECTOR, f'{base1} a:nth-child(3) > div > div:nth-child(8) > bdi > div').text
            gols_marcados, gols_sofridos = mediagol.split(":")  # Separa os gols marcados e sofridos
            print(f"{nome} - Marcados: {gols_marcados}, Sofridos: {gols_sofridos}")
        except NoSuchElementException:
            print(f"Erro ao buscar a média de gols do time {nome}")
        
        
        except NoSuchElementException:
            print(f"!!ERRO!!")
            
# Feche o navegador quando terminar
driver.quit()

#a:nth-child(3) > div > div:nth-child(8) > bdi > div