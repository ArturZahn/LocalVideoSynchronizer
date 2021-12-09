@REM copy all files from source to compiling_folder (remove old stuff and create folde if needed)
Robocopy .\source .\compiling_folder /MIR /Z

CD ./compiling_folder

@REM compiles the code
pyinstaller .\localvideosynchronizer.py --hidden-import __future__ --hidden-import ctypes --hidden-import comtypes --hidden-import pycaw --hidden-import subprocess --hidden-import win32api --hidden-import pynput --hidden-import pprint --hidden-import requests --hidden-import webbrowser

@REM copy additional files
Robocopy ..\..\assets .\dist\localvideosynchronizer\assets /e /z
Robocopy ..\additional_files .\dist\localvideosynchronizer\ /e /z

rmdir ..\dist /S /Q
move dist\localvideosynchronizer ..\dist
cd ..
rmdir compiling_folder /S /Q

pause