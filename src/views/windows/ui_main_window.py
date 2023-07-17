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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(1000, 740))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.help_action = QAction(MainWindow)
        self.help_action.setObjectName(u"help_action")
        self.about_authors_action = QAction(MainWindow)
        self.about_authors_action.setObjectName(u"about_authors_action")
        self.close_action = QAction(MainWindow)
        self.close_action.setObjectName(u"close_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.vLine_2 = QFrame(self.centralwidget)
        self.vLine_2.setObjectName(u"vLine_2")
        self.vLine_2.setFrameShape(QFrame.VLine)
        self.vLine_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.vLine_2)

        self.tools_frame = QFrame(self.centralwidget)
        self.tools_frame.setObjectName(u"tools_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools_frame.sizePolicy().hasHeightForWidth())
        self.tools_frame.setSizePolicy(sizePolicy)
        self.vLayout_1 = QVBoxLayout(self.tools_frame)
        self.vLayout_1.setObjectName(u"vLayout_1")
        self.hLayout_2 = QHBoxLayout()
        self.hLayout_2.setObjectName(u"hLayout_2")
        self.add_student_btn = QPushButton(self.tools_frame)
        self.add_student_btn.setObjectName(u"add_student_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_student_btn.sizePolicy().hasHeightForWidth())
        self.add_student_btn.setSizePolicy(sizePolicy1)
        self.add_student_btn.setIconSize(QSize(30, 30))
        self.add_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.add_student_btn)

        self.edit_student_btn = QPushButton(self.tools_frame)
        self.edit_student_btn.setObjectName(u"edit_student_btn")
        sizePolicy1.setHeightForWidth(self.edit_student_btn.sizePolicy().hasHeightForWidth())
        self.edit_student_btn.setSizePolicy(sizePolicy1)
        self.edit_student_btn.setIconSize(QSize(30, 30))
        self.edit_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.edit_student_btn)

        self.del_student_btn = QPushButton(self.tools_frame)
        self.del_student_btn.setObjectName(u"del_student_btn")
        sizePolicy1.setHeightForWidth(self.del_student_btn.sizePolicy().hasHeightForWidth())
        self.del_student_btn.setSizePolicy(sizePolicy1)
        self.del_student_btn.setIconSize(QSize(30, 30))
        self.del_student_btn.setFlat(True)

        self.hLayout_2.addWidget(self.del_student_btn)


        self.vLayout_1.addLayout(self.hLayout_2)

        self.hLayout_1 = QHBoxLayout()
        self.hLayout_1.setObjectName(u"hLayout_1")
        self.prev_student_btn = QPushButton(self.tools_frame)
        self.prev_student_btn.setObjectName(u"prev_student_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.prev_student_btn.sizePolicy().hasHeightForWidth())
        self.prev_student_btn.setSizePolicy(sizePolicy2)
        self.prev_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.prev_student_btn)

        self.student_choose_box = QComboBox(self.tools_frame)
        self.student_choose_box.setObjectName(u"student_choose_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.student_choose_box.sizePolicy().hasHeightForWidth())
        self.student_choose_box.setSizePolicy(sizePolicy3)
        self.student_choose_box.setInsertPolicy(QComboBox.InsertAtBottom)
        self.student_choose_box.setFrame(True)

        self.hLayout_1.addWidget(self.student_choose_box)

        self.reload_student_btn = QPushButton(self.tools_frame)
        self.reload_student_btn.setObjectName(u"reload_student_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.reload_student_btn.sizePolicy().hasHeightForWidth())
        self.reload_student_btn.setSizePolicy(sizePolicy4)
        self.reload_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.reload_student_btn)

        self.next_student_btn = QPushButton(self.tools_frame)
        self.next_student_btn.setObjectName(u"next_student_btn")
        sizePolicy2.setHeightForWidth(self.next_student_btn.sizePolicy().hasHeightForWidth())
        self.next_student_btn.setSizePolicy(sizePolicy2)
        self.next_student_btn.setFlat(True)

        self.hLayout_1.addWidget(self.next_student_btn)


        self.vLayout_1.addLayout(self.hLayout_1)

        self.hLine_2 = QFrame(self.tools_frame)
        self.hLine_2.setObjectName(u"hLine_2")
        self.hLine_2.setFrameShape(QFrame.HLine)
        self.hLine_2.setFrameShadow(QFrame.Sunken)

        self.vLayout_1.addWidget(self.hLine_2)

        self.student_name_lbl = QLabel(self.tools_frame)
        self.student_name_lbl.setObjectName(u"student_name_lbl")
        self.student_name_lbl.setAlignment(Qt.AlignCenter)

        self.vLayout_1.addWidget(self.student_name_lbl)

        self.gLayout_3 = QGridLayout()
        self.gLayout_3.setObjectName(u"gLayout_3")
        self.summary_timespan_result_lbl = QLabel(self.tools_frame)
        self.summary_timespan_result_lbl.setObjectName(u"summary_timespan_result_lbl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.summary_timespan_result_lbl.sizePolicy().hasHeightForWidth())
        self.summary_timespan_result_lbl.setSizePolicy(sizePolicy5)
        self.summary_timespan_result_lbl.setAlignment(Qt.AlignCenter)

        self.gLayout_3.addWidget(self.summary_timespan_result_lbl, 2, 1, 1, 1)

        self.info_lbl_7 = QLabel(self.tools_frame)
        self.info_lbl_7.setObjectName(u"info_lbl_7")
        self.info_lbl_7.setAlignment(Qt.AlignCenter)

        self.gLayout_3.addWidget(self.info_lbl_7, 1, 0, 1, 1)

        self.info_lbl_8 = QLabel(self.tools_frame)
        self.info_lbl_8.setObjectName(u"info_lbl_8")
        self.info_lbl_8.setAlignment(Qt.AlignCenter)

        self.gLayout_3.addWidget(self.info_lbl_8, 2, 0, 1, 1)

        self.info_lbl_1 = QLabel(self.tools_frame)
        self.info_lbl_1.setObjectName(u"info_lbl_1")
        self.info_lbl_1.setAlignment(Qt.AlignCenter)

        self.gLayout_3.addWidget(self.info_lbl_1, 0, 0, 1, 1)

        self.period_info_lbl = QLabel(self.tools_frame)
        self.period_info_lbl.setObjectName(u"period_info_lbl")
        self.period_info_lbl.setAlignment(Qt.AlignCenter)

        self.gLayout_3.addWidget(self.period_info_lbl, 0, 1, 1, 1)

        self.student_summary_result_lbl = QLabel(self.tools_frame)
        self.student_summary_result_lbl.setObjectName(u"student_summary_result_lbl")
        sizePolicy5.setHeightForWidth(self.student_summary_result_lbl.sizePolicy().hasHeightForWidth())
        self.student_summary_result_lbl.setSizePolicy(sizePolicy5)
        self.student_summary_result_lbl.setAlignment(Qt.AlignCenter)

        self.gLayout_3.addWidget(self.student_summary_result_lbl, 1, 1, 1, 1)


        self.vLayout_1.addLayout(self.gLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hSpacer_3)

        self.filter_frame = QFrame(self.tools_frame)
        self.filter_frame.setObjectName(u"filter_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.filter_frame.sizePolicy().hasHeightForWidth())
        self.filter_frame.setSizePolicy(sizePolicy6)
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

        self.gLayout_2 = QGridLayout()
        self.gLayout_2.setObjectName(u"gLayout_2")
        self.this_year_filter_rbtn = QRadioButton(self.filter_frame)
        self.this_year_filter_rbtn.setObjectName(u"this_year_filter_rbtn")
        self.this_year_filter_rbtn.setChecked(False)

        self.gLayout_2.addWidget(self.this_year_filter_rbtn, 0, 0, 1, 1)

        self.this_month_filter_rbtn = QRadioButton(self.filter_frame)
        self.this_month_filter_rbtn.setObjectName(u"this_month_filter_rbtn")

        self.gLayout_2.addWidget(self.this_month_filter_rbtn, 0, 1, 1, 1)

        self.all_days_filter_rbtn = QRadioButton(self.filter_frame)
        self.all_days_filter_rbtn.setObjectName(u"all_days_filter_rbtn")
        self.all_days_filter_rbtn.setChecked(True)

        self.gLayout_2.addWidget(self.all_days_filter_rbtn, 1, 0, 1, 1)

        self.custom_period_rbtn = QRadioButton(self.filter_frame)
        self.custom_period_rbtn.setObjectName(u"custom_period_rbtn")

        self.gLayout_2.addWidget(self.custom_period_rbtn, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gLayout_2)

        self.info_lbl_3 = QLabel(self.filter_frame)
        self.info_lbl_3.setObjectName(u"info_lbl_3")
        self.info_lbl_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.info_lbl_3)

        self.gLayout_1 = QGridLayout()
        self.gLayout_1.setObjectName(u"gLayout_1")
        self.info_lbl_4 = QLabel(self.filter_frame)
        self.info_lbl_4.setObjectName(u"info_lbl_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.info_lbl_4.sizePolicy().hasHeightForWidth())
        self.info_lbl_4.setSizePolicy(sizePolicy7)
        self.info_lbl_4.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.info_lbl_4, 0, 0, 1, 1)

        self.info_lbl_5 = QLabel(self.filter_frame)
        self.info_lbl_5.setObjectName(u"info_lbl_5")
        self.info_lbl_5.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.info_lbl_5, 1, 0, 1, 1)

        self.choose_from_date_btn = QPushButton(self.filter_frame)
        self.choose_from_date_btn.setObjectName(u"choose_from_date_btn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.choose_from_date_btn.sizePolicy().hasHeightForWidth())
        self.choose_from_date_btn.setSizePolicy(sizePolicy8)
        self.choose_from_date_btn.setFlat(False)

        self.gLayout_1.addWidget(self.choose_from_date_btn, 0, 2, 1, 1)

        self.choose_to_date_btn = QPushButton(self.filter_frame)
        self.choose_to_date_btn.setObjectName(u"choose_to_date_btn")
        sizePolicy8.setHeightForWidth(self.choose_to_date_btn.sizePolicy().hasHeightForWidth())
        self.choose_to_date_btn.setSizePolicy(sizePolicy8)
        self.choose_to_date_btn.setFlat(False)

        self.gLayout_1.addWidget(self.choose_to_date_btn, 1, 2, 1, 1)

        self.from_date_lbl = QLabel(self.filter_frame)
        self.from_date_lbl.setObjectName(u"from_date_lbl")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.from_date_lbl.sizePolicy().hasHeightForWidth())
        self.from_date_lbl.setSizePolicy(sizePolicy9)
        self.from_date_lbl.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.from_date_lbl, 0, 1, 1, 1)

        self.to_date_lbl = QLabel(self.filter_frame)
        self.to_date_lbl.setObjectName(u"to_date_lbl")
        sizePolicy9.setHeightForWidth(self.to_date_lbl.sizePolicy().hasHeightForWidth())
        self.to_date_lbl.setSizePolicy(sizePolicy9)
        self.to_date_lbl.setAlignment(Qt.AlignCenter)

        self.gLayout_1.addWidget(self.to_date_lbl, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gLayout_1)


        self.horizontalLayout.addWidget(self.filter_frame)

        self.hSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.hSpacer_2)


        self.vLayout_1.addLayout(self.horizontalLayout)

        self.hLine_1 = QFrame(self.tools_frame)
        self.hLine_1.setObjectName(u"hLine_1")
        self.hLine_1.setFrameShape(QFrame.HLine)
        self.hLine_1.setFrameShadow(QFrame.Sunken)

        self.vLayout_1.addWidget(self.hLine_1)

        self.info_lbl_6 = QLabel(self.tools_frame)
        self.info_lbl_6.setObjectName(u"info_lbl_6")
        self.info_lbl_6.setFrameShadow(QFrame.Plain)
        self.info_lbl_6.setAlignment(Qt.AlignCenter)

        self.vLayout_1.addWidget(self.info_lbl_6)

        self.all_results_table_view = QTableView(self.tools_frame)
        self.all_results_table_view.setObjectName(u"all_results_table_view")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(2)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.all_results_table_view.sizePolicy().hasHeightForWidth())
        self.all_results_table_view.setSizePolicy(sizePolicy10)

        self.vLayout_1.addWidget(self.all_results_table_view)


        self.horizontalLayout_3.addWidget(self.tools_frame)

        self.vLine_1 = QFrame(self.centralwidget)
        self.vLine_1.setObjectName(u"vLine_1")
        self.vLine_1.setFrameShape(QFrame.VLine)
        self.vLine_1.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.vLine_1)

        self.workspace_frame = QFrame(self.centralwidget)
        self.workspace_frame.setObjectName(u"workspace_frame")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(5)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.workspace_frame.sizePolicy().hasHeightForWidth())
        self.workspace_frame.setSizePolicy(sizePolicy11)
        self.verticalLayout_3 = QVBoxLayout(self.workspace_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.hLayout_3 = QHBoxLayout()
        self.hLayout_3.setObjectName(u"hLayout_3")
        self.hSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_3.addItem(self.hSpacer_1)

        self.theme_change_btn = QPushButton(self.workspace_frame)
        self.theme_change_btn.setObjectName(u"theme_change_btn")
        sizePolicy6.setHeightForWidth(self.theme_change_btn.sizePolicy().hasHeightForWidth())
        self.theme_change_btn.setSizePolicy(sizePolicy6)

        self.hLayout_3.addWidget(self.theme_change_btn)


        self.verticalLayout_3.addLayout(self.hLayout_3)

        self.visits_info_frame = QFrame(self.workspace_frame)
        self.visits_info_frame.setObjectName(u"visits_info_frame")
        sizePolicy.setHeightForWidth(self.visits_info_frame.sizePolicy().hasHeightForWidth())
        self.visits_info_frame.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.visits_info_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hLayout_5 = QHBoxLayout()
        self.hLayout_5.setObjectName(u"hLayout_5")
        self.add_visit_btn = QPushButton(self.visits_info_frame)
        self.add_visit_btn.setObjectName(u"add_visit_btn")
        self.add_visit_btn.setFlat(False)

        self.hLayout_5.addWidget(self.add_visit_btn)

        self.edit_visit_btn = QPushButton(self.visits_info_frame)
        self.edit_visit_btn.setObjectName(u"edit_visit_btn")
        self.edit_visit_btn.setFlat(False)

        self.hLayout_5.addWidget(self.edit_visit_btn)

        self.del_visit_btn = QPushButton(self.visits_info_frame)
        self.del_visit_btn.setObjectName(u"del_visit_btn")
        self.del_visit_btn.setFlat(False)

        self.hLayout_5.addWidget(self.del_visit_btn)


        self.verticalLayout_2.addLayout(self.hLayout_5)

        self.student_visits_table_view = QTableView(self.visits_info_frame)
        self.student_visits_table_view.setObjectName(u"student_visits_table_view")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(3)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.student_visits_table_view.sizePolicy().hasHeightForWidth())
        self.student_visits_table_view.setSizePolicy(sizePolicy12)

        self.verticalLayout_2.addWidget(self.student_visits_table_view)


        self.verticalLayout_3.addWidget(self.visits_info_frame)


        self.horizontalLayout_3.addWidget(self.workspace_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"StudentAccounting", None))
        self.help_action.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about_authors_action.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.close_action.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.add_student_btn.setText("")
        self.edit_student_btn.setText("")
        self.del_student_btn.setText("")
        self.prev_student_btn.setText("")
        self.reload_student_btn.setText("")
        self.next_student_btn.setText("")
        self.student_name_lbl.setText(QCoreApplication.translate("MainWindow", u"StudentName", None))
        self.summary_timespan_result_lbl.setText(QCoreApplication.translate("MainWindow", u"0 \u0447\u0430\u0441\u043e\u0432", None))
        self.info_lbl_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434", None))
        self.info_lbl_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.info_lbl_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.period_info_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0434\u043d\u0438", None))
        self.student_summary_result_lbl.setText(QCoreApplication.translate("MainWindow", u"0 BYN", None))
        self.info_lbl_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.this_year_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0442\u043e\u0442 \u0433\u043e\u0434", None))
        self.this_month_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0442\u043e\u0442 \u043c\u0435\u0441\u044f\u0446", None))
        self.all_days_filter_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0434\u043d\u0438", None))
        self.custom_period_rbtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.info_lbl_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.info_lbl_4.setText(QCoreApplication.translate("MainWindow", u"\u0421 ", None))
        self.info_lbl_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e", None))
        self.choose_from_date_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.choose_to_date_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.from_date_lbl.setText(QCoreApplication.translate("MainWindow", u"%d.%.m.Y", None))
        self.to_date_lbl.setText(QCoreApplication.translate("MainWindow", u"%d.%.m.Y", None))
        self.info_lbl_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e\u0432\u044b\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.theme_change_btn.setText("")
        self.add_visit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.edit_visit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.del_visit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435", None))
    # retranslateUi

