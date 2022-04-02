import  requests
from bs4 import BeautifulSoup
url="https://www.21ks.net/lunwen/slsdgclw/93275.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55",
}
data=requests.get(url=url,headers=headers)
# print(data.text)
data.encoding = "gbk"
data=data.content.decode("gbk")
# print(type(data))
# print()

# soup=BeautifulSoup(data,"html.parser",from_encoding="gbk")
# print(soup.title)
# print(soup.find("div",id="div16"))
# res=data.content.decode("gbk")
# print(res)
with open("save_html.txt","w",encoding="utf-8") as f:
    f.write(data)
with  open("save_html.txt","r",encoding="utf-8") as f:
    res=f.read()
# print(res)
soup=BeautifulSoup(res,"html.parser")
# print(soup.title)
elm=soup.find("div",id="div16")
result=""
# fp=open("save_txt.txt","w",encoding="utf-8")
with open("save_txt.txt","w",encoding="utf-8") as fp:
    for i in elm:

        result+=i.text.replace("\n","").replace("。",".\n")
        fp.write(i.text.replace("\n","").replace("。",".\n"))


    # print(i.text.replace("\n",""))#.replace("。",".\n"))
# print(result)

# soup=BeautifulSoup(res,"html.parser",from_encoding="utf-8")
# print(soup)