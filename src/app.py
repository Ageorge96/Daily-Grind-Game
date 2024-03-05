from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen


Quiz = QuizGame(1000,650)
Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)
Signup = SignupScreen(1000, 650) 
Woodcutting = WoodcuttingScreen(1000, 650)

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

    elif response == 'intellect':
        Quiz.user = currentScreen.user
        currentScreen = Quiz 

        
    elif response == 'stop':
        run = False