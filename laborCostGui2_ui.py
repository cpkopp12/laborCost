# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laborCostGui2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(651, 526)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(220, 60, 311, 361))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.output = QTextEdit(self.widget)
        self.output.setObjectName(u"output")

        self.verticalLayout_4.addWidget(self.output)

        self.button_3 = QPushButton(self.widget)
        self.button_3.setObjectName(u"button_3")

        self.verticalLayout_4.addWidget(self.button_3)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 130, 151, 162))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.stubbysBox = QCheckBox(self.widget1)
        self.stubbysBox.setObjectName(u"stubbysBox")

        self.verticalLayout.addWidget(self.stubbysBox)

        self.scootersBox = QCheckBox(self.widget1)
        self.scootersBox.setObjectName(u"scootersBox")

        self.verticalLayout.addWidget(self.scootersBox)

        self.icBox = QCheckBox(self.widget1)
        self.icBox.setObjectName(u"icBox")

        self.verticalLayout.addWidget(self.icBox)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button = QPushButton(self.widget1)
        self.button.setObjectName(u"button")

        self.verticalLayout_2.addWidget(self.button)

        self.button_2 = QPushButton(self.widget1)
        self.button_2.setObjectName(u"button_2")

        self.verticalLayout_2.addWidget(self.button_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_3.setText(QCoreApplication.translate("Form", u"Run", None))
        self.label.setText(QCoreApplication.translate("Form", u"Select Locations", None))
        self.stubbysBox.setText(QCoreApplication.translate("Form", u"Stubbys", None))
        self.scootersBox.setText(QCoreApplication.translate("Form", u"Scooters", None))
        self.icBox.setText(QCoreApplication.translate("Form", u"Island Coffee", None))
        self.button.setText(QCoreApplication.translate("Form", u"TimeCards File", None))
        self.button_2.setText(QCoreApplication.translate("Form", u"Sales Summary File", None))
    # retranslateUi

