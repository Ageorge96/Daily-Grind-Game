from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen
# from minigames.strength.running import RunningGameScreen
from screen.dummy import MainDummy

Login = LoginScreen()
Main = MainScreen()
Signup = SignupScreen() 
Woodcutting = WoodcuttingScreen()
# RunningGame = RunningGameScreen()
Quiz = QuizGame()
dummy = MainDummy()

currentScreen = Login

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        Main.user = currentScreen.user
        currentScreen = Main

    elif response == 'signup':
        currentScreen = Signup
    
    elif response == 'login':
        currentScreen = Login

    elif response == 'strength':
        Woodcutting.user = currentScreen.user
        currentScreen = Woodcutting
    
    # elif response == 'running':
    #     RunningGame.data = currentScreen.data
    #     currentScreen = RunningGame

    elif response == 'intellect':
        Quiz.user = currentScreen.user
        currentScreen = Quiz 

    elif response == 'dummy':
        dummy.user = currentScreen.user
        currentScreen = dummy
        
    elif response == 'stop':
        run = False