import json
from utils.colors import *
from utils.loadconfig import load_config
import random
import time
from utils.pluraliser import pluralise
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

    def get_random_mp(self):
        partyNumber = random.randrange(0, len(self.save.parties))
        mp = random.choice(self.save.parties[partyNumber].mps)
        return mp

    def show(self):
        config = load_config()
        
        #part1 = random.choice(config["questionParts"]["part1"])
        #part2 = random.choice(config["questionParts"]["part2"])
        #part3 = random.choice(config["questionParts"]["part3"])

        category = 1
        if category == 1:
            newConfig = json.load(open("./configs/countries.json", "r"))
            part1 = random.choice(newConfig["part1"])
            part2 = random.choice(newConfig["part2"])
            part3 = random.choice(newConfig["part3"])

        randomMp = self.get_random_mp()
        print(Colors.BLUE + "Question " + str(self.questionNumber) + Colors.RESET)

        question = part1 + " " + part2 + " " + part3

        print(Colors.GREEN + randomMp.name + ": I propose that " + question + Colors.RESET)

        self.questions.append(question)

        if not self.fastMode:
            time.sleep(3)

        yes = 0
        no = 0

        for party in self.save.parties:
            mpCount = len(party.mps)
            for i in range(mpCount):
                rannum = random.randint(0, 1)

                if rannum == 1:
                    yes += 1
                    print(Colors.GREEN + f"{party.mps[i].name} {party.mps[i].surname} voted in favour of the motion." + Colors.RESET)
                else:
                    no += 1
                    print(Colors.RED + f"{party.mps[i].name} {party.mps[i].surname} voted in opposition to the motion." + Colors.RESET)

        if yes > no:
            print(Colors.RED + self.save.speaker.name + ": The motion '" + question + "' has been rejected." + Colors.RESET)
        if no > yes:
            print(Colors.GREEN + self.save.speaker.name + ": The motion '" + question + "' has been rejected." + Colors.RESET)
        if yes == no:
            print(Colors.CYAN + self.save.speaker.name + ": The vote is a draw." + Colors.RESET)

        self.yesDict[question] = yes
        self.noDict[question] = no
        if not self.fastMode:
            time.sleep(3)

        os.system("cls")

        if self.questionNumber == config["questionsPerDay"]:
            csv_export(self.yesDict, self.noDict, self.questions, "output.csv")
            print("Outputed table to output.csv")
            exit()
        self.questionNumber += 1