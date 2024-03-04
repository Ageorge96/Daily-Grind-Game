from screen.login import LoginScreen
from screen.main import MainScreen
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen
from minigames.strength.running import RunningGameScreen
Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)
Signup = SignupScreen(1000, 650) 
Woodcutting = WoodcuttingScreen(1000, 650)
RunningGame = RunningGameScreen(1000,650)


currentScreen = Login

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        Main.data = currentScreen.data
        currentScreen = Main

    elif response == 'signup':
        currentScreen = Signup
    
    elif response == 'login':
        currentScreen = Login

    elif response == 'strength':
        Woodcutting.data = currentScreen.data
        currentScreen = Woodcutting
    
    elif response == 'running':
        RunningGame.data = currentScreen.data
        currentScreen = RunningGame

        
    elif response == 'stop':
        run = False