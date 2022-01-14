import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


print('')
print('')
print('')
print('Iniciando automação...')
time.sleep(3)
print('')
print('.')
print('.')
print('.')
print('')

def youtube_login():

    email = 'pedrohenriquedefb@gmail.com'
    password = '<12345Pedro1'

    # Navegador
    driver = webdriver.Chrome()
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26feature%3Dsign_in_button%26app%3Ddesktop%26action_handle_signin%3Dtrue%26next%3D%252F&uilel=3&passive=true&service=youtube#identifier')
    driver.maximize_window()

    #login
    driver.find_element_by_id('identifierId').send_keys(email)
    driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
    WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.NAME, "password")))
    driver.find_element_by_name('password').send_keys(password)
    WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d")))
    driver.find_element_by_class_name('VfPpkd-vQzf8d').click()

    
    #WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.ID, "identity-prompt-confirm-button")))
    #driver.find_element_by_id('identity-prompt-confirm-button').click()

    print('Login efetuado com sucesso...')
    time.sleep(3)
    
    urls = []
    comentario = []

    # Importando arquivo txt com os links dos videos.
    with open("urls.txt","r") as arquivo1:
        for line in arquivo1.readlines():
            urls.append(line.strip())
            
    #Importando o arquivo txt com os comentarios.
    with open("comentarios.txt","r",encoding='utf-8') as arquivo2:
        for line in arquivo2.readlines():
            comentario.append(line.strip())
            
    x = 0

    print('Iniciando automação de comentarios...')
    time.sleep(3)

    #Acessando os links do arquivo txt.
    for url in urls:  
        driver.get(url)
        time.sleep(5)
        
        print('')
        print('Curtindo o video...')
        #Clica para dar like no video.
        like_video = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon")
        like_video.click()
        time.sleep(5)

        #Rolando a pagina para baixo.
        web_end = driver.find_element_by_tag_name("body")
        web_end.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

        #Ativando a caixa de comentarios.
        commentBox = driver.find_element_by_id('placeholder-area')
        commentBox.click()
        time.sleep(3)

        print('Comentando...')
        #Digitando o comentario na caixa de texto.
        inputBox =driver.find_element_by_id('contenteditable-root')
        inputBox.send_keys(comentario[x])
        time.sleep(3)

        #Clicando no botão comentar.
        publicar_button = driver.find_element_by_id('submit-button')
        publicar_button.click()
        time.sleep(3)

        print('Curtindo comentario...')
        #Dando click de like no comentario.
        like = driver.find_element_by_id('like-button')
        like.click()
        time.sleep(10)

        x = x+1

        print(f'Comentario({x}) concluido...')



youtube_login()

print('')
print('.')
print('.')
print('.')
print('')
print('Automação concluida com sucesso!')