from utils.colors import *
from utils.loadconfig import load_config
import random
import os
from utils.csvexport import csv_export

class QuestionPromptScreen:
    questionNumber = 1
    questions = []
    yesDict = {}
    noDict = {}

    def __init__(self, save, fastMode):
        self.save = save
        self.fastMode = fastMode

    def show(self):
        config = load_config()
        
        part1 = random.choice(config["questionParts"]["part1"])
        part2 = random.choice(config["questionParts"]["part2"])
        part3 = random.choice(config["questionParts"]["part3"])

        print(Colors.BLUE + "Question " + str(self.questionNumber) + Colors.RESET)

        question = part1 + " " + part2 + " " + part3

        print(Colors.GREEN + question + Colors.RESET)

        self.questions.append(question)

        if not self.fastMode:
            input("Press enter to continue.")

        yes = 0
        no = 0

        for party in self.save.parties:
            mpCount = len(party.mps)
            for i in range(mpCount):
                rannum = random.randint(0, 1)

                if rannum == 1:
                    yes += 1
                else:
                    no += 1

        if yes > no:
            print(Colors.RED + part2 + " will " + part3[:-1] + "." + Colors.RESET)
        if no > yes:
            print(Colors.GREEN + part2 + " will not " + part3[:-1] + "." + Colors.RESET)
        if yes == no:
            print(Colors.CYAN + "Draw" + Colors.RESET)

        self.yesDict[question] = yes
        self.noDict[question] = no
        if not self.fastMode:
            input("Press enter to continue.")

        os.system("cls")

        if self.questionNumber == config["questionsPerDay"]:
            csv_export(self.yesDict, self.noDict, self.questions, "output.csv")
            print("Outputed table to output.csv")
            exit()
        self.questionNumber += 1