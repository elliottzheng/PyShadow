# PyShadow 
　　自动获取iShadowsocks服务器ip，密码，端口并部署到SS客户端的python脚本
## 作用
- iShadowSocks上提供免费的SS，但是有一个问题就是它每六个小时会更新一次密码（可能还有端口），这就不太方便。
- PyShadow.py帮你爬取ishdowshocks上最新的免费SS服务器ip，密码，端口，并写入SS的配置文件 gui-config.json。
- PyShadow.bat调用PyShadow.py帮你更新完服务器，端口，密码之后顺便帮你关闭失效的SS再打开新的SS。

## 安装 
1. 安装 python3.x
2. 将项目clone到本地，拷贝 PyShadow.py，PyShadow.bat，gui-config_template.json 使它们和 Shadowsocks.exe在同一目录下。
3. 安装依赖
```
pip install -r requirements.txt
```
## 使用方法
- 运行 PyShadow.py 更新gui-config.json 内的服务器配置
- 或双击运行 **PyShadow.bat** 除了帮你更新完服务器ip，端口，密码之后还顺便帮你关闭失效的SS再打开新的SS。

## 效果
1. 从服务器上获得最新的iShadowSocks 网址（这种网站经常换域名的，我尽量保证最新的可用）
2. 从服务器上获取id_list.json,也就是html元素的id列表，帮助我们通过beautifulsoup找到服务器ip，密码，端口。
3. requests 爬取iShadowSocks，通过beautifulsoup解析，查找，最后保存到gui-configs.json中（以gui-config_template.json为模板）
### 注
　　网址文件和id_list.json现在托管在coding（国内速度还是可以），现在每次应该可以获取12个服务器ip，密码，端口。按照顺序从上到下，每3个为一组，分别为美国，日本，新加坡，SSR。**默认设置的是美国服务器，但是为了服务器均衡，具体是哪个服务器，是由随机数决定的**。。。如果想切换服务器，请打开SS自行切换。

## 原理
基于requests、Beautifulsoup