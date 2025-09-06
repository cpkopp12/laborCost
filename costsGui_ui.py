# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'costsGui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.textInput = QLineEdit(Form)
        self.textInput.setObjectName(u"textInput")
        self.textInput.setGeometry(QRect(170, 40, 113, 21))
        self.textInput_2 = QLineEdit(Form)
        self.textInput_2.setObjectName(u"textInput_2")
        self.textInput_2.setGeometry(QRect(170, 110, 113, 21))
        self.button = QPushButton(Form)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(40, 110, 100, 32))
        self.output = QTextEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(90, 160, 181, 111))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

