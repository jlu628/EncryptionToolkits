import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '--noconsole',
    '--onefile',
    '--icon=./encr.ico',
    "./main.py"                                       
])