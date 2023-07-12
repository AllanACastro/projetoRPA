from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("index.py", base = "Win32GUI")]

packages = ["tkinter", "pandas", "re", "pyautogui", "time", "xlrd", ]
options = {
    'build_exe': {

        'packages': packages,
    },

}

setup(
    name = "ProjetoIrio",
    options = options,
    version = "1.0",
    description = 'fim do CornoJob',
    executables = executables
)