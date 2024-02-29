from screen.login import LoginScreen
from screen.main import MainScreen
from screen.games.quiz.quiz import QuizGame

Quiz = QuizGame(1000,650)
Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)

currentScreen = Quiz

run = True

while run:
    response = currentScreen.render()
    if response == 'main':
        Main.data = currentScreen.data
        currentScreen = Main
    
    elif response == 'stop':
        run = False