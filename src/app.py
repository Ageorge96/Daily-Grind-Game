import lib.screen
import screen.main
import screen.second
import types

Main = lib.screen.Screen(1000, 650)
Main.render = types.MethodType(screen.main.render, Main)

Second = lib.screen.Screen(1000, 650)
Second.render = types.MethodType(screen.second.render, Second)

currentScreen = Main

if currentScreen.render() == 'second':
    data = currentScreen.data
    currentScreen = Second
    currentScreen.data = data
    currentScreen.render()