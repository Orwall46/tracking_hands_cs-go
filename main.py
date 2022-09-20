import keyboard
import pymem
import time 
from pymem import process
from offsets import *


_process = pymem.Pymem("csgo.exe")
_client = pymem.process.module_from_name(_process.process_handle, "client.dll").lpBaseOfDll


def main():
    while True:
        try:
            if keyboard.is_pressed('space'):
                print("YES")
        except pymem.exception.MemoryReadError as ex:
            print(ex)


if __name__ == "__main__":
    main()