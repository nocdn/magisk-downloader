# Automatic magisk downloader

<h3>This is a simple script to automatically download the latest release of Magisk (and other files)</h3>

<h2>Current features:</h2>
    
    - Uses Github API to get the latest release of Magisk (and a few other reposetories)
        - Through requests module, gets browser_download_url from the JSON
        - Uses requests module again to download the file
        - Writes the downloaded content to a file with the appropriate name
    - Creates a copy of the file with the same name, but with a .zip extention (to flash in android recovery)
    - Checks if the file is already downloaded, and asks if you want to download again
    
    - Calculates hash of file to make sure download is intact
    - Allows for saving custom GitHub links to download
    - At that point, works the same as with Magisk files
    - If multiple of the same files exist, will ask whether you would like to overwrite or enumerate the file
        - Currently works on just the saved links
    
<h2>To-do:</h2>
    
    - Fix overwrite/enumerate when file already downloaded
