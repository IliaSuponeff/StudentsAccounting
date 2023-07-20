# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        if not HelpDialog.objectName():
            HelpDialog.setObjectName(u"HelpDialog")
        HelpDialog.resize(800, 700)
        HelpDialog.setMinimumSize(QSize(800, 700))
        HelpDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(HelpDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_lbl_1 = QLabel(HelpDialog)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setFrameShape(QFrame.NoFrame)
        self.info_lbl_1.setFrameShadow(QFrame.Plain)
        self.info_lbl_1.setLineWidth(1)
        self.info_lbl_1.setAlignment(Qt.AlignCenter)
        self.info_lbl_1.setWordWrap(True)

        self.verticalLayout.addWidget(self.info_lbl_1)

        self.help_info_tb = QTextBrowser(HelpDialog)
        self.help_info_tb.setObjectName(u"help_info_tb")
        self.help_info_tb.setReadOnly(True)
        self.help_info_tb.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.help_info_tb)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_1.addItem(self.hSpacer_1)

        self.close_btn = QPushButton(HelpDialog)
        self.close_btn.setObjectName(u"close_btn")

        self.hLayout_1.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.hLayout_1)


        self.retranslateUi(HelpDialog)

        QMetaObject.connectSlotsByName(HelpDialog)
    # setupUi

    def retranslateUi(self, HelpDialog):
        HelpDialog.setWindowTitle(QCoreApplication.translate("HelpDialog", u"Help", None))
        self.info_lbl_1.setText(QCoreApplication.translate("HelpDialog", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("HelpDialog", u"Close", None))
    # retranslateUi

