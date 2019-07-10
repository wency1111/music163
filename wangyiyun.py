import requests
import re
import json



def get_text(url):
    response=requests.get(url,headers=headers)
    response.encoding="utf-8"
    text=response.text
    return text

def get_info(html):
    ids=re.findall(r'<a href="/song\?(.*?)">(.*?)</a>',html)
    IDS = []
    for i in range(len(ids)):
        if ids[i][0]!="id=${x.id}":
            IDS.append(ids[i])
    for i in range(len(IDS)):
        link="https://music.163.com/song?{}".format(IDS[i][0])
        print(IDS[i][1],link)
    return IDS

def get_lyric(IDS):
    fromdata={"params":"HW2K7WtRwAMWwsZxQgaCnvb5zHuwJy34h7RVOegiAuedGNQzHjwl49EWOeFEO85bCBIQqaa+BFMEtA3oAjJ0boockyUd2BtoZnOXp5lQD+A=",
                "encSecKey":"77e12fbdeadba24ffeff9cca3ed4e2e5d9b52f291ca5d12af62d32e00f66c3beba47da90afdc35b6f777e0eabd0afb8db939803f5386badbc94ed884dddd82d7da8c6d2e5489d2b52d8ee2fe8a59b63473691986a434549097aa25502a73bbd9294f51c5c260ea4e618b261b9d1f7e736c4790d625b801b37e0f0361f9053c00Namelyric?csrf_token="}
    for i in range(len(IDS)):
        url="https://music.163.com/api/song/lyric?%s&lv=1&kv=1&tv=-1"%IDS[i][0]
        response = requests.post(url, headers=headers, data=fromdata)
        text = response.text
        html = json.loads(text)
        print(html['lrc'])


def get_comments(IDS):
    fromdata={"params":"XIt/aISht9OLmPBv9ZF1GBXBsHJW8/Y435fGJkg3qZG4sW5HwZnMRiTz8oUuI0m8ljY8H1pA9+7gRYBL1WsQYrJxqNmiAP17Spp/gguv+p38lNdlFJ5Y5m3Vxr1kgsUpyurv8Ug9VwtHJrilV1fu0FgVn1OBD4ZiZDoPoIixYSTvWBKrX3NRH4OrbB3UiJ/W",
                "encSecKey":"57e853afce4b7e607c6461039dfda401143d0aa7b22b9d1b8aaff3d9ac5f95c815a6215dbd187a569e2a679eb12680db3834601461ca1d3e1aa6b28989b31561ed21cb43bee8c1566c0504d98cba8abc70b702d57538c7d133abf98f31dda33f765f19ffbeb4516e5eaf0286b412845f2fa1efb392e5b994e316756fcba09142"}
    for i in range(len(IDS)):
        url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=" % IDS[i][0][3:]
        response = requests.post(url,headers=headers,data=fromdata)
        text=response.text
        html=json.loads(text)
        num=1
        for user in html['comments']:
            commtent=user['user']['nickname']+":"+user['content']+"点赞数："+str(user['likedCount'])
            with open("1.txt","a+",encoding="utf-8")as f:
                f.write(str(num)+"  "+commtent+"\n")
            num+=1

if __name__=="__main__":
    headers = {
        'cookie': '_ntes_nnid=a2f12a2fb72f9b4ff5090f80be2f049c,1556885398382; _ntes_nuid=a2f12a2fb72f9b4ff5090f80be2f049c; JSESSIONID-WYYY=28iAQTJDmZQU%5C6MkgR%5CwklxZ1dsc%2FWyRiY4V0YG1gly%5CjpHvnY4DZ16REs%2BgEhz9BNUmoY0DyX4%2Fc7i2ki5IbQuG8sE%2BtKvnn2hIOvAFf7p4IM3XNRcr%2FA7oKj6fMkQj7iY2IDUG2OFEYwpItsmdWAKzPIvriTbDKifUxs6DCgTgf84H%3A1561473337786; _iuqxldmzr_=32; WM_NI=HmRdWgEHDafv4IJBGLZq8tt9RSGoTBCy3qz2YBLM%2BTeZ5ZyNM63A7bC68AumpIsrZnI9vMs85Lkf2hnhnD0rW6xdcsy%2F%2F0F140W010o6l5%2Btk%2FKHoh12iVstR3%2BDoOP7Y00%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed9e672818abf99d17af2a88aa6c84e879e8e84bb72f798f796ed52828ebe84c92af0fea7c3b92a8cb39e85d66d87988c82e57ef89786a3c6489aaff895f733928d8990d74a81a7fd92f93a9b9e84aeaa60a786fbbbfc468feafda2b66a81eaf8a2f867b497bd93d9668be7baaef234f794a587b164aeb8a2a5b37a95eab885e279bbf1e1d1c53bf8f099d1b43cadeaa4d6aa80a9f185a9ee64f3eea7b7f28092ede5a5ee4594e997d1b337e2a3; WM_TID=BXP4Iv0EkjpBRAEAFRZsjWunx4K8sl%2Bd',
        'referer': 'https://music.163.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}

    id=input("请输入歌手id：")
    url = 'https://music.163.com/artist?id=%s'%id
    html1=get_text(url)
    IDS=get_info(html1)
    # get_lyric(IDS)
    get_comments(IDS)

    # for info in infos:
    #     print(info[0],info[1],info[2])
        # get_lyric(info[0],info[1],info[2])












































