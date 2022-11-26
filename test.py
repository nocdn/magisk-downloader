if os.path.isfile(filename):
    overwrite_or_enumerate = input(
        f"\033[1m{filename}\033[0m already exists. Would you like to overwrite it or enumerate it? (o/e)\n: ")
    if overwrite_or_enumerate.lower == "o" or overwrite_or_enumerate.lower == "overwrite":
        github_response = requests.get(download_url)
        open(filename, "wb").write(github_response.content)
        print(f"Downloaded: {filename}")
        print("Hash: " + hashing_file(filename))
        temp = input("\nPress \033[1mENTER\033[0m to exit\n")
        exit()
    else:
        filename = filename.split(".")
        filename[0] = filename[0] + "1"
        filename = ".".join(filename)
