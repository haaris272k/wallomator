@echo off
echo "Executing the Python script to change wallpapers..."

REM Define the full path to your Python script.
REM Modify the path below to match the location of your script.
set SCRIPT_PATH=C:\Users\dir1\dir2\dir3\wallomator\Wallomator\script.py

REM Check if the Python script exists at the specified path.
if not exist "%SCRIPT_PATH%" (
  echo "Error: Python script not found at %SCRIPT_PATH%"
  pause
  exit /b 1
)

REM Run the Python script silently, redirecting output and error to NUL.
python "%SCRIPT_PATH%" > NUL 2>&1

echo "Script execution complete."
pause
