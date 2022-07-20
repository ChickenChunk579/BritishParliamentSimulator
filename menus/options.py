import os
import json
from utils.colors import *

class OptionsScreen:
    def show(self):
        os.system("cls")
        print(Colors.GREEN + "Options" + Colors.RESET)
        print(Colors.BLUE + "   1: Questions Per Day" + Colors.RESET)
        print(Colors.BLUE + "   2: Open Excel when complete" + Colors.RESET)
        print(Colors.BLUE + "   3: Exit" + Colors.RESET)

        i = input("> ")
        if i == "1":
            i = input(Colors.GREEN + "New Value: " + Colors.RESET)
            newConfig = json.load(open("config.json", "r"))
            newConfig["questionsPerDay"] = int(i)
            open("config.json", "w").write(json.dumps(newConfig, indent=4))
            self.show()

        if i == "2":
            i = input(Colors.GREEN + "Y/n? " + Colors.RESET)
            newConfig = json.load(open("config.json", "r"))
            if i == "y":
                newConfig["openFileWhenComplete"] = True
            else:
                newConfig["openFileWhenComplete"] = False

            open("config.json", "w").write(json.dumps(newConfig, indent=4))
            self.show()

        if i == "3":
            os.system("cls")
            return