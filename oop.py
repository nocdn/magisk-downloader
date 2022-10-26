import requests

class OpenURL:
    
    def download(self, url, filename):
        self.url = url
        self.filename = filename
        self.github_response = requests.get(self.url)
        open(self.filename, "wb").write(self.github_response.content)
        print(f"Downloaded {self.filename}")