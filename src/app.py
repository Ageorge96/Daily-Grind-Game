from screen.login import LoginScreen
from screen.main import MainScreen

Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)

currentScreen = Login

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        Main.data = currentScreen.data
        currentScreen = Main
    
    elif response == 'stop':
        run = False