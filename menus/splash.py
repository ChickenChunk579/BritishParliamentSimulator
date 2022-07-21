import time
import os
from utils.colors import Colors

class SplashScreen:
    def show(self):
        print(Colors.GREEN + """

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─████████████████───██████──██████─████████──████████─██████████████────██████████████─██████████████─██████──██████─████████████───██████████─██████████████─██████████████─
─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░████████░░██───██░░██──██░░██─████░░██──██░░████─██░░██████████────██░░██████████─██████░░██████─██░░██──██░░██─██░░████░░░░██─████░░████─██░░██████░░██─██░░██████████─
─██░░██────██░░██───██░░██──██░░██───██░░░░██░░░░██───██░░██────────────██░░██─────────────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─██░░██─────────
─██░░████████░░██───██░░██████░░██───████░░░░░░████───██░░██████████────██░░██████████─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─██░░██████████─
─██░░░░░░░░░░░░██───██░░░░░░░░░░██─────████░░████─────██░░░░░░░░░░██────██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─██░░░░░░░░░░██─
─██░░██████░░████───██░░██████░░██───────██░░██───────██████████░░██────██████████░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─██████████░░██─
─██░░██──██░░██─────██░░██──██░░██───────██░░██───────────────██░░██────────────██░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─────────██░░██─
─██░░██──██░░██████─██░░██──██░░██───────██░░██───────██████████░░██────██████████░░██─────██░░██─────██░░██████░░██─██░░████░░░░██─████░░████─██░░██████░░██─██████████░░██─
─██░░██──██░░░░░░██─██░░██──██░░██───────██░░██───────██░░░░░░░░░░██────██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████──██████████─██████──██████───────██████───────██████████████────██████████████─────██████─────██████████████─████████████───██████████─██████████████─██████████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""" + Colors.RESET)
        time.sleep(1)
        os.system("cls")