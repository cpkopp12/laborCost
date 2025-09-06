# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LaborCost.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.button = QPushButton(Form)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(80, 70, 100, 32))
        self.button_2 = QPushButton(Form)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(80, 120, 100, 32))
        self.output = QTextEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(200, 60, 181, 111))
        self.button_3 = QPushButton(Form)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(230, 190, 100, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button.setText(QCoreApplication.translate("Form", u"TimeCards File", None))
        self.button_2.setText(QCoreApplication.translate("Form", u"Sales Summary File", None))
        self.button_3.setText(QCoreApplication.translate("Form", u"Run Labor Cost Calc", None))
    # retranslateUi

