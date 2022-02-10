import os
import random
import ctypes
import time
from win10toast import ToastNotifier

# notifying at the startup
for_notification = ToastNotifier()
for_notification.show_toast(
    "Wallpaper Automator", "The script has been executed successfully..!", duration=10
)


"""------Main code begins------"""


def wallomator(path):

    try:
        # list of all the wallpapers in the folder
        list_wall = os.listdir(path)

        # perfroming iteration so that, the wallpaper gets keep on changing in every t seconds
        for i in range(len(list_wall)):

            # choosing a random wallpaper
            random_wallpaper = random.choice(list_wall)

            # getting the location of the randomly choosen wallpaper
            random_wallpaper = os.path.join(path, random_wallpaper)

            # image decoding
            final_wallpaper = bytes(random_wallpaper, "utf-8")

            # setting the wallpaper
            ctypes.windll.user32.SystemParametersInfoA(20, 0, final_wallpaper, 3)

            # specifying the time to change the wallpaper in n seconds
            t = 900
            time.sleep(t)
        return "Script Executed Successfully..!"
    except:
        print("Some error occured..!")


# current path of all the wallpapers (you gotta put your path to the directory of wallpapers)
path = r"D:\Python\Projects\scripts\wallpaper\wallpapers"
wallomator(path)
