import requests,sys,time
from datetime import datetime,timezone,timedelta

def get_text(url):
    with requests.get(url, stream= True) as r:
        if r.status_code == 200:
            with open("./Rules/tmp", "wb") as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
            time.sleep(0.1)
            with open("./Rules/tmp", "r",encoding='utf-8') as f:
                return f.read().strip()
        else:
            sys.exit(0)
############################################################  
############################################################
AD_URL = ("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Advertising/Advertising.list",
          "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Advertising/Advertising_Domain.list",
          "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Advertising/Advertising_MITM.plugin"
         )
tmp_set = set([i for i in get_text(AD_URL[1]).split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set = set()
for i in tmp_set:
    j = ''
    if i.startswith('.'):
        j = 'DOMAIN,' + i[1:]
    else:
        j = 'DOMAIN,' + i
    reject_set.add(j)
reject_text = '\n'.join(sorted(reject_set))
with open("./Rules/reject.txt", "w",encoding='utf-8') as f:
    f.write(reject_text)
    
