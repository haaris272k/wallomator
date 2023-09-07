# Wallpaper Changer Script

Automate the process of changing your desktop wallpaper using this Python script. Below are instructions for different methods to execute the script on your system.

## Usage

### Method 1: Direct Execution

1. **Execute the Main Script**: Run the script by double-clicking the provided batch (.bat) file. It will operate in the background, continuously changing your wallpaper.

### Method 2: Startup Configuration

1. **Configure .vbs Startup Script**:
   - Open the Registry Editor by pressing `Win + R`, typing `regedit`, and pressing Enter.
   - Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.
   - Create a new String Value, assign a name (e.g., "WallpaperChanger"), and set its value to the full path of your .vbs script.
   - The script will automatically run at system startup.

### Method 3: Task Scheduler

1. **Use Task Scheduler**:
   - Open the Task Scheduler by searching for it in the Windows Start Menu.
   - Create a new task and configure it to run your script using the provided batch file.
   - Set your preferred trigger (e.g., daily, on login) for the task.
   - The script will execute according to your scheduled task.

### Method 4: Convert to Executable

1. **Convert to Executable**:
   - You can convert the Python script into an executable (.exe) file using tools like PyInstaller or cx_Freeze.
   - Once converted, you can run the executable directly without relying on Python.

**Note: Please ensure that you update the file paths within the script to match your system's configuration.**

## Customization

Customize the script by editing the settings within the script file. Here are some common customizations:

- **Change Wallpaper Directory**: Modify the directory path in the script to point to your wallpaper images.
- **Adjust Wallpaper Change Frequency**: Change the time interval or triggers for wallpaper changes within the script.
- **Add Your Own Wallpapers**: Add or remove wallpaper images in the specified directory.
