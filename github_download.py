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

    if finding_magisk_file() is not None:
        download_choice = input("Magisk already downloaded, do you want to download it again? (y/n) ")
        if download_choice.lower() == "y" or download_choice.lower() == "":
            download_github("https://api.github.com/repos/topjohnwu/Magisk/releases/latest")
        else:
            exit(0)
    else:
        download_github("https://api.github.com/repos/topjohnwu/Magisk/releases/latest")

elif choice == "2":

    download_github('https://api.github.com/repos/LSPosed/LSPosed/releases/latest')

elif choice == "3":

    response = requests.get('https://api.github.com/repos/null-dev/UniversalAuth/releases/latest')
    data = response.json()
    download_url1 = data["assets"][0]["browser_download_url"]
    download_url2 = data["assets"][1]["browser_download_url"]
    github_response1 = requests.get(download_url1)
    github_response2 = requests.get(download_url2)
    text1 = download_url1.split("/")
    text2 = download_url2.split("/")
    filename1 = text1[-1]
    filename2 = text2[-1]
    print(f"Downloading: {filename1}")
    print(f"Downloading: {filename2}")
    open(filename1, "wb").write(github_response1.content)
    open(filename2, "wb").write(github_response2.content)
    print("Downloaded Universal Auth files")
    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()

elif choice == "custom":

    custom_downloading()
    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()

elif choice == "exit":
    exit()
    
elif int(choice) > 3:

    saved_downloading(choice)
    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()

# function that checks if file exists and gives option to ovewrite it or add a number to the end of the file
def check_file_exists(filename):
    if os.path.isfile(filename):
        file_exists = True
        while file_exists:
            print(f"{filename} already exists")
            overwrite = input("Do you want to overwrite it? (y/n) ")
            if overwrite.lower() == "y" or overwrite.lower() == "":
                os.remove(filename)
                file_exists = False
            elif overwrite.lower() == "n":
                file_exists = False
                filename = filename.split(".")
                filename[0] = filename[0] + "1"
                filename = ".".join(filename)
                check_file_exists(filename)
    return filename

# def overwrite_or_numerate(filename):
    