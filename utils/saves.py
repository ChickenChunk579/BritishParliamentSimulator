import json
import random
from utils.colors import Colors
from entities.mp import MP
from entities.pm import PM
from entities.parties import Party
from entities.speaker import Speaker
from utils.loadconfig import load_config

class Save:
    def __init__(self, parties, speaker):
        self.parties = parties
        self.speaker = speaker

def load_save(name):
    f = open(f"./saves/{name}", "r")
    jsonObj = json.loads(f.read())

    parties = []
    speaker = Speaker(jsonObj["speaker"]["name"], jsonObj["speaker"]["age"], jsonObj["speaker"]["surname"])

    for party in jsonObj["parties"]:
        mps = []
        pm = PM(party["pm"]["name"], party["pm"]["age"], party["pm"]["surname"])

        for mp in party["mps"]:
            mps.append(MP(mp["name"], mp["age"], mp["surname"]))

        parties.append(Party(party["name"], mps, pm))

    save = Save(parties, speaker)
    return save

def print_save_info(loadedSave):

    print(Colors.BLUE + "Speaker: " + Colors.RESET)
    print(Colors.GREEN + "     Name: " + loadedSave.speaker.name + Colors.RESET)
    print(Colors.GREEN + "     Age: " + str(loadedSave.speaker.age) + Colors.RESET)
    print(Colors.GREEN + "     Surname: " + loadedSave.speaker.surname  + Colors.RESET)
    print()

    for party in loadedSave.parties:
        print(Colors.BLUE + "Party Name: " + party.name + Colors.RESET)

        print()

        print(Colors.BLUE + "PM: " + Colors.RESET)
        print(Colors.GREEN + "     Name: " + party.pm.name + Colors.RESET)
        print(Colors.GREEN + "     Age: " + str(party.pm.age) + Colors.RESET)
        print(Colors.GREEN + "     Surname: " + party.pm.surname + Colors.RESET)
        print()

        print(Colors.BLUE + "MPS: ")

        for mp in party.mps:
            print()
            print(Colors.BLUE + mp.name + ":" + Colors.RESET)
            print(Colors.GREEN + "     Age: " + str(mp.age) + Colors.RESET)
            print(Colors.GREEN + "     Surname: " + mp.surname + Colors.RESET)
            print()

def generate_random_human(config):
    age = random.randint(config["mpData"]["minAge"], config["mpData"]["maxAge"])
    name = random.choice(config["mpData"]["names"])


def generate_random_save(outputName):
    config = load_config()
