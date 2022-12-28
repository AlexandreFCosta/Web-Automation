from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def find_dolar():
    # abrir navegador
    nav = webdriver.Chrome(
        executable_path='C:\\Users\\alexa\\Downloads\\chromedriver_win32\\chromedriver.exe')
    nav.get('https://www.google.com/')

    #Encontrar barra de pesquisa e digitar a moeda
    element = nav.find_element(By.CLASS_NAME, "gLFyf").send_keys(
        "cotação dolar" + Keys.ENTER)
    
    #Encontrar valor 
    dolar = nav.find_element(
        By.CSS_SELECTOR, "#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt > span.DFlfde.SwHCTb").get_attribute("data-value")

    #Converter a variavel de str para float
    dolar = float(dolar)

    #Formatar o numero
    dolar = round(dolar,2)    

    #Mostrar o valor
    print("Preço atual do dolar: ", dolar)

    nav.quit()



