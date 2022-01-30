# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
from os import system

system('title Bot de Instagram @jean_carlos.019')
system('color a')
system('cls')
print('-='*30,'\n')
print(' '*14,'Bot de comentarios (Instagram)')
print(' '*19,'By: @jean_carlos.019\n')
print('-='*30)
sleep(4)

def opcao_invalida():
    system('color 4')
    print('-='*30)
    print('Opção inválida! Tente novamente!\n')
    system('pause')

def login_instagram(Driver, usuario, senha):
    campo_usuario = Driver.find_element_by_xpath('//input[@name="username"]')
    campo_usuario.click()
    campo_usuario.clear()
    campo_usuario.send_keys(usuario)

    campo_senha = Driver.find_element_by_xpath('//input[@name="password"]')
    campo_senha.click()
    campo_senha.clear()
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)

def login_facebook(Driver, usuario, senha):
    campo_facebook = Driver.find_element_by_xpath('//button[@type="button"]')
    campo_facebook.click()
    sleep(3)

    campo_usuario = Driver.find_element_by_xpath('//input[@name="email"]')
    campo_usuario.click()
    campo_usuario.clear()
    campo_usuario.send_keys(usuario)

    campo_senha = Driver.find_element_by_xpath('//input[@name="pass"]')
    campo_senha.click()
    campo_senha.clear()
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)

while True:
    system('cls')
    system('color e')
    print('-='*30)
    login = input("Deseja logar pelo Instagram ou pelo Facebook? (I/F) ").strip().upper()[0]
    system('cls')
    
    if login not in 'IF':
        opcao_invalida()
        continue
    
    print('-='*30)
    usuario = input("Digite seu e-mail: ").strip()
    system('cls')
    
    if usuario in '':
        opcao_invalida()
        continue
    
    print('-='*30)
    senha = input('Digite sua senha: (Ela não será salva) ')
    system('cls')
    
    if senha in '':
        opcao_invalida()
        continue
    
    print('-='*30)
    publicacao = input('Digite o link da publicação: ').strip()
    system('cls')
    
    if publicacao in '':
        opcao_invalida()
        continue
    
    print('-='*30)
    comentario = input('Por fim, digite os comentários: (Separe-os por vírgula) ').strip()
    system('cls')
    
    if comentario in '':
        opcao_invalida()
        continue
    break

Driver = webdriver.Edge(executable_path='.//msedgedriver.exe')

Driver.get("https://www.instagram.com")
sleep(3)

if login == 'I':
    login_instagram(Driver, usuario, senha)
elif login == 'F':
    login_facebook(Driver, usuario, senha)

sleep(10)
Driver.get(publicacao)
system('cls')

for i in range(10000):
    try:
        system('color b')
        print(f'Repetição numero {i}')

        # → Divide os comentários em uma lista e escolhe aleátoriamente um índice.
        comentarios = [comentario.split(',')[randint(0, len(comentario.split(', ')))]]
        
        Driver.find_element_by_class_name('Ypffh').click()
        campo_comentario = Driver.find_element_by_class_name('Ypffh')
        campo_comentario.send_keys(comentarios)
        sleep(randint(3, 7))
        Driver.find_element_by_xpath('//button[contains(text(),"Publicar")]').click()
        sleep(randint(4, 8))

        # → Tá meio chato de desviar do bloqueio, uma vez bloqueado, jaera.       
        if len(Driver.find_elements_by_class_name('gxNyb')) > 0:
            print('Um elemento de bloqueio foi encontrado!')
            sleep(randint(8, 25))
            Driver.find_element_by_xpath('//button[contains(text(),"Publicar")]').click()
            if Driver.find_element_by_xpath('//button[contains(text(),"disable")]') == True:
                continue

            #<button class="sqdOP yWX7d    y3zKF" type="submit">Publicar</button> -> aqui fica disable
            #<form class="X7cDz" method="POST">...</form>
    except:
        system('color 4')
        print('Ocorreu um erro! Vamos repetir tudo novamente.')
        continue
