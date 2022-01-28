

# SCPSL白名单验证工具
## 简介
由于国服有人吃饱了撑的没事干，天天打服，很多服务器都使用了IP白名单验证，但因为国内糟糕的网络环境，进行验证有时候很困难，便有了本工具。  
本工具用于在使用加速器时进行SCPSL中某些服务器的IP白名单验证。效果图：
![enter description here](https://cdn.jsdelivr.net/gh/XCwosjw/CDN@main/Pic/2.png)

## 构建
```
git clone https://github.com/XCwosjw/SCPSL-Verify-Tool.git
cd SCPSL-Verify-Tool
pip install -r requirements.txt
pyinstaller -F -w (--upx-dir) main.py
```

## 使用
在[Releases](https://github.com/XCwosjw/SCPSL-Verify-Tool/releases)下载最新版，然后打开腾讯加速器加速国服SL(其他加速器不确定行不行)，再打开本程序(打开可能较慢，因为是PyInstaller打包，要释放文件)，若显示的IP位置与节点的地域相同即为成功，然后直接进行验证即可。

## FAQ
Q：为啥我显示的IP位置与节点的地域不同？  
A：如果是腾讯加速器，可以试试修复工具里的功能，每个都试试，如果还是不行就多试几次。如果是别的加速器，那我也不知道。

