from lib2to3.pgen2.token import OP
import warnings
warnings.filterwarnings('ignore')

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import os
import pandas as pd



# ============================================================================================================================================

lista_geral = []

def resetar_dicionario():
    dictionary = {
        'url': 0,

        'vin': 0,
        'marca': 0,
        'veiculo': 0,
        'ano': 0,
        'cat1': 0,
        'cat2': 0,
        'cat3': 0,
        'cat4': 0,

        'nome': 0,
        'codigo': 0,
        'texto': 0
    }
    return dictionary

dictionary = resetar_dicionario()

def salvar_excel(lista_geral, nome):
    if '/' in nome:
        nome = nome.replace('/', '')
    try:
        nome = nome.replace('"', '')
    except:
        pass

    try:
        df = pd.DataFrame(lista_geral)
        df.to_csv(f'./bases/{nome}.csv', index=False, encoding='utf-8')
    except ValueError:
        df_caso_de_erro = pd.DataFrame.from_dict(lista_geral, orient='index')
        df_caso_de_erro = df_caso_de_erro.transpose()
        df_caso_de_erro = df_caso_de_erro.explode('codigo')
        df_caso_de_erro.to_csv(f'./bases/{nome}.csv', index=False)

# ============================================================================================================================================



# ============================================================================================================================================

def get_infos():
    #script pronto - text, codigo:
    try:
        try:

            check = driver.find_element_by_xpath('//div[@class="B1ZOni84Q4_Yx7mcZ7zKp"]')

            categorias = len(driver.find_elements_by_xpath('//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li'))
            aux = driver.find_element_by_xpath('//div[@class="tnvYZzmJ-jmbyZ9kNPryT _2btyhDfbjoNwKel2Ew_Mmf _2DOJ7JD_9Z1Xej6XwlAZvf"]')

            nome_lista = []
            codigo_lista = []
            for categoria in range(1, categorias+1):
                for categoria_li in range(1, 10):
                    try:
                        codigo = aux.find_element_by_xpath(f'//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li[{categoria}]/div[2]/ul/li[{categoria_li}]//div[@class="KbFygPgMlJ7jl5s21RJPI _1YwnP4Z5J3grA6c0wGSvnF"]').text
                        nome = aux.find_element_by_xpath(f'//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li[{categoria}]/div[1]/div/div/div/span').text

                        nome_lista.append(nome)
                        codigo_lista.append(codigo)

                        dictionary['nome'] = nome_lista
                        dictionary['codigo'] = codigo_lista
                    except NoSuchElementException:
                        pass
            aux_ano = [elem.find_element_by_xpath('div[2]').text if elem.find_element_by_xpath('div[1]').text == "Year" else "" for elem in driver.find_elements_by_xpath('//li[@class="_1aQVewIy8-bOC25Ti2Wsxl"]')]
            aux_vin = [elem.find_element_by_xpath('div[2]').text if elem.find_element_by_xpath('div[1]').text == "VIN / FRAME" else "" for elem in driver.find_elements_by_xpath('//li[@class="_1aQVewIy8-bOC25Ti2Wsxl"]') ]


            dictionary['marca'] = driver.find_element_by_xpath('//h1[@class="_3CVGOzNwYm3aWZcBrVcWx"]/p').text
            dictionary['vin'] = [vin for vin in aux_vin if vin != ''][0]
            dictionary['ano'] = [ano for ano in aux_ano if ano != ''][0]
            
        except NoSuchElementException:

            check = driver.find_element_by_xpath('//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li/div[2]')

            categorias = len(driver.find_elements_by_xpath('//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li'))
            aux = driver.find_element_by_xpath('//div[@class="tnvYZzmJ-jmbyZ9kNPryT _2btyhDfbjoNwKel2Ew_Mmf _2DOJ7JD_9Z1Xej6XwlAZvf"]')

            nome_lista = []
            codigo_lista = []
            for categoria in range(1, categorias+1):
                for categoria_li in range(1, 10):
                    try:
                        codigo = aux.find_element_by_xpath(f'//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li[{categoria}]/div[2]/ul/li[{categoria_li}]//div[@class="KbFygPgMlJ7jl5s21RJPI _1YwnP4Z5J3grA6c0wGSvnF"]').text
                        nome = aux.find_element_by_xpath(f'//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li[{categoria}]/div[1]/div/div/div/span').text

                        nome_lista.append(nome)
                        codigo_lista.append(codigo)

                        dictionary['nome'] = nome_lista
                        dictionary['codigo'] = codigo_lista
                    except NoSuchElementException:
                        pass


            aux_ano = [elem.find_element_by_xpath('div[2]').text if elem.find_element_by_xpath('div[1]').text == "Year" else "" for elem in driver.find_elements_by_xpath('//li[@class="_1aQVewIy8-bOC25Ti2Wsxl"]')]

            aux_vin = [elem.find_element_by_xpath('div[2]').text if elem.find_element_by_xpath('div[1]').text == "VIN / FRAME" else "" for elem in driver.find_elements_by_xpath('//li[@class="_1aQVewIy8-bOC25Ti2Wsxl"]') ]


            dictionary['marca'] = driver.find_element_by_xpath('//h1[@class="_3CVGOzNwYm3aWZcBrVcWx"]/p').text
            dictionary['vin'] = [vin for vin in aux_vin if vin != ''][0]
            dictionary['ano'] = [ano for ano in aux_ano if ano != ''][0]
            
    except NoSuchElementException:

        esperar_elemento_carregar()

        categorias = len(driver.find_elements_by_xpath('//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li'))
        aux = driver.find_element_by_xpath('//div[@class="tnvYZzmJ-jmbyZ9kNPryT _2btyhDfbjoNwKel2Ew_Mmf _2DOJ7JD_9Z1Xej6XwlAZvf"]')

        nome_lista = []
        codigo_lista = []
        for categoria in range(1, categorias+1):
            for categoria_li in range(1, 10):
                try:
                    codigo = aux.find_element_by_xpath(f'//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li[{categoria}]/div[2]/ul/li[{categoria_li}]//div[@class="KbFygPgMlJ7jl5s21RJPI _1YwnP4Z5J3grA6c0wGSvnF"]').text
                    nome = aux.find_element_by_xpath(f'//ul[@class="_3v42nw3VuuL9niLqM2FkLE"]/li[{categoria}]/div[1]/div/div/div/span').text

                    nome_lista.append(nome)
                    codigo_lista.append(codigo)

                    dictionary['nome'] = nome_lista
                    dictionary['codigo'] = codigo_lista
                except NoSuchElementException:
                    pass

        aux_ano = [elem.find_element_by_xpath('div[2]').text if elem.find_element_by_xpath('div[1]').text == "Year" else "" for elem in driver.find_elements_by_xpath('//li[@class="_1aQVewIy8-bOC25Ti2Wsxl"]')]

        aux_vin = [elem.find_element_by_xpath('div[2]').text if elem.find_element_by_xpath('div[1]').text == "VIN / FRAME" else "" for elem in driver.find_elements_by_xpath('//li[@class="_1aQVewIy8-bOC25Ti2Wsxl"]') ]


        dictionary['marca'] = driver.find_element_by_xpath('//h1[@class="_3CVGOzNwYm3aWZcBrVcWx"]/p').text
        dictionary['vin'] = [vin for vin in aux_vin if vin != ''][0]
        dictionary['ano'] = [ano for ano in aux_ano if ano != ''][0]

    esperar_elemento_carregar()

    try:
        buttons = aux.find_elements_by_xpath('//button[@class="_3WUo0QW-jq7ej3P0zmFZRX"]')

        button_lista = []
        for button in buttons:
            sleep(1.5)
            button.click()
            texto_button = button.find_element_by_xpath('//div[@class="B1ZOni84Q4_Yx7mcZ7zKp"]/div').text
            button_lista.append(texto_button.split('\n'))
        dictionary['texto'] = button_lista


        while len(dictionary['nome']) > len(dictionary['texto']):
            dictionary['texto'].append(0)
        while len(dictionary['nome']) < len(dictionary['texto']):
            dictionary['texto'].pop()
    except:
         pass

    return None

# ============================================================================================================================================



# ============================================================================================================================================

def esperar_elemento_carregar():
    #sleep(3.5)
    sleep(3.5)
    return None

# ============================================================================================================================================



# ============================================================================================================================================

try: # linux
    EXECUTABLE_PATH = os.getcwd() + str('/geckodriver')
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
except: #windows
    firefox_options = Options()
    #firefox_options.add_argument("--headless")
    EXECUTABLE_PATH = os.getcwd() + str('/geckodriver.exe')
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH, options=firefox_options)

#url_inicial = 'https://www.parts-catalogs.com/us/demo/#/groups?catalogId=toyota&carId=20b1dd5e990e15eb990815c66888c010&q=9brb29btxd2020094&criteria=d4%2a9BRB29BTXD2020094%21c16f6b53%24481W%7DZ00%5E3%3CFA10%3E1H6'
#url_inicial = "https://www.parts-catalogs.com/us/demo/#/groups?catalogId=toyota&carId=d72cce7ccf782cbce9ef28288705d13d&q=9BRBD48E8C2534336&criteria=41%2a9BRBD48E8C2534336%21c16f6b53%24487W%3CLA12%3E1E7"
#url_inicial = "https://www.parts-catalogs.com/us/demo#/groups?catalogId=bmw&carId=2ddf12ac84c7f991ab51838314407c3d&q=WBA1A1105EJ658563&criteria=e2%2aWBA1A1105EJ658563~1378144288%21c16f6b53%7D1A11%5E61%3C20130900" #automatic
#url_inicial = "https://www.parts-catalogs.com/us/demo#/groups?catalogId=hyundai&carId=7a40c15fa6a613f5743ffd65d33265f8&q=KMHJN81DP8U897992&criteria=ea%2aKMHJN81DP8U897992%7BW5%7CF7%7C6%7C1%7CC%7C%7C%7C%7C%7C~20080312%21c16f6b53%2477c9f9273693dc7cf39f98d8ba670ab9%7D358dce1d900d6106bc62d5c9bf75c87d%5E1%3C01%28W5,02%28F7,03%286,04%281,05%28C,DT%28L,WT%281%3E0"
url_inicial = "https://www.parts-catalogs.com/us/demo#/groups?catalogId=mitsubishi&carId=5255b75f5768880445aad7e34113b040&q=JMYLRN34WWZ800158&criteria=92%2aJMYLRN34WWZ800158~1998021%21c16f6b53%241993121%7D2000113%5EA75A%3C35H%3ES17"
driver.get(url_inicial)

# ============================================================================================================================================



# ============================================================================================================================================

RED_BEGIN = '\033[41m'
BLUR_BEGIN = '\033[44m'
GREEN_COLOR = '\033[42m'
YELLOW_COLOR = '\033[43m'

END_COLOR = '\033[0m'

# ============================================================================================================================================

sleep(5)

esperar_elemento_carregar()
ul1 = driver.find_element_by_class_name('_22r-aP-9FoHZ7xmDD2tOmg')
lista1 = len(ul1.find_elements_by_tag_name('li'))
esperar_elemento_carregar()

contador = 0
for a in range(7, lista1+1): #1

    driver.get(url_inicial)
    
    sleep(8.5)
    
    veiculo = driver.find_element_by_xpath('//p[@class="_3Lq4fcn4TzG6Y7NrRWi-DP"]').text    

    try:
        #encontrar elemento
        esperar_elemento_carregar()
        xpath1 = f"/html/body/div/div/div/div/section/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/ul/li[{a}]"
        driver_item = driver.find_element_by_xpath(xpath1)

        #saber onde ele se encontra
        print("1° categoria: " + RED_BEGIN + f"{driver_item.text}" + END_COLOR)
        categoria1 = driver_item.text
        dictionary['cat1'] = categoria1

        #verificar se existe categorias
        esperar_elemento_carregar()
        svg_existe = driver_item.find_element_by_class_name('XNLxut0x5WycKiNrTph-5')
        driver_item.click()
        
        # salvar checkpoint
        sleep(5)
        url2 = driver.current_url
        
        # salvar lista se tiver categorias
        esperar_elemento_carregar()
        ul2 = driver.find_element_by_class_name('_22r-aP-9FoHZ7xmDD2tOmg') 
        lista2 = len(ul2.find_elements_by_tag_name('li'))
        esperar_elemento_carregar()
        
        for b in range(1, lista2+1): #2
            
            #print(b)

            driver.get(url2)

            esperar_elemento_carregar()

            try:
                #encontrar elemento
                esperar_elemento_carregar()
                xpath2 = f"/html/body/div/div/div/div/section/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[5]/ul/li[{b}]" 
                driver_item2 = driver.find_element_by_xpath(xpath2)

                #saber onde ele se encontra
                print("2° categoria: " + BLUR_BEGIN + f"{driver_item2.text}" + END_COLOR)
                categoria2 = driver_item2.text
                dictionary['cat2'] = categoria2

                #verificar se existe categorias
                esperar_elemento_carregar()
                svg_existe2 = driver_item2.find_element_by_class_name('XNLxut0x5WycKiNrTph-5')
                driver_item2.click()

                # salvar checkpoint
                sleep(5)
                url3 = driver.current_url

                #salvar lista se tiver categorias
                esperar_elemento_carregar()
                ul3 = driver.find_element_by_class_name('_22r-aP-9FoHZ7xmDD2tOmg')
                lista3 = len(ul3.find_elements_by_tag_name('li'))
                esperar_elemento_carregar()

                for c in range(1, lista3+1): #3

                    esperar_elemento_carregar()

                    driver.get(url3)

                    esperar_elemento_carregar()

                    try:   
                        #encontrar elemento
                        esperar_elemento_carregar()                                 
                        xpath3 = f"/html/body/div/div/div/div/section/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[5]/ul/li[{c}]"
                        driver_item3 = driver.find_element_by_xpath(xpath3)

                        #saber onde ele se encontra
                        print("3° categoria: " + GREEN_COLOR + f"{driver_item3.text}" + END_COLOR)
                        categoria3 = driver_item3.text
                        dictionary['cat3'] = categoria3

                        #verificar se existe categorias
                        esperar_elemento_carregar()
                        svg_existe = driver_item3.find_element_by_class_name('XNLxut0x5WycKiNrTph-5')
                        driver_item3.click()

                        # salvar checkpoint
                        sleep(5)
                        url4 = driver.current_url


                        #salvar lista se tiver categorias
                        esperar_elemento_carregar()
                        ul4 = driver.find_element_by_class_name('_22r-aP-9FoHZ7xmDD2tOmg')
                        lista4 = len(ul4.find_elements_by_tag_name('li'))
                        esperar_elemento_carregar()
                        for d in range(1, lista4+1): #4

                            driver.get(url4)

                            esperar_elemento_carregar()

                            try:
                                #encontrar elemento 
                                esperar_elemento_carregar()
                                xpath4 = f"/html/body/div/div/div/div/section/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[5]/ul/li[{d}]"
                                driver_item4 = driver.find_element_by_xpath(xpath4)

                                #saber onde ele se encontra
                                print("4° categoria: " + YELLOW_COLOR + f"{driver_item4.text}" + END_COLOR)
                                categoria4 = driver_item4.text
                                dictionary['cat4'] = categoria4

                                #verificar se existe categorias
                                esperar_elemento_carregar()
                                svg_existe = driver_item4.find_element_by_class_name('XNLxut0x5WycKiNrTph-5')
                                driver_item4.click()

                                # salvar checkpoint
                                sleep(5)
                                url5 = driver.current_url

                                #salvar lista se tiver categorias
                                esperar_elemento_carregar()
                                ul = driver.find_element_by_class_name('_22r-aP-9FoHZ7xmDD2tOmg')
                                lista5 = len(ul.find_elements_by_tag_name('li'))
                                esperar_elemento_carregar()

                            except NoSuchElementException:
                                contador += 1

                                driver_item4.click()
                                esperar_elemento_carregar()
                                get_infos()

                                dictionary['cat1'] = categoria1
                                dictionary['cat2'] = categoria2
                                dictionary['cat3'] = categoria3
                                dictionary['cat4'] = categoria4
                                
                                dictionary['url'] = driver.current_url
                                dictionary['veiculo'] = veiculo

                                esperar_elemento_carregar()

                                if '/' in categoria4:
                                    categoria4 = categoria4.replace('/', '')

                                salvar_excel(dictionary, f'{categoria4}_{str(contador)}')
                                dictionary = resetar_dicionario()

                                #print('CHEGOU NO FINAL!')

                    except NoSuchElementException:
                        contador += 1

                        driver_item3.click()
                        esperar_elemento_carregar()
                        get_infos()

                        dictionary['cat1'] = categoria1
                        dictionary['cat2'] = categoria2
                        dictionary['cat3'] = categoria3

                        dictionary['url'] = driver.current_url
                        dictionary['veiculo'] = veiculo

                        if '/' in categoria3:
                            categoria3 = categoria3.replace('/', '')

                        esperar_elemento_carregar()

                        salvar_excel(dictionary, f'{categoria3}_{str(contador)}')
                        dictionary = resetar_dicionario()

                        #print('CHEGOU NO FINAL!')


            except NoSuchElementException:
                contador += 1

                driver_item2.click()
                esperar_elemento_carregar()
                get_infos()

                dictionary['cat1'] = categoria1
                dictionary['cat2'] = categoria2

                dictionary['url'] = driver.current_url
                dictionary['veiculo'] = veiculo

                esperar_elemento_carregar()

                if '/' in categoria2:
                    categoria2 = categoria2.replace('/', '')

                salvar_excel(dictionary, f'{categoria2}_{str(contador)}')
                dictionary = resetar_dicionario()

                #print('CHEGOU NO FINAL!')

    except NoSuchElementException:
        contador += 1

        driver_item.click()
        esperar_elemento_carregar()
        get_infos()
        
        dictionary['cat1'] = categoria1

        dictionary['url'] = driver.current_url
        dictionary['veiculo'] = veiculo

        esperar_elemento_carregar()

        if '/' in categoria4:
            categoria4 = categoria4.replace('/', '')

        salvar_excel(dictionary, f'{categoria1}_{str(contador)}')
        dictionary = resetar_dicionario()

    df = pd.DataFrame(lista_geral)
    df.to_csv('lista_geral.csv', index=False)

