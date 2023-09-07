import os
import random
import ctypes
import time
from win10toast import ToastNotifier

# Notify user at startup
notification = ToastNotifier()
notification.show_toast(
    "Wallpaper Automator", "The script has been executed successfully..!", duration=10
)

# Function to change desktop wallpaper
def change_wallpaper(path):
    """
    Change the desktop wallpaper with images from a specified directory.

    :param path: The directory containing wallpaper images.
    """
    try:
        wallpaper_files = os.listdir(path)

        while True:
            random_wallpaper = random.choice(wallpaper_files)
            wallpaper_path = os.path.join(path, random_wallpaper)

            # Set the wallpaper
            ctypes.windll.user32.SystemParametersInfoA(20, 0, wallpaper_path.encode("utf-8"), 3)

            # Change wallpaper every 15 minutes (900 seconds)
            time.sleep(900)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Define the path to the directory containing wallpaper images
wallpaper_directory_path = r"D:\Python\Projects\scripts\wallpaper\wallpapers"

# Start the wallpaper changer with the specified directory path
change_wallpaper(wallpaper_directory_path)