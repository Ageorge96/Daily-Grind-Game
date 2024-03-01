from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.strength.woodcutting import WoodcuttingScreen

Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)
Woodcutting = WoodcuttingScreen(1000, 650)

currentScreen = Login

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        Main.data = currentScreen.data
        currentScreen = Main

    elif response == 'strength':
        Woodcutting.data = currentScreen.data
        currentScreen = Woodcutting

    elif response == 'stop':
        run = False