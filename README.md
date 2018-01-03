# PyShadow 
　　自动获取iShadowsocks账号密码并部署到SS客户端的python脚本，基于requests、Beautifulsoup、json。
## 作用
- 爬取ishdowshocks上最新的免费SS服务器ip，密码，端口，并写入SS的配置文件 gui-config.json。
- 还有一个.bat脚本帮你更新完服务器，端口，密码之后顺便帮你关闭失效的SS再打开新的SS。

## 安装 
1. 安装 python3.x
2. 将项目clone到本地，拷贝 PyShadow.py，PyShadow.bat，gui-config2.json 和 Shadowsocks.exe在同一目录下。
3. 安装依赖文件
```
pip install -r requirements.txt
```
## 使用方法
- 双击运行 PyShadow.py 更新gui-config.json 内的配置
- 命令行输入 python PyShadow.py
- 双击运行 PyShadow.bat 除了帮你更新完服务器，端口，密码之后顺便帮你关闭失效的SS再打开新的SS。
## 原理
