from menus.mainmenu import MainMenuScreen
from menus.splash import SplashScreen
import os
os.system("cls")

splashScreen = SplashScreen()
splashScreen.show()

menuScreen = MainMenuScreen()

menuScreen.show()