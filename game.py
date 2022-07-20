import os

from menus.loadsave import LoadSaveScreen
from menus.questionprompt import QuestionPromptScreen
from utils.colors import *
from utils.saves import load_save

class Game:
    def start(self, fastMode):
        os.system("cls")
        print(Colors.GREEN + "Welcome to the British Parliment Simulator", Colors.RESET)
        loadSaveScreen = LoadSaveScreen()

        self.loadedSave = loadSaveScreen.show()
        os.system("cls")
        questionPrompt = QuestionPromptScreen(self.loadedSave, fastMode)
        while True:
            questionPrompt.show()

    def startFromSaveManager(self, saveFile):
        os.system("cls")
        print(Colors.GREEN + "Welcome to the British Parliment Simulator", Colors.RESET)
        
        self.loadedSave = load_save(saveFile)

        os.system("cls")
        questionPrompt = QuestionPromptScreen(self.loadedSave, False)
        while True:
            questionPrompt.show()