from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen
from minigames.strength.running import RunningGameScreen

Login = LoginScreen()
Main = MainScreen()
Signup = SignupScreen() 
Woodcutting = WoodcuttingScreen()
RunningGame = RunningGameScreen()
Quiz = QuizGame()

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

    elif response == 'woodcutting':
        Woodcutting.data = currentScreen.data
        currentScreen = Woodcutting
    
    elif response == 'running':
        RunningGame.data = currentScreen.data
        currentScreen = RunningGame

    elif response == 'intellect':
        Quiz.data = currentScreen.data
        currentScreen = Quiz 

        
    elif response == 'stop':
        run = False
