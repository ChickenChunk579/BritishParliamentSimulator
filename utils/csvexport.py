import csv
from utils.loadconfig import load_config
import os

def csv_export(yesDict, noDict, questions, outFile):
    with open(outFile, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["          ", "Yes", "No"])

        for question in questions:
            rowArray = [question]
            rowArray.append(yesDict[question])
            rowArray.append(noDict[question])
            writer.writerow(rowArray)

        if load_config()["openFileWhenComplete"]:
            os.system("start excel ./output.csv")