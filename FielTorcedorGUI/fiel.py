#importações de bibliotecas
from asyncio.windows_events import NULL
from cgitb import text
import imp
from turtle import title
import pyautogui
from time import sleep

"""while True:
    sleep(2)
    print(pyautogui.position())"""

#Pegar informações de login do usuário
userInfo = True
while userInfo:
    getUserId = pyautogui.password(text='Digite seu Usuário', title='LOGIN', mask='')
    getUserPass = pyautogui.password(text='Digite sua senha', title='LOGIN')

    if len(getUserId) == 0:
        pyautogui.alert(text='Digite seu usuário!', title='ALERT')
        continue

    elif len(getUserPass) == 0:
        pyautogui.alert(text='Digite sua senha!', title='ALERT')
        continue

    else:
        userInfo = False

pyautogui.alert(text='Verifique se o  CAPS LOCK está desativado, depois clique em confirmar', button='Confirmar')
#Buscar o chrome pela aba de pesquisas
pyautogui.press('win')
pyautogui.PAUSE= 0.8
pyautogui.write('chrome')
pyautogui.PAUSE = 1
#Abrir o chrome
pyautogui.press('enter')
pyautogui.PAUSE = 1
#Digitar a URL do fielTorecedor
pyautogui.click(x=611, y=75)
pyautogui.PAUSE = 0.5
pyautogui.write('fieltorcedor.com.br')
pyautogui.press('enter')
#Fechar anuncio inicial
sleep(1.5)
pyautogui.click(x=1848, y=200)
#Entrar na tela de login
pyautogui.click(x=1665, y=248)
#Digitar as credenciais e passar pelo reCaptcha
pyautogui.click(x=1010, y=427)
pyautogui.write(getUserId)
pyautogui.PAUSE = 0.5
pyautogui.click(x=1360, y=545)
pyautogui.write(getUserPass)
pyautogui.click(x=793, y=665)
sleep(2.5)
pyautogui.click(x=1421, y=619)
#