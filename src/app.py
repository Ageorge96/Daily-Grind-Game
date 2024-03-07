from screen.login import LoginScreen
from screen.main import MainScreen
from screen.signup import SignupScreen
from minigames.intellect.quiz.quiz import QuizGame
from minigames.strength.woodcutting import WoodcuttingScreen
from minigames.strength.running import RunningGameScreen
from minigames.intellect.memory_game.memory_game import MemoryGame

Login = LoginScreen()
Main = MainScreen()
Signup = SignupScreen() 
Woodcutting = WoodcuttingScreen()
RunningGame = RunningGameScreen()
Quiz = QuizGame()
Memory = MemoryGame()

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

    elif response == 'intellect':
        Quiz.data = currentScreen.data
        currentScreen = Quiz 

    elif response == 'stop':
        run = False
