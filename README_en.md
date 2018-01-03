# PyShadow
[中文 Chinese](./README.md)

A python script that automatically gets the iShadowsocks free SS sever、port and password and deployed to SS client.
- iShadowSocks  provides free SS , but it will change the password ( or port ) every six hours , which is unhandy.
- [pyshadow.py](./pyshadow.py) can help you get the latest free SS server IP, password,and port from ishdowshocks, and update the SS configuration file(gui-config.json).
- [pyshadow.bat](./pyshadow.bat) calls [pyshadow.py](./pyshadow.py) to help you update the configuration of SS and restart it.
## Installation
1. Install python3.x
2. Clone the project to the local, and copy [pyshadow.py](./pyshadow.py),[pyshadow.bat](./pyshadow.bat), and [gui-config_template.json](./gui-config_template.json)，make sure they are under the same directory as **Shadowsocks.exe.**
3. Install dependence
```
pip install -r requirements.txt
```
## Usage
- run [pyshadow.py](./pyshadow.py) to update the server configuration (**gui-config.json**)
- run [pyshadow.bat](./pyshadow.bat) No only helps you update the server configuration, but also restart the SS.
## effect
1. Get the latest iShadowSocks URL from the server  (iShadowSocks often changes its domain name, I will try to ensure it is valid)
2. Get the  **id_list.json** from the server, that is, the ID list of the HTML element, helps us to find the server IP, the password, and the port by beautifulsoup.
3. Use requests to crawl iShadowSocks, parse through beautifulsoup, find, and finally save it to gui-configs.json (use [gui-config_template.json](./gui-config_template.json) as a template)
### Notice
URL files and id_list.json are now hosted in [coding.net](https://coding.net/) , and now you can get 12 servers IP , password, port. In order from top to bottom, each 3 is one group, the United States, Japan, Singapore, SSR. * * * the default setting is the American server, but for the balance of the server, what American server you're using is random.* * *. If you want to switch the server, please open the SS by yourself.
## principle
Based on requests and Beautifulsoup