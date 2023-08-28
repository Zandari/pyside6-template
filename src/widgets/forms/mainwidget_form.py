# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.tableview = QTableView(Form)
        self.tableview.setObjectName(u"tableview")
        self.tableview.setGeometry(QRect(10, 10, 381, 251))
        self.incr_button = QPushButton(Form)
        self.incr_button.setObjectName(u"incr_button")
        self.incr_button.setGeometry(QRect(10, 270, 80, 22))
        self.decr_button = QPushButton(Form)
        self.decr_button.setObjectName(u"decr_button")
        self.decr_button.setGeometry(QRect(100, 270, 80, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.incr_button.setText(QCoreApplication.translate("Form", u"incr", None))
        self.decr_button.setText(QCoreApplication.translate("Form", u"decr", None))
    # retranslateUi

