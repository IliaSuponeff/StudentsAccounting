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
        MoreInfoDialog.resize(725, 700)
        MoreInfoDialog.setMinimumSize(QSize(600, 500))
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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.hSpacer_3)

        self.all_students_check_rbtn = QRadioButton(MoreInfoDialog)
        self.all_students_check_rbtn.setObjectName(u"all_students_check_rbtn")
        self.all_students_check_rbtn.setLayoutDirection(Qt.RightToLeft)
        self.all_students_check_rbtn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.all_students_check_rbtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.one_student_check_rbtn = QRadioButton(MoreInfoDialog)
        self.one_student_check_rbtn.setObjectName(u"one_student_check_rbtn")

        self.horizontalLayout_3.addWidget(self.one_student_check_rbtn)

        self.hSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.hSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.prev_student_btn = QPushButton(MoreInfoDialog)
        self.prev_student_btn.setObjectName(u"prev_student_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.prev_student_btn.sizePolicy().hasHeightForWidth())
        self.prev_student_btn.setSizePolicy(sizePolicy1)
        self.prev_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.prev_student_btn)

        self.student_choose_box = QComboBox(MoreInfoDialog)
        self.student_choose_box.setObjectName(u"student_choose_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.student_choose_box.sizePolicy().hasHeightForWidth())
        self.student_choose_box.setSizePolicy(sizePolicy2)
        self.student_choose_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.student_choose_box.setFrame(True)

        self.hLayout_2.addWidget(self.student_choose_box)

        self.reload_student_btn = QPushButton(MoreInfoDialog)
        self.reload_student_btn.setObjectName(u"reload_student_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reload_student_btn.sizePolicy().hasHeightForWidth())
        self.reload_student_btn.setSizePolicy(sizePolicy3)
        self.reload_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.reload_student_btn)

        self.next_student_btn = QPushButton(MoreInfoDialog)
        self.next_student_btn.setObjectName(u"next_student_btn")
        sizePolicy1.setHeightForWidth(self.next_student_btn.sizePolicy().hasHeightForWidth())
        self.next_student_btn.setSizePolicy(sizePolicy1)
        self.next_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.next_student_btn)


        self.verticalLayout.addLayout(self.hLayout_2)

        self.info_lbl_1 = QLabel(MoreInfoDialog)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_1)

        self.summary_graph_frame = QFrame(MoreInfoDialog)
        self.summary_graph_frame.setObjectName(u"summary_graph_frame")
        self.summary_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.summary_graph_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.summary_graph_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vLayout_1 = QVBoxLayout()
        self.vLayout_1.setObjectName(u"vLayout_1")
        self.morph_summary_graph_btn = QPushButton(self.summary_graph_frame)
        self.morph_summary_graph_btn.setObjectName(u"morph_summary_graph_btn")
        sizePolicy3.setHeightForWidth(self.morph_summary_graph_btn.sizePolicy().hasHeightForWidth())
        self.morph_summary_graph_btn.setSizePolicy(sizePolicy3)

        self.vLayout_1.addWidget(self.morph_summary_graph_btn)

        self.vSpacer_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vLayout_1.addItem(self.vSpacer_1)


        self.horizontalLayout.addLayout(self.vLayout_1)


        self.verticalLayout.addWidget(self.summary_graph_frame)

        self.info_lbl_2 = QLabel(MoreInfoDialog)
        self.info_lbl_2.setObjectName(u"info_lbl_2")
        self.info_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_2)

        self.timespan_graph_frame = QFrame(MoreInfoDialog)
        self.timespan_graph_frame.setObjectName(u"timespan_graph_frame")
        self.timespan_graph_frame.setFrameShape(QFrame.StyledPanel)
        self.timespan_graph_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.timespan_graph_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vLayout_2 = QVBoxLayout()
        self.vLayout_2.setObjectName(u"vLayout_2")
        self.morph_timespan_graph_btn = QPushButton(self.timespan_graph_frame)
        self.morph_timespan_graph_btn.setObjectName(u"morph_timespan_graph_btn")
        sizePolicy3.setHeightForWidth(self.morph_timespan_graph_btn.sizePolicy().hasHeightForWidth())
        self.morph_timespan_graph_btn.setSizePolicy(sizePolicy3)

        self.vLayout_2.addWidget(self.morph_timespan_graph_btn)

        self.vSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vLayout_2.addItem(self.vSpacer_2)


        self.horizontalLayout_2.addLayout(self.vLayout_2)


        self.verticalLayout.addWidget(self.timespan_graph_frame)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_1.addItem(self.hSpacer_1)

        self.create_report_btn = QPushButton(MoreInfoDialog)
        self.create_report_btn.setObjectName(u"create_report_btn")

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
        self.info_lbl_1.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0434\u043e\u0445\u043e\u0434\u0430", None))
        self.morph_summary_graph_btn.setText("")
        self.info_lbl_2.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0437\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.morph_timespan_graph_btn.setText("")
        self.create_report_btn.setText(QCoreApplication.translate("MoreInfoDialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
    # retranslateUi

