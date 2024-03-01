from screen.login import LoginScreen
from screen.main import MainScreen
from screen.signup import SignupScreen

Login = LoginScreen(1000, 650)
Main = MainScreen(1000, 650)
Signup = SignupScreen(1000, 650) 

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
        
    elif response == 'stop':
        run = False