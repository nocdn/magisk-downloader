import csv, hashlib, os, requests
from os.path import exists

from requests import request

def writing_data_csv(filename, data_to_write):
    """
    Function to write data to csv file
    Parameters: filename (string) - the name of the file to be read
                data_to_write (string) - the data to be written (or appended) to the file
    """
    file_exists = exists(filename)
    if file_exists is False:
        header = ['name', 'link']
        with open(filename, 'w+', newline="", encoding='utf-8') as writing_file:
            csvwriter1 = csv.writer(writing_file) # 1. create a csvwriter object
            csvwriter1.writerow(header) # 2. write the header
            csvwriter1.writerow(data_to_write) # 3. write the rest of the data
            writing_file.close() # 4. close the file
    else:
        with open(filename, 'a', newline="", encoding='utf-8') as appending_file:
            csvwriter2 = csv.writer(appending_file) # 1. create a csvwriter object
            csvwriter2.writerow(data_to_write) # 2. write the row, without the header
            appending_file.close() # 3. close the file

def reading_data_csv(filename):
    """
    Reads the data from the csv file and returns a header and a list of rows (both as lists)
    Parameters: filename (string) - the name of the file to be read
    """
    if exists(filename) is False:
        with open("saved_links.txt", "w+", encoding='utf-8') as tempFile:
            tempFile.close()
    with open(filename, 'r+', encoding='utf-8') as read_file:
        content = read_file.readlines()
    read_header = content[:1]
    read_rows = content[1:]
    read_file.close()
    if read_rows != []:
        read_header[-1] = read_header[-1].strip()
        for i in range(len(read_rows)):
            read_rows[i] = read_rows[i].strip()
        return read_header, read_rows
    else:
        return read_header, read_rows

def finding_magisk_file():
    """
    Finds the magisk file in the current directory and returns the name of the file
    """
    import os
    files = os.listdir()
    for file in files:
        if file.startswith("Magisk"):
            return file

def generate_github_link(repo_url):
    return repo_url.replace("github.com", "api.github.com/repos") + "/releases/latest"

def check_if_file_exists(filename):
    """
    Checking if a file exists
    Parameters: filename (string) - the name of the file to be checked
    """
    if os.path.isfile(filename):
        return True
    return False

def read_file(filename):
    """
    Opening a file and reading the contents into a variable called 'lines_data'
    Parameters:filename (string) - the name of the file to be read
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines_data = file.readlines()
        file.close()
    return lines_data

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

def download_github(api_url):
    respone = requests.get(api_url)
    if respone.status_code == 200:
        data = respone.json()
        download_url = data["assets"][0]["browser_download_url"]
        github_response = requests.get(download_url)
        text = download_url.split("/")
        filename = text[-1]
        print(f"Downloading {filename}...")
        open(filename, "wb").write(github_response.content)
        print("\nDownloaded successfully!")
        print("Hash: " + hashing_file(filename))

        temp = input("\nPress \033[1mENTER\033[0m to exit\n")
        exit()
    else:
        return f"Error: {respone.status_code}"
    
