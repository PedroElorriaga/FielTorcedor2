# importações de bibliotecas
from asyncio.windows_events import NULL
from cgitb import text
import imp
import importlib
from turtle import title
import pyautogui
from time import sleep
import re

"""while True:
    sleep(2)
    print(pyautogui.position())"""

# Pegar informações de login do usuário
userInfo = True
while userInfo:
    getUserId = pyautogui.password(
        text='Digite seu Usuário', title='LOGIN', mask='')
    getUserPass = pyautogui.password(text='Digite sua senha', title='LOGIN')

    if len(getUserId) == 0:
        pyautogui.alert(text='Digite seu usuário!', title='ALERT')
        continue

    elif len(getUserPass) == 0:
        pyautogui.alert(text='Digite sua senha!', title='ALERT')
        continue

    else:
        userInfo = False

pyautogui.alert(
    text='Verifique se o  CAPS LOCK está desativado, depois clique em confirmar',
    button='Confirmar')

# Buscar o chrome pela aba de pesquisas e abrir o chrome
pyautogui.press('win')
pyautogui.PAUSE = 2
pyautogui.write('chrome')
pyautogui.PAUSE = 1
pyautogui.press('enter')
pyautogui.PAUSE = 1

# Digitar a URL do fielTorecedor
pyautogui.PAUSE = 0.5
pyautogui.write('fieltorcedor.com.br')
pyautogui.press('enter')


# Fechar anuncio inicial
def closeAd():
    tentativas = True
    while tentativas:
        pyautogui.click(x=1421, y=619)
        try:
            x, y = pyautogui.locateCenterOnScreen('img/closeads.png')
            pyautogui.moveTo(x, y)
            pyautogui.PAUSE = 0.5, pyautogui.click()
            tentativas = False
        except:
            pyautogui.PAUSE = 0.5
            print('CloseAdALERT')


closeAd()


# Entrar na tela de login
def enterLog():
    pyautogui.PAUSE = 0.5
    tentativas = True
    while tentativas:
        try:
            locate = pyautogui.locateCenterOnScreen('img/enterbutton.png')
            pyautogui.click(locate.x, locate.y)
            tentativas = False
        except:
            pyautogui.PAUSE = 0.2


enterLog()


# Digitar as credenciais e passar pelo reCaptcha
def credentialToken(userId, passw):
    tentativas = True
    while tentativas:
        try:
            user = pyautogui.locateCenterOnScreen(
                'img/Userid.png', confidence=0.4)
            pyautogui.moveTo(user.x, user.y), pyautogui.click(
            ), pyautogui.write(userId)
            password = pyautogui.locateCenterOnScreen(
                'img/Passwo.png', confidence=0.4)
            pyautogui.moveTo(password.x, password.y), pyautogui.click()
            pyautogui.write(passw)
            recaptcha = pyautogui.locateCenterOnScreen('img/Recapcha.png')
            pyautogui.click(recaptcha.x, recaptcha.y), sleep(0.3)
            enter = pyautogui.locateCenterOnScreen('img/login.png')
            pyautogui.click(enter.x, enter.y)
            tentativas = False
        except:
            print('TokenALERT')


credentialToken(getUserId, getUserPass)
