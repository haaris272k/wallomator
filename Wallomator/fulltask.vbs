' Wallpaper Change VBScript
' This VBScript is used to execute a batch script to change wallpapers.

' Create a WScript Shell object for running the batch script.
Set WshShell = CreateObject("WScript.Shell")

' Specify the path to the batch script that changes wallpapers.
' Modify the path below to match the location of your execute.bat file.
BatchScriptPath = "D:\Python\Projects\scripts\wallpaper\execute.bat"

' Run the batch script silently (0), and wait for it to complete (True).
WshShell.Run BatchScriptPath, 0, True

' Clean up the WScript Shell object.
Set WshShell = Nothing

' The script has finished executing the batch file to change wallpapers.