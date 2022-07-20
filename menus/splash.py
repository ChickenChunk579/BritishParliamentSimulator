import time
import os
from utils.colors import Colors

class SplashScreen:
    def show(self):
        print(Colors.CYAN + """

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
        time.sleep(0.1)
        os.system("cls")