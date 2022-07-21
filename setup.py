import os
import urllib.request

class Colors:
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    REVERSE = "\033[;7m"

class Styles:
    BOLD    = "\033[;1m"
    UNDERLINE    = "\033[;4m"

import win32com.client

print(Colors.BLUE + "Welcome to the British Parliment Simulator Installer." + Colors.RESET)
input("Press enter to continue")
print(Colors.GREEN + "Where do you want to install the simulator? " + Colors.RESET)
loc = input("> ")
print(Colors.GREEN + "Downloading...")
urllib.request.urlretrieve("https://github.com/ChickenChunk579/BritishParliamentSimulator/archive/refs/heads/main.zip", "tmp.zip")
print("Installing...")

import zipfile
with zipfile.ZipFile("tmp.zip", 'r') as zip_ref:
    zip_ref.extractall(loc)

print("Creating shortcuts..." + Colors.RESET)

path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "British Parliment Simulator.lnk")
target = loc + "\BritishParliamentSimulator-main\main.py"
icon = loc + '\BritishParliamentSimulator-main\logo.ico' # not needed, but nice
workingDir = loc + '\BritishParliamentSimulator-main'

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.WindowStyle = 3 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.WorkingDirectory = workingDir
shortcut.save()