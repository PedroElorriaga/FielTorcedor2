from http import server
import pyautogui
from time import sleep


def search_url(url):
    search = True
    while search:
        sleep(0.5)
        try:
            x, y = pyautogui.locateCenterOnScreen('img/Pesquisa.png')
            pyautogui.moveTo(x, y)
            pyautogui.PAUSE = 1
            pyautogui.click()
            pyautogui.PAUSE = 0.5, pyautogui.write(
                url), pyautogui.press('enter')
            search = False
        except:
            pyautogui.alert(text='Não encontrado')


inputUrl = pyautogui.password(text='Digite a URL', title='URL', mask='')
search_url(inputUrl)
