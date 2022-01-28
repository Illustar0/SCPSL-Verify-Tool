import os
import sys
from threading import Thread
import requests
from PyQt5.QtWidgets import QMessageBox
from resource import *
import SCPSL
from PyQt5 import QtCore, QtWebEngineWidgets, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
import _thread
import json





qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2


def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)


def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)


qInitResources()

if getattr(sys, 'frozen', False):
    QTpath = sys._MEIPASS + r"\PyQt5\Qt5\bin\SCPSL.exe"
    os.rename(sys._MEIPASS + r"\PyQt5\Qt5\bin\QtWebEngineProcess.exe", sys._MEIPASS + r"\PyQt5\Qt5\bin\SCPSL.exe")
    os.environ['QTWEBENGINEPROCESS_PATH'] = QTpath

else:
    QTpath = os.getcwd() + r"\SCPSL.exe"


def myip():
    ui.IP.setText(SCPSL.getip())


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(737, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 101, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urledit = QtWidgets.QLineEdit(Form)
        self.urledit.setGeometry(QtCore.QRect(100, 0, 511, 25))
        self.urledit.setObjectName("urledit")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(0, 0, 25, 25))
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.forward = QtWidgets.QPushButton(Form)
        self.forward.setGeometry(QtCore.QRect(25, 0, 25, 25))
        self.forward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/icons/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon1)
        self.forward.setObjectName("forward")
        self.horizontalLayout.addWidget(self.forward)
        self.reload = QtWidgets.QPushButton(Form)
        self.reload.setGeometry(QtCore.QRect(50, 0, 25, 25))
        self.reload.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/icons/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon2)
        self.reload.setObjectName("reload")
        self.horizontalLayout.addWidget(self.reload)
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(75, 0, 25, 25))
        self.stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon3)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(611, 0, 121, 26))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GO = QtWidgets.QPushButton(Form)
        self.GO.setGeometry(QtCore.QRect(611, 0, 25, 25))
        self.GO.setText("")
        self.GO.setIcon(icon1)
        self.GO.setCheckable(False)
        self.GO.setObjectName("GO")
        self.horizontalLayout_2.addWidget(self.GO)
        self.Author = QtWidgets.QLabel(Form)
        self.Author.setGeometry(QtCore.QRect(636, 0, 101, 25))
        self.Author.setObjectName("Author")
        self.horizontalLayout_2.addWidget(self.Author)
        self.webView = WebEngineView(Form)
        self.webView.setGeometry(QtCore.QRect(0, 25, 611, 500))
        self.webView.urlChanged.connect(self.renew_urlbar)
        self.webView.setUrl(QtCore.QUrl("https://scpslgame.com/"))
        self.webView.setObjectName("webView")

        self.kj = QtWidgets.QLabel(Form)
        self.kj.setGeometry(QtCore.QRect(611, 25, 126, 40))
        self.kj.setObjectName("kj")
        self.IP = QtWidgets.QLabel(Form)
        self.IP.setGeometry(QtCore.QRect(0, 525, 611, 24))
        self.IP.setObjectName("IP")
        self.cdcp = QtWidgets.QPushButton(Form)
        self.cdcp.setGeometry(QtCore.QRect(610, 65, 126, 30))
        self.cdcp.setObjectName("cdcp")
        self.scpmiao = QtWidgets.QPushButton(Form)
        self.scpmiao.setGeometry(QtCore.QRect(610, 90, 126, 30))
        self.scpmiao.setObjectName("scpmiao")
        self.bg = QtWidgets.QPushButton(Form)
        self.bg.setEnabled(False)
        self.bg.setGeometry(QtCore.QRect(610, 115, 126, 30))
        self.bg.setObjectName("bg")
        self.remia = QtWidgets.QPushButton(Form)
        self.remia.setGeometry(QtCore.QRect(610, 140, 126, 30))
        self.remia.setObjectName("remia")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        _thread.start_new_thread(myip, ())

        self.urledit.returnPressed.connect(self.navigate_to_url)

        self.cdcp.clicked.connect(self.cdcp_load)
        self.GO.clicked.connect(self.go_load)
        self.back.clicked.connect(self.back_load)
        self.forward.clicked.connect(self.forward_load)
        self.reload.clicked.connect(self.reload_load)
        self.stop.clicked.connect(self.stop_load)
        self.remia.clicked.connect(self.remia_load)
        self.scpmiao.clicked.connect(self.miao_load)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SCPSL白名单验证"))
        self.cdcp.setText(_translate("Form", "超电磁炮服论坛"))
        self.scpmiao.setText(_translate("Form", "喵呜服务器验证"))
        self.bg.setText(_translate("Form", "白给实验室验证"))
        self.remia.setText(_translate("Form", "Remia服验证"))
        self.kj.setText(_translate("Form", "------快捷链接------"))
        self.Author.setText(_translate("Form", "By XCwosjw"))
        self.IP.setText(_translate("Form", "正在获取IP"))

    def cdcp_load(self):
        self.webView.setUrl(QtCore.QUrl("https://bbs.railgungame.cn/"))

    def miao_load(self):
        self.webView.setUrl(QtCore.QUrl("http://scpmiao.cn:12345/"))

    def remia_load(self):
        self.webView.setUrl(QtCore.QUrl("http://scpsl.yuyuko.com:12345/"))

    def renew_urlbar(self, q):
        self.urledit.setText(q.toString())
        self.urledit.setCursorPosition(0)

    def navigate_to_url(self):
        q = QUrl(self.urledit.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.webView.setUrl(q)

    def go_load(self):
        q = QUrl(self.urledit.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.webView.setUrl(q)

    def back_load(self):
        self.webView.back()

    def forward_load(self):
        self.webView.forward()

    def reload_load(self):
        self.webView.reload()

    def stop_load(self):
        self.webView.stop()


class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self, url):
        self.setUrl(url)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    MainWindow.show()
    sys.exit(app.exec_())
