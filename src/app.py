from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen
from minigames.intellect.memory_game.memory_game import MemoryGame

Memory = MemoryGame(1000, 650)
Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)
Signup = SignupScreen(1000, 650) 
Woodcutting = WoodcuttingScreen(1000, 650)
Quiz = QuizGame(1000,650)

currentScreen = Memory

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
        Memory.data = currentScreen.data
        currentScreen = Memory

    elif response == 'intellect':
        Quiz.data = currentScreen.data
        currentScreen = Quiz 

    


        
    elif response == 'stop':
        run = False