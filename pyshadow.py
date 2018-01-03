import sys,os
import requests
from bs4 import BeautifulSoup
import re
import json
import copy
import random



def store(filename,data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data))


def fetch(baseUrl,id_list,data):
    template=copy.deepcopy(data["configs"][0])
    data['configs'].clear()
    
    # 第1步：模拟浏览器发送请求
    r=requests.get(baseUrl)
    
    if r.status_code!=200:
        return None
    soup=BeautifulSoup(r.text, "html.parser")
    
    for one_id in id_list:
        print(one_id)
        temp=copy.deepcopy(template)
        temp["sever"]=soup.find("span",id=one_id['ip']).text
        temp["server_port"]=int(soup.find("span",id=one_id['port']).text)
        temp["password"]=int(soup.find("span",id=one_id['password']).text)
        data['configs'].append(temp)
        
    #设置当前服务器为美国服务器中的任意一个，(0,2)三个服务器为美国服务器
    data["index"]=random.randint(0,2)
    return
    # 第3步：返回在页面上析取的元素


def fetch_id_list(id_list_url):
    r=requests.get(id_list_url)
    
    if r.status_code!=200:
        return None
    return json.loads(r.text)["configs"]

def fetch_new_url(url_url):
    r=requests.get(url_url)
    if r.status_code!=200:
        return None
    return r.text



    
#######     执行    ######## 
if __name__ =="__main__":
    
    #存放着最新的ishadowsocks地址的url
    url_url='https://coding.net/u/ElliottZheng/p/elliottzheng.coding.me/git/raw/master/pyshadow_config/ishadowsocks'
    #获取最新的ishadowsocks地址
    print("Fetching the latest url of iShadowSocks...")
    url =fetch_new_url(url_url)
    
    #配置文件名
    bak_config_file_name="gui-config_template.json"
    config_file_name="gui-config.json"
    
    #获取最新的html id列表
    id_list_url='https://coding.net/u/ElliottZheng/p/elliottzheng.coding.me/git/raw/master/pyshadow_config/id_list.json'
    print("Fetching the latest iShadowSocks' html ip set....")
    id_list=fetch_id_list(id_list_url)

    
    data=json.load(open(bak_config_file_name))
    #存放到名字列表中
    print("Fetching the latest Free SS sever,port,and password ....")
    fetch(url,id_list,data)
    
    store(config_file_name,data)
    

