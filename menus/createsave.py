from utils.colors import Colors
import os
import json

class CreateSaveScreen:
    def createHuman(self):
        name = input(Colors.GREEN + "  Name: " + Colors.RESET)
        age = int(input(Colors.GREEN + "  Age: " + Colors.RESET))
        surname = input(Colors.GREEN + "  Surname: " + Colors.RESET)

        return [name, age, surname]

    def show(self):
        os.system("cls")
        print(Colors.BLUE + "Create Save:" + Colors.RESET)
        self.name = input(Colors.GREEN + "  Name: " + Colors.RESET)
        partyCount = int(input(Colors.GREEN + "  Party Count: " + Colors.RESET))

        parties = []

        for i in range(partyCount):
            print(Colors.BLUE + f"Create Party {i + 1}:" + Colors.RESET)
            name = input(Colors.GREEN + "  Name: " + Colors.RESET)
            mpCount = int(input(Colors.GREEN + "  MP Count: ") + Colors.RESET)
            print(Colors.BLUE + "Create PM:" + Colors.RESET)
            pmData = self.createHuman()

            pm = {"name": pmData[0], "age": pmData[1], "surname": pmData[2]}
            mps = []

            for j in range(mpCount):
                print(Colors.BLUE + f"Create MP {j + 1}:" + Colors.RESET)
                mpData = self.createHuman()

                mp = {"name": mpData[0], "age": mpData[1], "surname": mpData[2]}

                mps.append(mp)

            partyData = {"name": name, "pm": pm, "mps": mps}
            parties.append(partyData)

        print(Colors.BLUE + f"Create Speaker:" + Colors.RESET)
        speakerData = self.createHuman()


        speaker = {"name": speakerData[0], "age": speakerData[1], "surname": speakerData[2]}

        finalJSON = {"speaker": speaker, "parties": parties}

        json.dump(finalJSON, open("saves/" + self.name + ".json", "w"))