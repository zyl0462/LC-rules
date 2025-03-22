import requests,sys,time
from datetime import datetime,timezone,timedelta

def get_text(url):
    file = url.split("/")[-1]
    with requests.get(url, stream= True) as r:
        if r.status_code == 200:
            with open("./Rules/" + file, "wb") as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
        else:
            sys.exit(0)

