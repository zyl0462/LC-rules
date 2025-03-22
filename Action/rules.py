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
def get_url(url, file):
    with requests.get(url, stream= True) as r:
        if r.status_code == 200:
            with open("./Rules/" + file, "wb") as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
        else:
            sys.exit(0)
############################################################  
############################################################
REJECT_URL = ('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Advertising/Advertising_Domain.list',
          'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Advertising/Advertising.list',
          'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Advertising/Advertising_MITM.plugin'
         )
PROXY_URL = ('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Global/Global_Domain.list',
             ('https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Global/Global.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/GitHub/GitHub.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Google/Google.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/YouTube/YouTube.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Telegram/Telegram.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/TikTok/TikTok.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Twitter/Twitter.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Facebook/Facebook.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Discord/Discord.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Instagram/Instagram.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/GitLab/GitLab.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/Pinterest/Pinterest.list',
             'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Loon/OpenAI/OpenAI.list')
            )
DIRECT_URL = (('https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/ChinaMaxNoMedia/ChinaMaxNoMedia_Domain.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/China/China_Domain.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/Apple/Apple_Domain.list'),
              ('https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/Apple/Apple.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/China/China.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/ChinaIPs/ChinaIPs.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/ChinaMaxNoMedia/ChinaMaxNoMedia.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/ChinaMedia/ChinaMedia.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/WeChat/WeChat.list',
              'https://github.com/blackmatrix7/ios_rule_script/raw/refs/heads/master/rule/Loon/ByteDance/ByteDance.list')
             )

tmp_set = set([i for i in get_text(REJECT_URL[0]).split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set = set()
for i in tmp_set:
    j = ''
    if i.startswith('.'):
        j = 'DOMAIN,' + i[1:]
    else:
        j = 'DOMAIN,' + i
    reject_set.add(j)
tmp_set.clear()
tmp_set = set([i for i in get_text(REJECT_URL[1]).split("\n") if not (i.startswith('#') or i.startswith('!'))])
reject_set.update(tmp_set)
LEN_reject = len(reject_set)
tmp_set.clear()
reject_text = '\n'.join(sorted(reject_set))
with open("./Rules/reject.list", "w",encoding='utf-8') as f:
    f.write(reject_text)
get_url(REJECT_URL[2], 'reject.plugin')
del reject_set,reject_text

tmp_set = set([i for i in get_text(PROXY_URL[0]).split("\n") if not (i.startswith('#') or i.startswith('!'))])
proxy_set = set()
for i in tmp_set:
    j = ''
    if i.startswith('.'):
        j = 'DOMAIN,' + i[1:]
    else:
        j = 'DOMAIN,' + i
    proxy_set.add(j)
tmp_set.clear()
for item in PROXY_URL[1]:
    proxy_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('!'))])
LEN_proxy = len(proxy_set)
proxy_text = '\n'.join(sorted(proxy_set))
with open("./Rules/proxy.list", "w",encoding='utf-8') as f:
    f.write(proxy_text)
del proxy_set,proxy_text

direct_set = set()
for item in DIRECT_URL[0]:
    tmp_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('!'))])
for i in tmp_set:
    j = ''
    if i.startswith('.'):
        j = 'DOMAIN,' + i[1:]
    else:
        j = 'DOMAIN,' + i
    direct_set.add(j)
del tmp_set
for item in DIRECT_URL[1]:
    direct_set.update([i for i in get_text(item).split("\n") if not (i.startswith('#') or i.startswith('!'))])
LEN_direct = len(direct_set)
direct_text = '\n'.join(sorted(direct_set))
with open("./Rules/direct.list", "w",encoding='utf-8') as f:
    f.write(direct_text)
del direct_set,direct_text
my_stat = []
with open("./Rules/stat", "r",encoding='utf-8') as f:
    my_stat.extend([i[i.rindex(' ')+1:] for i in f.read().strip().split("\n") if not i.startswith('#')])
LEN_reject0,LEN_proxy0,LEN_direct0,LEN_total= int(my_stat[0]),int(my_stat[1]),int(my_stat[2]),int(my_stat[3])
STR_stat = f'#{(datetime.now().astimezone(timezone(timedelta(hours=8)))).strftime("%Y/%m/%d %H:%M:%S")}(UTC/GMT+08:00)\n\
reject rules({LEN_reject0}{"+" if LEN_reject-LEN_reject0 >= 0 else "-"}{abs(LEN_reject-LEN_reject0)}): {LEN_reject}\n\
proxy rules({LEN_proxy0}{"+" if LEN_proxy-LEN_proxy0 >= 0 else "-"}{abs(LEN_proxy-LEN_proxy0)}): {LEN_proxy}\n\
direct rules({LEN_direct0}{"+" if LEN_direct-LEN_direct0 >= 0 else "-"}{abs(LEN_direct-LEN_direct0)}): {LEN_direct}\n\
total rules({LEN_total}{"+" if LEN_reject+LEN_proxy+LEN_direct-LEN_total >= 0 else "-"}{abs(LEN_reject+LEN_proxy+LEN_direct-LEN_total)}): {LEN_reject+LEN_proxy+LEN_direct}'
with open("./Rules/stat", "w",encoding='utf-8') as f:
    f.write(STR_stat)
del my_stat,STR_stat,LEN_reject,LEN_proxy,LEN_direct,LEN_reject0,LEN_proxy0,LEN_direct0,LEN_total


