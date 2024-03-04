from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen


Quiz = QuizGame()
Login = LoginScreen()
Main = MainScreen()
Signup = SignupScreen() 
Woodcutting = WoodcuttingScreen()

currentScreen = Main

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

    elif response == 'intellect':
        intellect.data = currentScreen.data
        currentScreen = Quiz 

        
    elif response == 'stop':
        run = False
