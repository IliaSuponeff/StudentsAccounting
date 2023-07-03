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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1164, 730)
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

        self.unactive_student_choose_box = QComboBox(self.centralwidget)
        self.unactive_student_choose_box.setObjectName(u"unactive_student_choose_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.unactive_student_choose_box.sizePolicy().hasHeightForWidth())
        self.unactive_student_choose_box.setSizePolicy(sizePolicy2)

        self.vLayout_1.addWidget(self.unactive_student_choose_box)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.prev_active_student_btn = QPushButton(self.centralwidget)
        self.prev_active_student_btn.setObjectName(u"prev_active_student_btn")
        sizePolicy1.setHeightForWidth(self.prev_active_student_btn.sizePolicy().hasHeightForWidth())
        self.prev_active_student_btn.setSizePolicy(sizePolicy1)
        self.prev_active_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.prev_active_student_btn)

        self.active_student_choose_box = QComboBox(self.centralwidget)
        self.active_student_choose_box.setObjectName(u"active_student_choose_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.active_student_choose_box.sizePolicy().hasHeightForWidth())
        self.active_student_choose_box.setSizePolicy(sizePolicy3)

        self.hLayout_1.addWidget(self.active_student_choose_box)

        self.next_active_student_btn = QPushButton(self.centralwidget)
        self.next_active_student_btn.setObjectName(u"next_active_student_btn")
        sizePolicy1.setHeightForWidth(self.next_active_student_btn.sizePolicy().hasHeightForWidth())
        self.next_active_student_btn.setSizePolicy(sizePolicy1)
        self.next_active_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.next_active_student_btn)


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
        self.choose_from_date_btn = QPushButton(self.filter_frame)
        self.choose_from_date_btn.setObjectName(u"choose_from_date_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.choose_from_date_btn.sizePolicy().hasHeightForWidth())
        self.choose_from_date_btn.setSizePolicy(sizePolicy6)

        self.gLayout_1.addWidget(self.choose_from_date_btn, 0, 2, 1, 1)

        self.info_lbl_4 = QLabel(self.filter_frame)
        self.info_lbl_4.setObjectName(u"info_lbl_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.info_lbl_4.sizePolicy().hasHeightForWidth())
        self.info_lbl_4.setSizePolicy(sizePolicy7)
        self.info_lbl_4.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.info_lbl_4, 0, 0, 1, 1)

        self.from_date_filter_de = QDateEdit(self.filter_frame)
        self.from_date_filter_de.setObjectName(u"from_date_filter_de")
        sizePolicy3.setHeightForWidth(self.from_date_filter_de.sizePolicy().hasHeightForWidth())
        self.from_date_filter_de.setSizePolicy(sizePolicy3)

        self.gLayout_1.addWidget(self.from_date_filter_de, 0, 1, 1, 1)

        self.to_date_filter_de = QDateEdit(self.filter_frame)
        self.to_date_filter_de.setObjectName(u"to_date_filter_de")
        sizePolicy3.setHeightForWidth(self.to_date_filter_de.sizePolicy().hasHeightForWidth())
        self.to_date_filter_de.setSizePolicy(sizePolicy3)

        self.gLayout_1.addWidget(self.to_date_filter_de, 1, 1, 1, 1)

        self.choose_to_date_btn = QPushButton(self.filter_frame)
        self.choose_to_date_btn.setObjectName(u"choose_to_date_btn")

        self.gLayout_1.addWidget(self.choose_to_date_btn, 1, 2, 1, 1)

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
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.results_all_students.sizePolicy().hasHeightForWidth())
        self.results_all_students.setSizePolicy(sizePolicy8)

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

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(3)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy9)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableWidget)


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
        self.prev_active_student_btn.setText("")
        self.next_active_student_btn.setText("")
        self.student_name_lbl.setText(QCoreApplication.translate("MainWindow", u"StudentName", None))
        self.student_summary_result_lbl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.student_currency_lbl.setText(QCoreApplication.translate("MainWindow", u"BYN", None))
        self.info_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.this_year_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"This year", None))
        self.this_month_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"This month", None))
        self.custom_period_rbtn.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.info_lbl_3.setText(QCoreApplication.translate("MainWindow", u"Custom Period", None))
        self.choose_from_date_btn.setText(QCoreApplication.translate("MainWindow", u"Choose", None))
        self.info_lbl_4.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.choose_to_date_btn.setText(QCoreApplication.translate("MainWindow", u"Choose", None))
        self.info_lbl_5.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.info_lbl_6.setText(QCoreApplication.translate("MainWindow", u"Results for all", None))
        self.add_visit_btn.setText(QCoreApplication.translate("MainWindow", u"Add visit", None))
        self.edit_visit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit visit", None))
        self.del_visit_btn.setText(QCoreApplication.translate("MainWindow", u"Delete visit", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Timespan", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Summary", None));
    # retranslateUi

