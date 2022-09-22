# Automatic magisk downloader

<h3>This is a simple script to automatically download the latest release of Magisk</h3>

<h2>Current features:</h2>
    
    - Uses Github API to get the latest release of Magisk
        - Through requests module, gets browser_download_url from the JSON
        - Uses requests module again to download the file
        - Writes the downloaded content to a file with the appropriate name
    - Creates a copy of the file with the same name, but with a .zip extention (to flash in android recovery)
    - Calculates hash of file to make sure download is intact
    
    
<h2>To-do:</h2>
    
    - Checks if the file is already downloaded
