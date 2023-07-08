# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'date_choose.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DateChoose(object):
    def setupUi(self, DateChoose):
        if not DateChoose.objectName():
            DateChoose.setObjectName(u"DateChoose")
        DateChoose.resize(480, 420)
        DateChoose.setMinimumSize(QSize(480, 420))
        DateChoose.setMaximumSize(QSize(480, 420))
        DateChoose.setModal(True)
        self.verticalLayout = QVBoxLayout(DateChoose)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_lbl_1 = QLabel(DateChoose)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_1)

        self.calendar = QCalendarWidget(DateChoose)
        self.calendar.setObjectName(u"calendar")

        self.verticalLayout.addWidget(self.calendar)

        self.hlayout_1 = QHBoxLayout()
        self.hlayout_1.setObjectName(u"hlayout_1")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlayout_1.addItem(self.hSpacer_1)

        self.done_btn = QPushButton(DateChoose)
        self.done_btn.setObjectName(u"done_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_btn.sizePolicy().hasHeightForWidth())
        self.done_btn.setSizePolicy(sizePolicy)

        self.hlayout_1.addWidget(self.done_btn)


        self.verticalLayout.addLayout(self.hlayout_1)


        self.retranslateUi(DateChoose)

        QMetaObject.connectSlotsByName(DateChoose)
    # setupUi

    def retranslateUi(self, DateChoose):
        DateChoose.setWindowTitle(QCoreApplication.translate("DateChoose", u"Choose Date", None))
        self.info_lbl_1.setText(QCoreApplication.translate("DateChoose", u"Choose Date", None))
        self.done_btn.setText(QCoreApplication.translate("DateChoose", u"Choose", None))
    # retranslateUi

