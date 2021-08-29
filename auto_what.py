import pyautogui as pag
import time
import subprocess
import getpass
import wmi

from models.number import Number
from utils.read_data import DataRead
from utils.alarm import Alarm

wp_file_path = "C:\\Users\\" + \
    getpass.getuser() + "\\AppData\\Local\\WhatsApp\\WhatsApp.exe"


def getAddIcon():
    theme = input("Enter whatsapp theme (d/l): ")
    if (theme.lower() == "d" or theme.lower() == "dark"):
        return "images/add_icon_dark.png"

    elif (theme.lower() == "l" or theme.lower() == "light"):
        return "images/add_icon_light.png"

    else:
        print("Invalid Input!")
        exit()


def checkIsWPWorking():

    print("Checking Whatsapp state...")

    f = wmi.WMI()
    is_wp_working = False
    for proc in f.Win32_Process():
        if (proc.Name.lower() == "whatsapp.exe"):
            subprocess.call([wp_file_path])
            is_wp_working = True

    print(is_wp_working)

    if (is_wp_working == False):
        print("whatsapp not working")
        subprocess.call([wp_file_path])
        time.sleep(10)


dr = DataRead()
persons = dr.getNumbersAndNames()
add_icon = "null"

try:
    add_icon = getAddIcon()
    message = input("Enter the message to be sent: ")
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))

    if (hour >= 24):
        raise ValueError("Hour can't more than or equal to 24")
    elif (minute >= 60):
        raise ValueError("Minute can't more than or equal to 60")
except:
    print("Invalid Input!")
    exit()

Alarm().setAlarm(hour, minute)

checkIsWPWorking()

time.sleep(1)

print("Starting...")
print("\n!!!Please don't close your whatsapp!!!\n")

for person in persons:
    try:
        add_icon_x, add_icon_y = pag.locateCenterOnScreen(add_icon)

    except:
        print("Error! Add new message button not found in the screen!")
        exit()

    pag.click(add_icon_x, add_icon_y)

    time.sleep(.2)
    pag.typewrite(person.number)

    time.sleep(.5)
    pag.press("enter")
    pag.press("esc")
    pag.press("esc")

    time.sleep(.3)
    pag.typewrite(person.name + " " + message)

    time.sleep(.2)
    pag.press("enter")


print("Messages are sent...")
