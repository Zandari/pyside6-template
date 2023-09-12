# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accountwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(381, 42)
        Form.setMinimumSize(QSize(380, 30))
        Form.setStyleSheet(u"QPushButton {\n"
"	qproperty-iconSize: 24px 24px;\n"
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QPushButton#settings_button {\n"
"	qproperty-icon: url(:/icons/resources/icons/settings.png);\n"
"}\n"
"\n"
"QPushButton#browser_button {\n"
"	qproperty-icon: url(:/icons/resources/icons/web_asset.png);\n"
"}\n"
"\n"
"QPushButton#logs_button {\n"
"	qproperty-icon: url(:/icons/resources/icons/list_alt.png);\n"
"}\n"
"\n"
"QPushButton#start_button {\n"
"	qproperty-icon: url(:/icons/resources/icons/resume.png);\n"
"}")
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 381, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.settings_button = QPushButton(self.horizontalLayoutWidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.settings_button)

        self.browser_button = QPushButton(self.horizontalLayoutWidget)
        self.browser_button.setObjectName(u"browser_button")
        self.browser_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.browser_button)

        self.logs_button = QPushButton(self.horizontalLayoutWidget)
        self.logs_button.setObjectName(u"logs_button")
        self.logs_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.logs_button)

        self.start_button = QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.start_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Proxy", None))
        self.settings_button.setText("")
        self.browser_button.setText("")
        self.logs_button.setText("")
        self.start_button.setText("")
    # retranslateUi

