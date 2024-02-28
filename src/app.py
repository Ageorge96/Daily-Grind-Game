from screen.login import LoginScreen
from screen.main import MainScreen

Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)

currentScreen = Login

if currentScreen.render() == 'second':
    data = currentScreen.data
    currentScreen = Main
    currentScreen.data = data
    currentScreen.render()