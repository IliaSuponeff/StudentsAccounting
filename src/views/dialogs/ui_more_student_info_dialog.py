# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'more_student_info_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MoreInfoDialog(object):
    def setupUi(self, MoreInfoDialog):
        if not MoreInfoDialog.objectName():
            MoreInfoDialog.setObjectName(u"MoreInfoDialog")
        MoreInfoDialog.resize(1280, 640)
        MoreInfoDialog.setMinimumSize(QSize(1280, 640))
        MoreInfoDialog.setMaximumSize(QSize(1280, 720))
        MoreInfoDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(MoreInfoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fiter_period_info_lbl = QLabel(MoreInfoDialog)
        self.fiter_period_info_lbl.setObjectName(u"fiter_period_info_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiter_period_info_lbl.sizePolicy().hasHeightForWidth())
        self.fiter_period_info_lbl.setSizePolicy(sizePolicy)
        self.fiter_period_info_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.fiter_period_info_lbl)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setObjectName(u"hLayout_4")
        self.hSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_4.addItem(self.hSpacer_3)

        self.all_students_check_rbtn = QRadioButton(MoreInfoDialog)
        self.all_students_check_rbtn.setObjectName(u"all_students_check_rbtn")
        self.all_students_check_rbtn.setLayoutDirection(Qt.RightToLeft)
        self.all_students_check_rbtn.setChecked(True)

        self.hLayout_4.addWidget(self.all_students_check_rbtn)

        self.hSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.hLayout_4.addItem(self.hSpacer_5)

        self.one_student_check_rbtn = QRadioButton(MoreInfoDialog)
        self.one_student_check_rbtn.setObjectName(u"one_student_check_rbtn")

        self.hLayout_4.addWidget(self.one_student_check_rbtn)

        self.hSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_4.addItem(self.hSpacer_4)


        self.verticalLayout.addLayout(self.hLayout_4)

        self.student_choose_frame = QFrame(MoreInfoDialog)
        self.student_choose_frame.setObjectName(u"student_choose_frame")
        self.hLayout_2 = QHBoxLayout(self.student_choose_frame)
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.prev_student_btn = QPushButton(self.student_choose_frame)
        self.prev_student_btn.setObjectName(u"prev_student_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.prev_student_btn.sizePolicy().hasHeightForWidth())
        self.prev_student_btn.setSizePolicy(sizePolicy1)
        self.prev_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.prev_student_btn)

        self.student_choose_box = QComboBox(self.student_choose_frame)
        self.student_choose_box.setObjectName(u"student_choose_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.student_choose_box.sizePolicy().hasHeightForWidth())
        self.student_choose_box.setSizePolicy(sizePolicy2)
        self.student_choose_box.setEditable(True)
        self.student_choose_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.student_choose_box.setFrame(True)

        self.hLayout_2.addWidget(self.student_choose_box)

        self.reload_student_btn = QPushButton(self.student_choose_frame)
        self.reload_student_btn.setObjectName(u"reload_student_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reload_student_btn.sizePolicy().hasHeightForWidth())
        self.reload_student_btn.setSizePolicy(sizePolicy3)
        self.reload_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.reload_student_btn)

        self.next_student_btn = QPushButton(self.student_choose_frame)
        self.next_student_btn.setObjectName(u"next_student_btn")
        sizePolicy1.setHeightForWidth(self.next_student_btn.sizePolicy().hasHeightForWidth())
        self.next_student_btn.setSizePolicy(sizePolicy1)
        self.next_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.next_student_btn)


        self.verticalLayout.addWidget(self.student_choose_frame)

        self.hLayout_3 = QHBoxLayout()
        self.hLayout_3.setObjectName(u"hLayout_3")
        self.hSpacer_8 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_3.addItem(self.hSpacer_8)

        self.plot_type_box = QComboBox(MoreInfoDialog)
        self.plot_type_box.setObjectName(u"plot_type_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.plot_type_box.sizePolicy().hasHeightForWidth())
        self.plot_type_box.setSizePolicy(sizePolicy4)
        self.plot_type_box.setEditable(True)
        self.plot_type_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.plot_type_box.setFrame(True)

        self.hLayout_3.addWidget(self.plot_type_box)

        self.hSpacer_9 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_3.addItem(self.hSpacer_9)


        self.verticalLayout.addLayout(self.hLayout_3)

        self.plot_widget = QWidget(MoreInfoDialog)
        self.plot_widget.setObjectName(u"plot_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy5)
        self.plot_layout = QHBoxLayout(self.plot_widget)
        self.plot_layout.setObjectName(u"plot_layout")

        self.verticalLayout.addWidget(self.plot_widget)

        self.currency_choose_frame = QFrame(MoreInfoDialog)
        self.currency_choose_frame.setObjectName(u"currency_choose_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.currency_choose_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hSpacer_6 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.hSpacer_6)

        self.currency_choose_box = QComboBox(self.currency_choose_frame)
        self.currency_choose_box.setObjectName(u"currency_choose_box")
        sizePolicy4.setHeightForWidth(self.currency_choose_box.sizePolicy().hasHeightForWidth())
        self.currency_choose_box.setSizePolicy(sizePolicy4)
        self.currency_choose_box.setEditable(True)
        self.currency_choose_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.currency_choose_box.setFrame(True)

        self.horizontalLayout_2.addWidget(self.currency_choose_box)

        self.hSpacer_7 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.hSpacer_7)


        self.verticalLayout.addWidget(self.currency_choose_frame)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_1.addItem(self.hSpacer_1)

        self.create_report_btn = QPushButton(MoreInfoDialog)
        self.create_report_btn.setObjectName(u"create_report_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.create_report_btn.sizePolicy().hasHeightForWidth())
        self.create_report_btn.setSizePolicy(sizePolicy6)

        self.hLayout_1.addWidget(self.create_report_btn)

        self.hSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_1.addItem(self.hSpacer_2)


        self.verticalLayout.addLayout(self.hLayout_1)


        self.retranslateUi(MoreInfoDialog)

        QMetaObject.connectSlotsByName(MoreInfoDialog)
    # setupUi

    def retranslateUi(self, MoreInfoDialog):
        MoreInfoDialog.setWindowTitle(QCoreApplication.translate("MoreInfoDialog", u"MoreInfo", None))
        self.fiter_period_info_lbl.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0417\u0430 \u043f\u0435\u0440\u0438\u043e\u0434 \u0441 %d.%m.%Y \u043f\u043e %d.%m.%Y \u0434\u043b\u044f", None))
        self.all_students_check_rbtn.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0414\u043b\u044f \u0432\u0441\u0435\u0445 \u0443\u0447\u0435\u043d\u0438\u043a\u043e\u0432", None))
        self.one_student_check_rbtn.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0414\u043b\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.prev_student_btn.setText("")
        self.reload_student_btn.setText("")
        self.next_student_btn.setText("")
        self.create_report_btn.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
    # retranslateUi

