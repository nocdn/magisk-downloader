from signal import signal, SIGINT
from external_modules import writing_data_csv, reading_data_csv
import hashlib
import os
import shutil
import platform
import requests
import json

def handler(signal_received, frame):
    # Handling any cleanup here
    print('\nCTRL-C or SIGINT detected. Exiting gracefully...')
    exit(0)

def generate_github_link(repo_url):
    return repo_url.replace("github.com", "api.github.com/repos") + "/releases/latest"

def hashing_file(filename_to_hash):
    """
    Hashing a file
    Parameters: filename (string) - the name of the file to be hashed
    """
    sha256_hash = hashlib.sha256()
    with open(filename_to_hash, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
        file.close()
    return sha256_hash.hexdigest()

def check_if_file_exists(filename):
    """
    Checking if a file exists
    Parameters: filename (string) - the name of the file to be checked
    """
    if os.path.isfile(filename):
        return True
    return False

def append_to_file(filename, data_to_write):
    """
    Appending a line to the end of a file
    Parameters: filename (string) - the name of the file to be read
    data_to_write (string) - the line to be appended to the file
    """
    with open(filename, "a+", encoding='utf-8') as file_object:
        file_object.seek(0)
        reading_data = file_object.read(100)
        if len(reading_data) > 0 :
            file_object.write("\n")
        file_object.write(data_to_write)
        file_object.close()

def read_file(filename):
    """
    Opening a file and reading the contents into a variable called 'lines_data'
    Parameters:filename (string) - the name of the file to be read
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines_data = file.readlines()
        file.close()
    return lines_data



signal(SIGINT, handler)
os.system("cls") if 'Windows' in platform.system() else os.system("clear")
print("""Choose what you would like to download
[1] Magisk
[2] LSPosed (Zygisk)
[3] Universal auth files
Saved links:""")
read_headers, read_rows = reading_data_csv("saved_links.txt")
for i in range(len(read_rows)):
    name, link = read_rows[i].split(",")
    print(f"[{i+4}] {name}")
print("""
[custom] Add custom URL
[exit] Exit""")
choice = input(">>> ")
if choice == "1":
    if check_if_file_exists("magisk."):
        download_choice = input("Magisk already downloaded, do you want to download it again? (y/n) ")
        if download_choice.lower() == "y":
            pass
        else:
            exit(0)
    response = requests.get('https://api.github.com/repos/topjohnwu/Magisk/releases/latest')
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    print(f"Downloading: {filename}")

    open(filename, "wb").write(github_response.content)
    print("\nDownloaded Magisk files")
    print("\n")

    print("Hash: " + hashing_file(filename))

    # shutil.copyfile(filename, f"./{filename[:-4]}.zip")

    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()
elif choice == "2":
    response = requests.get('https://api.github.com/repos/LSPosed/LSPosed/releases/latest')
    data = response.json()
    download_url = data["assets"][1]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    print(f"Downloading: {filename}")

    open(filename, "wb").write(github_response.content)
    print("Downloaded LSPosed")
    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()
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
    user_github_url = input("Enter the Github repo URL of the file(s) you would like to download\n: ")
    new_string = generate_github_link(user_github_url)
    print("Downloading...")
    response = requests.get(new_string)
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    open(filename, "wb").write(github_response.content)
    print(f"Downloaded: {filename}")
    save_choice = input("\nWould you like to save this for later? (y/n)\n: ")
    if save_choice == "y":
        name = input("\nWhat do you want to save the file as (to show in the list)?\n: ")
        data_to_save = []
        data_to_save.append(name)
        data_to_save.append(new_string)
        writing_data_csv("saved_links.txt", data_to_save)
        print("\nSaved for later")
    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()
elif choice == "exit":
    exit()
elif int(choice) > 3:
    read_header1, read_rows1 = reading_data_csv("saved_links.txt")
    for i in range(len(read_rows1)):
        name, link = read_rows1[i].split(",")
        if int(choice) == i+4:
            print(f"Downloading: {name}")
            github_raw_data = requests.get(link)
            data = github_raw_data.json()
            download_url = data["assets"][0]["browser_download_url"]
            filename = data["assets"][0]["name"]
            github_response = requests.get(download_url)
            open(filename, "wb").write(github_response.content)
            print(f"Downloaded: {filename}")
            temp = input("\nPress \033[1mENTER\033[0m to exit\n")
            exit()
    print(f"Downloading from: {link[int(choice)-4]}")
    response = requests.get(link[int(choice)-4])
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    open(filename, "wb").write(github_response.content)
    print(f"Downloaded: {filename}")
    temp = input("\nPress \033[1mENTER\033[0m to exit\n")
    exit()
