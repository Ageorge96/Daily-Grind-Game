from screen.login import LoginScreen
from screen.main import MainScreen
from minigames.intellect.quiz import QuizGame
from screen.signup import SignupScreen
from minigames.strength.woodcutting import WoodcuttingScreen
from minigames.strength.running import RunningScreen
from screen.main_dummy import MainDummy
import pygame


Quiz = QuizGame()
Login = LoginScreen()
Main = MainScreen()
Signup = SignupScreen() 
Woodcutting = WoodcuttingScreen()
Running = RunningScreen()
Dummy = MainDummy()

currentScreen = Dummy

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

    elif response == 'quiz':
        # Quiz.user = currentScreen.user
        currentScreen = Quiz 

    elif response == 'running':
        # Running.user = currentScreen.user
        currentScreen = Running 
    elif response == 'dummy':
        # Running.user = currentScreen.user
        currentScreen = Dummy 

        
    elif response == 'stop':
        run = False
