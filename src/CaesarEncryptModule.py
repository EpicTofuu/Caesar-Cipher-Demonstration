import tkProg
import os
import random
from os.path import exists
from Cipher.CaesarEncrypt import CaesarEncrypt, CaesarEncryptKey

class CaesarEncryptMod:

    def __init__ (self, alphabet):
        self.Name = "Single Layer Encryption"
        self.AlphabetContainer = alphabet

    def EncryptTxt (self):
        # take inputs
        tkProg.ClearScreen()
        path = input ("input path of txt to encrypt")
        tkProg.ClearScreen()
        outPath = input ("input path to folder output to, leave as blank if you want to output to the program directory")
        tkProg.ClearScreen()
        outFileName = input ("What should the name of the file be, leave blank for default name, do not include file extensions")
        key = input ("input the value of the key to encrypt with, leave as blank for a randomly generated key")
        alphabet = self.AlphabetContainer.TakeAlphabets ()  # take the working alphabet
            
        value = "" 

        # read the file and encrypt
        if (exists (path)):     # verify that the file exists
            f = open (path)
            msgs = f.readlines ()

            v = []

            if (key == ""):
                key = random.randrange (len (alphabet))
            
            p = 0
            for msg in msgs:
                v.append (CaesarEncryptKey (msg, int(key), alphabet))
                p += 1
                print (str(round ((p / len(msgs)) * 100, 2)) + "%")
                tkProg.ClearScreen()
        else:
            print ("The file does not exist, please try again")
            return

        # output the file
        T = ""
        if (outFileName == ""):
            T = ("Encryption with key " + key)  
        else:
            T = outFileName
        filepath = os.path.join (outPath, T) + ".txt"
        f = open (filepath, "w")
        for l in v:
            f.writelines (l)
        f.close()

        # letting the user know
        print ("The encrypted message is " + value)
        print ("Key: " + key)
        print ("The file has been written to " + filepath)
        
        return 1
                    
    # add actions to the dictionary
    Actions = dict() 
    Actions ["Encrypt text file"] = EncryptTxt

    