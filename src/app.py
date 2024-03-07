from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen
from minigames.strength.running import RunningGameScreen
Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)
Signup = SignupScreen(1000, 650) 
Woodcutting = WoodcuttingScreen(1000, 650)
RunningGame = RunningGameScreen(1000,650)
Quiz = QuizGame(1000,650)

currentScreen = Login

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        # Main.user = currentScreen.user
        currentScreen = Main

    elif response == 'signup':
        currentScreen = Signup
    
    elif response == 'login':
        currentScreen = Login

    elif response == 'woodcutting':
        # Woodcutting.user = currentScreen.user
        currentScreen = Woodcutting
    
    elif response == 'running':
        RunningGame.data = currentScreen.data
        currentScreen = RunningGame

    elif response == 'intellect':
        Quiz.data = currentScreen.data
        currentScreen = Quiz 

    elif response == 'running':
        # Running.user = currentScreen.user
        currentScreen = Running 
    elif response == 'dummy':
        # Running.user = currentScreen.user
        currentScreen = Dummy 

        
    elif response == 'stop':
        run = False
'''    
    elif response == 'running':
        RunningGame.data = currentScreen.data
        currentScreen = RunningGame
'''