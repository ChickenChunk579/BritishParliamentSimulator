from utils.colors import Colors
from utils.saves import *
import os

class LoadSaveScreen:
    def show(self):
        print(Colors.BLUE + "Select your save" + Colors.RESET)

        saveFiles = os.listdir("./saves")

        saveNumber = 1

        for saveFile in saveFiles:
            print(Colors.GREEN + f"  {saveNumber}: {saveFile}" + Colors.RESET)
            saveNumber += 1

        i = int(input("> "))

        loadedSave = load_save(saveFiles[i - 1])

        print(Colors.GREEN + "Save Info:")
        print_save_info(loadedSave)

        isCorrectSave = input("Is this correct? (y/n) ")

        if isCorrectSave == "y":
            return loadedSave
        else:
            return self.show()