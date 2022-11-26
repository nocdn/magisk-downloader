from signal import signal, SIGINT
import os
import platform
import requests
from external_modules import *


def handler(signal_received, frame):
    # Handling Ctrl+C and exiting gracefully
    print('\nCTRL-C or SIGINT detected. Exiting gracefully...')
    exit(0)


def clear_and_sigint():
    os.system("cls") if 'Windows' in platform.system() else os.system("clear")


### Main program ###
clear_and_sigint
signal(SIGINT, handler)
print("""Choose what you would like to download
[1] Magisk
[2] LSPosed (Zygisk)
[3] Universal auth files
Saved links:""")
read_headers, read_rows = reading_data_csv("saved_links.csv")
for row in range(len(read_rows)):
    name, link = read_rows[row].split(",")
    print(f"[{row+4}] {name}")
print("""
[custom] Add custom URL
[exit] Exit""")
choice = input(">>> ")


if choice == "1":
    # if finding_magisk_file() is not None:
    #     download_choice = input("Magisk already downloaded, do you want to download it again? (y/n) ")
    #     if download_choice.lower() == "y" or download_choice.lower() == "":
    #         download_github("https://api.github.com/repos/topjohnwu/Magisk/releases/latest")
    #     else:
    #         exit(0)
    # else:
    #     download_github("https://api.github.com/repos/topjohnwu/Magisk/releases/latest")
    download_github(
        "https://api.github.com/repos/topjohnwu/Magisk/releases/latest")

elif choice == "2":
    download_github(
        'https://api.github.com/repos/LSPosed/LSPosed/releases/latest')

elif choice == "3":
    download_github_two_releases(
        'https://api.github.com/repos/null-dev/UniversalAuth/releases/latest')

elif int(choice) > 3:
    saved_downloading(choice)

elif choice == "custom":
    custom_downloading()

elif choice == "exit":
    exit()
