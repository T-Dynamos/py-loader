
import requests

downloadUrl = 'https://omextemplates.content.office.net/support/templates/en-us/tf16402488.dotx'

req = requests.get(downloadUrl)
filename = req.url[downloadUrl.rfind('/')+1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

def download_file(url, filename=''):
    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None
def help():
	print("Use This Syntax")
	print(">>>from py_loader import download_file")
	print(">>>download_file('https://www.example.com/','name.html')")
	print()



