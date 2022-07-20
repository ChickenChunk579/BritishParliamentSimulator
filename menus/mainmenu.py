from menus.options import OptionsScreen
from menus.savemanager import SaveManagerScreen
from utils.colors import *
import sys
from game import Game
from menus.createsave import CreateSaveScreen
import os

class MainMenuScreen:
    def show(self):
        print(Colors.GREEN + "Welcome to British Parliment Simulator!" + Colors.RESET)
        print(Colors.BLUE + "   1: Play" + Colors.RESET)
        print(Colors.BLUE + "   2: Play (Fast Mode)" + Colors.RESET)
        print(Colors.BLUE + "   3: Options" + Colors.RESET)
        print(Colors.BLUE + "   4: Save Manager" + Colors.RESET)
        print(Colors.BLUE + "   5: Quit" + Colors.RESET)
        print(Colors.BLUE + "   6: Save Random" + Colors.RESET)

        number = int(input("> "))

        if number == 1:
            game = Game()
            game.start(False)

        if number == 2:
            game = Game()
            game.start(True)

        if number == 3:
            optionsScreen = OptionsScreen()
            optionsScreen.show()

        if number == 4:
            saveManagerScreen = SaveManagerScreen()
            saveManagerScreen.show()

        if number == 5:
            sys.exit()

        os.system("cls")
        self.show()