# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_student.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CreaterStudent(object):
    def setupUi(self, CreaterStudent):
        if not CreaterStudent.objectName():
            CreaterStudent.setObjectName(u"CreaterStudent")
        CreaterStudent.resize(500, 200)
        CreaterStudent.setMinimumSize(QSize(500, 200))
        CreaterStudent.setMaximumSize(QSize(500, 200))
        CreaterStudent.setModal(True)
        self.verticalLayout = QVBoxLayout(CreaterStudent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dialog_title_lbl = QLabel(CreaterStudent)
        self.dialog_title_lbl.setObjectName(u"dialog_title_lbl")
        self.dialog_title_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dialog_title_lbl)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.info_lbl_1 = QLabel(CreaterStudent)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.hLayout_1.addWidget(self.info_lbl_1)

        self.name_le = QLineEdit(CreaterStudent)
        self.name_le.setObjectName(u"name_le")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_le.sizePolicy().hasHeightForWidth())
        self.name_le.setSizePolicy(sizePolicy)
        self.name_le.setAlignment(Qt.AlignCenter)
        self.name_le.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.hLayout_1.addWidget(self.name_le)


        self.verticalLayout.addLayout(self.hLayout_1)

        self.hLine_1 = QFrame(CreaterStudent)
        self.hLine_1.setObjectName(u"hLine_1")
        self.hLine_1.setFrameShape(QFrame.HLine)
        self.hLine_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.hLine_1)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setObjectName(u"hLayout_4")
        self.hLayout_3 = QHBoxLayout()
        self.hLayout_3.setObjectName(u"hLayout_3")
        self.info_lbl_2 = QLabel(CreaterStudent)
        self.info_lbl_2.setObjectName(u"info_lbl_2")
        self.info_lbl_2.setAlignment(Qt.AlignCenter)

        self.hLayout_3.addWidget(self.info_lbl_2)

        self.hour_cost_spin_box = QDoubleSpinBox(CreaterStudent)
        self.hour_cost_spin_box.setObjectName(u"hour_cost_spin_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hour_cost_spin_box.sizePolicy().hasHeightForWidth())
        self.hour_cost_spin_box.setSizePolicy(sizePolicy1)
        self.hour_cost_spin_box.setWrapping(False)
        self.hour_cost_spin_box.setFrame(True)
        self.hour_cost_spin_box.setAlignment(Qt.AlignCenter)
        self.hour_cost_spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.hour_cost_spin_box.setDecimals(1)
        self.hour_cost_spin_box.setMaximum(999999.000000000000000)
        self.hour_cost_spin_box.setValue(0.000000000000000)

        self.hLayout_3.addWidget(self.hour_cost_spin_box)


        self.hLayout_4.addLayout(self.hLayout_3)

        self.vLine_1 = QFrame(CreaterStudent)
        self.vLine_1.setObjectName(u"vLine_1")
        self.vLine_1.setFrameShape(QFrame.VLine)
        self.vLine_1.setFrameShadow(QFrame.Sunken)

        self.hLayout_4.addWidget(self.vLine_1)

        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.info_lbl_3 = QLabel(CreaterStudent)
        self.info_lbl_3.setObjectName(u"info_lbl_3")
        self.info_lbl_3.setAlignment(Qt.AlignCenter)

        self.hLayout_2.addWidget(self.info_lbl_3)

        self.currency_box = QComboBox(CreaterStudent)
        self.currency_box.setObjectName(u"currency_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currency_box.sizePolicy().hasHeightForWidth())
        self.currency_box.setSizePolicy(sizePolicy2)

        self.hLayout_2.addWidget(self.currency_box)


        self.hLayout_4.addLayout(self.hLayout_2)


        self.verticalLayout.addLayout(self.hLayout_4)

        self.hLine_2 = QFrame(CreaterStudent)
        self.hLine_2.setObjectName(u"hLine_2")
        self.hLine_2.setFrameShape(QFrame.HLine)
        self.hLine_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.hLine_2)

        self.hLayout_ = QHBoxLayout()
        self.hLayout_.setObjectName(u"hLayout_")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_.addItem(self.hSpacer_1)

        self.done_btn = QPushButton(CreaterStudent)
        self.done_btn.setObjectName(u"done_btn")
        sizePolicy1.setHeightForWidth(self.done_btn.sizePolicy().hasHeightForWidth())
        self.done_btn.setSizePolicy(sizePolicy1)

        self.hLayout_.addWidget(self.done_btn)


        self.verticalLayout.addLayout(self.hLayout_)


        self.retranslateUi(CreaterStudent)

        QMetaObject.connectSlotsByName(CreaterStudent)
    # setupUi

    def retranslateUi(self, CreaterStudent):
        CreaterStudent.setWindowTitle(QCoreApplication.translate("CreaterStudent", u"StudentCreater", None))
        self.dialog_title_lbl.setText(QCoreApplication.translate("CreaterStudent", u"Creating Student", None))
        self.info_lbl_1.setText(QCoreApplication.translate("CreaterStudent", u"Name", None))
        self.info_lbl_2.setText(QCoreApplication.translate("CreaterStudent", u"Hour cost", None))
        self.info_lbl_3.setText(QCoreApplication.translate("CreaterStudent", u"Currency", None))
        self.done_btn.setText(QCoreApplication.translate("CreaterStudent", u"Create", None))
    # retranslateUi
