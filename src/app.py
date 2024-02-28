from screen.login import LoginScreen
from screen.main import MainScreen
import pygame

Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)

currentScreen = Login

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        data = currentScreen.data
        currentScreen = Main
        currentScreen.data = data
    
    elif response == 'stop':
        run = False