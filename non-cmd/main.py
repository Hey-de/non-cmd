# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import sys
from typing import TextIO

from colorama import init, Fore, Back


class NonCmd:
    def __init__(self, args, terminal=False):
        self.args = args[0]
        self.mods = args[1]
        self.is_terminal = terminal
        self.stand_mods = {'UDP': "", 'TCP': "", 'SSH': "", 'Internet': ""}

    def config(self, options):
        for option, value in options.items():
            if option == "use_mods":
                if not value:
                    self.mods = {}
                else:
                    self.mods = value
            elif option == "use_www":
                if value:
                    self.stand_mods = {'UDP': "", 'TCP': "", 'SSH': "", 'Internet': ""}
                else:
                    self.stand_mods = {"Internet": ""}

    def run(self):
        if len(self.args) == 2:
            os.chdir(self.args[1])
        print(Fore.GREEN + "Session was run!")
        if not self.is_terminal:
            for dir in os.getcwd().split("\\"):
                print(Back.YELLOW + Fore.BLACK + dir, end=Fore.GREEN + ">")
            if ".git" in os.listdir(os.getcwd()):
                print(Fore.YELLOW + "~~~Git~~~", end=">")
            if ".idea" in os.listdir(os.getcwd()):
                print(Fore.YELLOW + "&~JetBrains project~&", end=">")
            if "dist" in os.listdir(os.getcwd()):
                print(Fore.YELLOW + "*PyInstaller*", end=">")
            if "__pycache__" in os.listdir(os.getcwd()):
                print(Fore.YELLOW + "#Compilled Python#", end=">")
            cmd = input()
            while cmd != "exit":
                if cmd.split(" ")[0] == "cd":
                    print(Fore.RED + '"cd" command changed to "cd /p" command')
                elif cmd.split(" /p ")[0] == "cd":
                    os.chdir(cmd.split(" /p ")[1])
                    os.system("cd " + cmd.split(" /p ")[1])
                elif cmd == "dir":
                    print(Fore.BLUE + "Folder " + os.getcwd() + " contents:")
                    for dir in os.listdir(os.getcwd()):
                        print(Fore.BLUE + "\t-" + dir)
                elif cmd == "help":
                    print(Fore.BLUE + """Non-cmd
                    It's shell with Windows commands and your OWN commands
                    from modules. You can config me with config.json file
                    and add your Python modules with commands using modules.json.
                    """ + Fore.YELLOW + """Warning: cd command changed to cd /p command""")
                else:
                    os.system(cmd)
                for dir in os.getcwd().split("\\"):
                    print(Back.YELLOW + Fore.BLACK + dir, end=Fore.GREEN + ">")
                if ".git" in os.listdir(os.getcwd()):
                    print(Fore.YELLOW + "~~~Git~~~", end=">")
                if ".idea" in os.listdir(os.getcwd()):
                    print(Fore.YELLOW + "&~JetBrains project~&", end=">")
                if "dist" in os.listdir(os.getcwd()):
                    print(Fore.YELLOW + "*PyInstaller*", end=">")
                if "__pycache__" in os.listdir(os.getcwd()):
                    print(Fore.YELLOW + "#Compilled Python#", end=">")
                cmd = input()


if __name__ == '__main__':
    init(autoreset=True)
    f: TextIO
    print(Back.BLUE + Fore.GREEN + """Welcome to non-cmd Shell!
    Python has been already installed because non-cmd cannot run without Python""")
    with open("modules.json") as f:
        mods = json.load(f)
    is_t = "y" == input(Fore.BLACK + "Run as terminal[y/n] ")
    session = NonCmd([sys.argv, mods], is_t)
    with open("config.json") as f:
        cfg = json.load(f)
    session.config(cfg)
    print(Back.BLUE + Fore.GREEN + "Running...")
    session.run()
