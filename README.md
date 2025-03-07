# automatic magisk downloader

> [!IMPORTANT]  
> this project is now archived, as I do not use magisk

> a simple script to automatically download the latest release of Magisk (and other files)

### Current Features:

- Uses the GitHub API to get the latest release of Magisk (and a few other repositories)
    - Through the `requests` module, gets the `browser_download_url` from the JSON response.
    - Uses the `requests` module again to download the file.
    - Writes the downloaded content to a file with the appropriate name.
- Creates a copy of the file with the same name, but with a `.zip` extension (to flash in Android recovery).
- Checks if the file is already downloaded, and asks if you want to download it again.

- Calculates the hash of the file to ensure the download is intact.
- Allows for saving custom GitHub links to download.
- At that point, it works the same as with Magisk files.
- If multiple files with the same name exist, it will ask whether you would like to overwrite or enumerate the file.
    - Currently, this only works on the saved links.

#### To-do:

- Fix overwrite/enumerate functionality when the file is already downloaded.
