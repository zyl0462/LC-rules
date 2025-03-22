import requests,sys,time
from datetime import datetime,timezone,timedelta

def get_text(url):
    parts = url.split("/")
    file = parts[-1]
    with requests.get(url, stream= True) as r:
        if r.status_code == 200:
            with open("./Rules/" + file, "wb") as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
            time.sleep(0.1)
            with open("./Rules/" + file, "r",encoding='utf-8') as f:
                return f.read().strip()
        else:
            sys.exit(0)
RULES_URL = ("https://rule.kelee.one/Loon/Apple.list")
get_text(RULES_URL[0])
