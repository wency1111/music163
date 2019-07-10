import json
import re
import requests
import csv


def get_html():
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        # print(html)
        return html
    except Exception as e:
        print(e)
        pass

def get_id(html):
    r=re.findall(r'<a href="/artist\?id=(\d+)" class="nm.*?>(.*?)</a>',html,re.S)
    title=re.findall(r'<title>(.*?)</title>',html,re.S)
    for tag in r:
        write_csv(tag,title)

def write_csv(tag,title):
    with open("all_singer.csv","a+",newline='',encoding="utf-8")as f:
        writer=csv.writer(f)
        writer.writerow((tag[0],tag[1],title[0]))

# def write_json(tag, title):
#     s = json.dumps({"id": tag[0], 'name': tag[1], 'title': title[0]})
#     with open("all_singer.json", "a+", newline='', encoding="utf-8")as f:
#         f.write(s)
#

if __name__=="__main__":
    headers = {
        'Connection': 'keep-alive',
        'upgrade-insecure-requests': '1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.169Safari / 537.36',
        'referer': 'https: // music.163.com /',
        'host': 'music.163.com',
        'cookie':'_iuqxldmzr_=32; _ntes_nnid=ce491ea72775cf2064fb08f603793425,1559303794852; _ntes_nuid=ce491ea72775cf2064fb08f603793425; WM_TID=QONQjzQ6Ys9BUURAABNsjgSimuqI%2BTIa; WM_NI=%2BhwokW6y%2BYJ1QzzTuaEFXe5UNJ%2FSd0GkA9ENvZ3RsPcRZtQvyovP%2FwTpxHpjauZBIlNF2V3cyDkSN2Kb9AdoXBcLKbdzAajF9dkQqL93p%2FslcPZAl71MqTaE4pDdtG8vZFE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3d074b49083d8f65e96b08aa2c85b929f9fbaf339fb93bd87c859fc9cbcb3e52af0fea7c3b92ae9b8b990ea5df6a7e5bac93b93a6b6b5f86b879a9886b85f8e96e1b4e73c85b58fdac846b686fdb3f25ca18e9695d47ebbb1bab1ae7d98b0b8a9f362a3ab96a3cc688e9afeb7b269bb9ca5b4cd3a89bef7a2e7659c9eadadca6aa8a68f82e94efbbca5b2f448fbedc0d0f268a19096a2ef3df393bfb5e44ff8b08c85f74dfcaa96a7c837e2a3; JSESSIONID-WYYY=cTGEBgdmpzqXIEDY4wV8ofaa%2Bl0lxVB3sQgFX807QNyEJiGj1bCZkby4wpCV5QeuiSGY%2FH3mBkfRNSfD0qESgnGeQTuU%5CICO%2BVNCxKoA%5CF9EGuFrG5PFFJlBJwRjKUMa5gcxGABP0zoud9Ei7NbwHevz8FoFopDC%2BiOgoZrB%2FUsM0Pc9%3A1561632677667; playerid=38046357'}
    list01=[1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003,4001,4002,4003]
    list02=[0,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    for i in list01:
        for j in list02:
            url='https://music.163.com/discover/artist/cat?id=%s&initial=%s'%(i,j)
            html=get_html()
            get_id(html)



















