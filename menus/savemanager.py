from game import Game
from utils.colors import Colors
import os

class SaveManagerScreen:
    def show(self):
        os.system("cls")
        print(Colors.GREEN + "Save Manager" + Colors.RESET)
        print(Colors.BLUE + "Select the save you want to manage" + Colors.RESET)
        saveFiles = os.listdir("./saves")

        saveNumber = 1

        for saveFile in saveFiles:
            print(Colors.BLUE + f"  {saveNumber}: {saveFile}" + Colors.RESET)
            saveNumber += 1

        saveNum = int(input("> "))

        os.system("cls")
        print(Colors.GREEN + saveFiles[saveNum - 1] + Colors.RESET)
        print(Colors.BLUE + "   1: Load" + Colors.RESET)
        print(Colors.BLUE + "   2: Delete" + Colors.RESET)
        i = int(input("> "))

        if i == 2:
            os.system(f"del .\saves\{saveFiles[saveNum - 1]}")
            self.show()

        if i == 1:
            game = Game()
            game.startFromSaveManager(saveFiles[saveNum - 1])