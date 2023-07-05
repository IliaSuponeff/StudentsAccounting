# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QSize(960, 640))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vLayout_1 = QVBoxLayout()
        self.vLayout_1.setObjectName(u"vLayout_1")
        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.add_student_btn = QPushButton(self.centralwidget)
        self.add_student_btn.setObjectName(u"add_student_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_student_btn.sizePolicy().hasHeightForWidth())
        self.add_student_btn.setSizePolicy(sizePolicy)
        self.add_student_btn.setIconSize(QSize(30, 30))
        self.add_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.add_student_btn)

        self.edit_student_btn = QPushButton(self.centralwidget)
        self.edit_student_btn.setObjectName(u"edit_student_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.edit_student_btn.sizePolicy().hasHeightForWidth())
        self.edit_student_btn.setSizePolicy(sizePolicy1)
        self.edit_student_btn.setIconSize(QSize(30, 30))
        self.edit_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.edit_student_btn)

        self.del_student_btn = QPushButton(self.centralwidget)
        self.del_student_btn.setObjectName(u"del_student_btn")
        sizePolicy.setHeightForWidth(self.del_student_btn.sizePolicy().hasHeightForWidth())
        self.del_student_btn.setSizePolicy(sizePolicy)
        self.del_student_btn.setIconSize(QSize(30, 30))
        self.del_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.del_student_btn)


        self.vLayout_1.addLayout(self.hLayout_2)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.prev_student_btn = QPushButton(self.centralwidget)
        self.prev_student_btn.setObjectName(u"prev_student_btn")
        sizePolicy1.setHeightForWidth(self.prev_student_btn.sizePolicy().hasHeightForWidth())
        self.prev_student_btn.setSizePolicy(sizePolicy1)
        self.prev_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.prev_student_btn)

        self.student_choose_box = QComboBox(self.centralwidget)
        self.student_choose_box.setObjectName(u"student_choose_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.student_choose_box.sizePolicy().hasHeightForWidth())
        self.student_choose_box.setSizePolicy(sizePolicy2)

        self.hLayout_1.addWidget(self.student_choose_box)

        self.reload_student_btn = QPushButton(self.centralwidget)
        self.reload_student_btn.setObjectName(u"reload_student_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reload_student_btn.sizePolicy().hasHeightForWidth())
        self.reload_student_btn.setSizePolicy(sizePolicy3)
        self.reload_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.reload_student_btn)

        self.next_student_btn = QPushButton(self.centralwidget)
        self.next_student_btn.setObjectName(u"next_student_btn")
        sizePolicy1.setHeightForWidth(self.next_student_btn.sizePolicy().hasHeightForWidth())
        self.next_student_btn.setSizePolicy(sizePolicy1)
        self.next_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.next_student_btn)


        self.vLayout_1.addLayout(self.hLayout_1)

        self.student_name_lbl = QLabel(self.centralwidget)
        self.student_name_lbl.setObjectName(u"student_name_lbl")
        self.student_name_lbl.setAlignment(Qt.AlignCenter)

        self.vLayout_1.addWidget(self.student_name_lbl)

        self.hLayout_3 = QHBoxLayout()
        self.hLayout_3.setObjectName(u"hLayout_3")
        self.student_summary_result_lbl = QLabel(self.centralwidget)
        self.student_summary_result_lbl.setObjectName(u"student_summary_result_lbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.student_summary_result_lbl.sizePolicy().hasHeightForWidth())
        self.student_summary_result_lbl.setSizePolicy(sizePolicy4)
        self.student_summary_result_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hLayout_3.addWidget(self.student_summary_result_lbl)

        self.student_currency_lbl = QLabel(self.centralwidget)
        self.student_currency_lbl.setObjectName(u"student_currency_lbl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.student_currency_lbl.sizePolicy().hasHeightForWidth())
        self.student_currency_lbl.setSizePolicy(sizePolicy5)
        self.student_currency_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hLayout_3.addWidget(self.student_currency_lbl)


        self.vLayout_1.addLayout(self.hLayout_3)

        self.filter_frame = QFrame(self.centralwidget)
        self.filter_frame.setObjectName(u"filter_frame")
        self.filter_frame.setFrameShape(QFrame.WinPanel)
        self.filter_frame.setFrameShadow(QFrame.Plain)
        self.filter_frame.setLineWidth(1)
        self.filter_frame.setMidLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.filter_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_lbl_2 = QLabel(self.filter_frame)
        self.info_lbl_2.setObjectName(u"info_lbl_2")
        self.info_lbl_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_2)

        self.hLayout_4 = QHBoxLayout()
        self.hLayout_4.setObjectName(u"hLayout_4")
        self.this_year_filter_rbtn = QRadioButton(self.filter_frame)
        self.this_year_filter_rbtn.setObjectName(u"this_year_filter_rbtn")
        self.this_year_filter_rbtn.setChecked(True)

        self.hLayout_4.addWidget(self.this_year_filter_rbtn)

        self.this_month_filter_rbtn = QRadioButton(self.filter_frame)
        self.this_month_filter_rbtn.setObjectName(u"this_month_filter_rbtn")

        self.hLayout_4.addWidget(self.this_month_filter_rbtn)

        self.custom_period_rbtn = QRadioButton(self.filter_frame)
        self.custom_period_rbtn.setObjectName(u"custom_period_rbtn")

        self.hLayout_4.addWidget(self.custom_period_rbtn)


        self.verticalLayout.addLayout(self.hLayout_4)

        self.info_lbl_3 = QLabel(self.filter_frame)
        self.info_lbl_3.setObjectName(u"info_lbl_3")
        self.info_lbl_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_3)

        self.gLayout_1 = QGridLayout()
        self.gLayout_1.setObjectName(u"gLayout_1")
        self.info_lbl_4 = QLabel(self.filter_frame)
        self.info_lbl_4.setObjectName(u"info_lbl_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.info_lbl_4.sizePolicy().hasHeightForWidth())
        self.info_lbl_4.setSizePolicy(sizePolicy6)
        self.info_lbl_4.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.info_lbl_4, 0, 0, 1, 1)

        self.from_date_filter_de = QDateEdit(self.filter_frame)
        self.from_date_filter_de.setObjectName(u"from_date_filter_de")
        sizePolicy2.setHeightForWidth(self.from_date_filter_de.sizePolicy().hasHeightForWidth())
        self.from_date_filter_de.setSizePolicy(sizePolicy2)
        self.from_date_filter_de.setAlignment(Qt.AlignCenter)
        self.from_date_filter_de.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.from_date_filter_de.setCalendarPopup(True)

        self.gLayout_1.addWidget(self.from_date_filter_de, 0, 1, 1, 1)

        self.to_date_filter_de = QDateEdit(self.filter_frame)
        self.to_date_filter_de.setObjectName(u"to_date_filter_de")
        sizePolicy2.setHeightForWidth(self.to_date_filter_de.sizePolicy().hasHeightForWidth())
        self.to_date_filter_de.setSizePolicy(sizePolicy2)
        self.to_date_filter_de.setAlignment(Qt.AlignCenter)
        self.to_date_filter_de.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.to_date_filter_de.setCalendarPopup(True)

        self.gLayout_1.addWidget(self.to_date_filter_de, 1, 1, 1, 1)

        self.info_lbl_5 = QLabel(self.filter_frame)
        self.info_lbl_5.setObjectName(u"info_lbl_5")
        self.info_lbl_5.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.info_lbl_5, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gLayout_1)


        self.vLayout_1.addWidget(self.filter_frame)

        self.info_lbl_6 = QLabel(self.centralwidget)
        self.info_lbl_6.setObjectName(u"info_lbl_6")
        self.info_lbl_6.setFrameShadow(QFrame.Plain)
        self.info_lbl_6.setAlignment(Qt.AlignCenter)

        self.vLayout_1.addWidget(self.info_lbl_6)

        self.results_all_students = QListWidget(self.centralwidget)
        self.results_all_students.setObjectName(u"results_all_students")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.results_all_students.sizePolicy().hasHeightForWidth())
        self.results_all_students.setSizePolicy(sizePolicy7)

        self.vLayout_1.addWidget(self.results_all_students)


        self.horizontalLayout.addLayout(self.vLayout_1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hLayout_5 = QHBoxLayout()
        self.hLayout_5.setObjectName(u"hLayout_5")
        self.add_visit_btn = QPushButton(self.centralwidget)
        self.add_visit_btn.setObjectName(u"add_visit_btn")

        self.hLayout_5.addWidget(self.add_visit_btn)

        self.edit_visit_btn = QPushButton(self.centralwidget)
        self.edit_visit_btn.setObjectName(u"edit_visit_btn")

        self.hLayout_5.addWidget(self.edit_visit_btn)

        self.del_visit_btn = QPushButton(self.centralwidget)
        self.del_visit_btn.setObjectName(u"del_visit_btn")

        self.hLayout_5.addWidget(self.del_visit_btn)


        self.verticalLayout_2.addLayout(self.hLayout_5)

        self.student_visits_table_view = QTableView(self.centralwidget)
        self.student_visits_table_view.setObjectName(u"student_visits_table_view")

        self.verticalLayout_2.addWidget(self.student_visits_table_view)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"StudentAccounting", None))
        self.add_student_btn.setText("")
        self.edit_student_btn.setText("")
        self.del_student_btn.setText("")
        self.prev_student_btn.setText("")
        self.reload_student_btn.setText("")
        self.next_student_btn.setText("")
        self.student_name_lbl.setText(QCoreApplication.translate("MainWindow", u"StudentName", None))
        self.student_summary_result_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.student_currency_lbl.setText(QCoreApplication.translate("MainWindow", u"BYN", None))
        self.info_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.this_year_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"This year", None))
        self.this_month_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"This month", None))
        self.custom_period_rbtn.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.info_lbl_3.setText(QCoreApplication.translate("MainWindow", u"Custom Period", None))
        self.info_lbl_4.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.info_lbl_5.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.info_lbl_6.setText(QCoreApplication.translate("MainWindow", u"Results for all", None))
        self.add_visit_btn.setText(QCoreApplication.translate("MainWindow", u"Add visit", None))
        self.edit_visit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit visit", None))
        self.del_visit_btn.setText(QCoreApplication.translate("MainWindow", u"Delete visit", None))
    # retranslateUi

