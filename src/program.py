# SECTION 5

# General Collection
# Do Not Write It Here

import os
import os.path
import argparse
import pickle
import Cipher
import tk

Modules = []    # stores all modules
Actions = []    # stores all actions in modules and the module itself

# TODO maybe use reflection
# import and instantiate each of the modules
from CaesarEncryptModule import CaesarEncryptMod
Modules.append (CaesarEncryptMod())

def Args ():
    """Handles argument parsing"""
    parser = argparse.ArgumentParser(description="Directly run a process from the run command")
    parser.add_argument("ProcessName", metavar="N", type=str, nargs='+', help="The name of the process to run")
    args = parser.parse_args()
    return args

tk.ClearScreen()
print ("Caesar encryption and decryption")
print ()

# display all module actions but also log them into a mega list
n = 1
for mod in Modules:
    for action in mod.Actions:
        print (str (n) + ") " + action)
        Actions.append ((mod.Actions[action], mod))
        n += 1

# TODO add input checking
userin = int (input (""))

# Call the method
Actions[userin - 1][0](Actions[userin - 1][1])

'''
ModulePaths = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
ModulePaths.remove ("program.py")
'''