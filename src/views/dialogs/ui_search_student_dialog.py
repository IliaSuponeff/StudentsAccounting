# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_student_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SearchStudentDialog(object):
    def setupUi(self, SearchStudentDialog):
        if not SearchStudentDialog.objectName():
            SearchStudentDialog.setObjectName(u"SearchStudentDialog")
        SearchStudentDialog.resize(450, 500)
        SearchStudentDialog.setMinimumSize(QSize(450, 300))
        SearchStudentDialog.setMaximumSize(QSize(450, 500))
        SearchStudentDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(SearchStudentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gLayout_1 = QFormLayout()
        self.gLayout_1.setObjectName(u"gLayout_1")
        self.info_lbl_2 = QLabel(SearchStudentDialog)
        self.info_lbl_2.setObjectName(u"info_lbl_2")
        self.info_lbl_2.setAlignment(Qt.AlignCenter)

        self.gLayout_1.setWidget(0, QFormLayout.LabelRole, self.info_lbl_2)

        self.student_name_le = QLineEdit(SearchStudentDialog)
        self.student_name_le.setObjectName(u"student_name_le")

        self.gLayout_1.setWidget(0, QFormLayout.FieldRole, self.student_name_le)

        self.info_lbl_1 = QLabel(SearchStudentDialog)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.gLayout_1.setWidget(1, QFormLayout.LabelRole, self.info_lbl_1)

        self.currency_box = QComboBox(SearchStudentDialog)
        self.currency_box.setObjectName(u"currency_box")
        self.currency_box.setEditable(True)

        self.gLayout_1.setWidget(1, QFormLayout.FieldRole, self.currency_box)


        self.verticalLayout.addLayout(self.gLayout_1)

        self.info_lbl_3 = QLabel(SearchStudentDialog)
        self.info_lbl_3.setObjectName(u"info_lbl_3")
        self.info_lbl_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_3)

        self.students_list = QListWidget(SearchStudentDialog)
        self.students_list.setObjectName(u"students_list")

        self.verticalLayout.addWidget(self.students_list)


        self.retranslateUi(SearchStudentDialog)

        QMetaObject.connectSlotsByName(SearchStudentDialog)
    # setupUi

    def retranslateUi(self, SearchStudentDialog):
        SearchStudentDialog.setWindowTitle(QCoreApplication.translate("SearchStudentDialog", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.info_lbl_2.setText(QCoreApplication.translate("SearchStudentDialog", u"\u0418\u043c\u044f \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.info_lbl_1.setText(QCoreApplication.translate("SearchStudentDialog", u"\u0422\u0438\u043f \u0432\u0430\u043b\u044e\u0442\u044b", None))
        self.info_lbl_3.setText(QCoreApplication.translate("SearchStudentDialog", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0443\u0447\u0435\u043d\u0438\u043a\u0438", None))
    # retranslateUi

