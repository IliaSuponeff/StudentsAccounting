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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        if not HelpDialog.objectName():
            HelpDialog.setObjectName(u"HelpDialog")
        HelpDialog.resize(600, 700)
        HelpDialog.setMinimumSize(QSize(600, 700))
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

        self.help_info_te = QTextEdit(HelpDialog)
        self.help_info_te.setObjectName(u"help_info_te")
        self.help_info_te.setFrameShape(QFrame.WinPanel)
        self.help_info_te.setReadOnly(True)

        self.verticalLayout.addWidget(self.help_info_te)

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
        self.help_info_te.setHtml(QCoreApplication.translate("HelpDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.close_btn.setText(QCoreApplication.translate("HelpDialog", u"Close", None))
    # retranslateUi

