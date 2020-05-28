# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 399)
        self.main_layout = QtWidgets.QVBoxLayout(Dialog)
        self.main_layout.setObjectName("main_layout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.mainTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.newWordListWidget = QtWidgets.QListWidget(self.mainTab)
        self.newWordListWidget.setAlternatingRowColors(True)
        self.newWordListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.newWordListWidget.setObjectName("newWordListWidget")
        self.verticalLayout.addWidget(self.newWordListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.deckLayout = QtWidgets.QHBoxLayout()
        self.deckLayout.setObjectName("deckLayout")
        self.deckLabel = QtWidgets.QLabel(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckLabel.sizePolicy().hasHeightForWidth())
        self.deckLabel.setSizePolicy(sizePolicy)
        self.deckLabel.setObjectName("deckLabel")
        self.deckLayout.addWidget(self.deckLabel)
        self.deckComboBox = QtWidgets.QComboBox(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckComboBox.sizePolicy().hasHeightForWidth())
        self.deckComboBox.setSizePolicy(sizePolicy)
        self.deckComboBox.setEditable(True)
        self.deckComboBox.setObjectName("deckComboBox")
        self.deckLayout.addWidget(self.deckComboBox)
        self.gridLayout_4.addLayout(self.deckLayout, 0, 0, 1, 2)
        self.createBtn = QtWidgets.QPushButton(self.mainTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy)
        self.createBtn.setMinimumSize(QtCore.QSize(100, 0))
        self.createBtn.setObjectName("createBtn")
        self.gridLayout_4.addWidget(self.createBtn, 2, 1, 1, 1)
        self.tabWidget.addTab(self.mainTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.defaultConfigGroupBox = QtWidgets.QGroupBox(self.settingTab)
        self.defaultConfigGroupBox.setObjectName("defaultConfigGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.defaultConfigGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.noPronRadioButton = QtWidgets.QRadioButton(self.defaultConfigGroupBox)
        self.noPronRadioButton.setChecked(True)
        self.noPronRadioButton.setObjectName("noPronRadioButton")
        self.gridLayout.addWidget(self.noPronRadioButton, 4, 2, 1, 1)
        self.AmEPronRadioButton = QtWidgets.QRadioButton(self.defaultConfigGroupBox)
        self.AmEPronRadioButton.setObjectName("AmEPronRadioButton")
        self.gridLayout.addWidget(self.AmEPronRadioButton, 4, 1, 1, 1)
        self.AmEPhoneticCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.AmEPhoneticCheckBox.setChecked(True)
        self.AmEPhoneticCheckBox.setObjectName("AmEPhoneticCheckBox")
        self.gridLayout.addWidget(self.AmEPhoneticCheckBox, 0, 2, 1, 1)
        self.BrEPhoneticCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.BrEPhoneticCheckBox.setChecked(True)
        self.BrEPhoneticCheckBox.setObjectName("BrEPhoneticCheckBox")
        self.gridLayout.addWidget(self.BrEPhoneticCheckBox, 0, 1, 1, 1)
        self.BrEPronRadioButton = QtWidgets.QRadioButton(self.defaultConfigGroupBox)
        self.BrEPronRadioButton.setChecked(False)
        self.BrEPronRadioButton.setObjectName("BrEPronRadioButton")
        self.gridLayout.addWidget(self.BrEPronRadioButton, 4, 0, 1, 1)
        self.sentenceCheckBox = QtWidgets.QCheckBox(self.defaultConfigGroupBox)
        self.sentenceCheckBox.setChecked(True)
        self.sentenceCheckBox.setObjectName("sentenceCheckBox")
        self.gridLayout.addWidget(self.sentenceCheckBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.defaultConfigGroupBox, 0, 0, 1, 2)
        self.tabWidget.addTab(self.settingTab, "")
        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")
        self.tabWidget.addTab(self.logTab, "")
        self.main_layout.addWidget(self.tabWidget)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.main_layout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "单词书来源"))
        self.deckLabel.setText(_translate("Dialog", "牌组"))
        self.createBtn.setText(_translate("Dialog", "创建单词书"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Dialog", "同步"))
        self.defaultConfigGroupBox.setTitle(_translate("Dialog", "默认设置"))
        self.noPronRadioButton.setText(_translate("Dialog", "无发音"))
        self.AmEPronRadioButton.setText(_translate("Dialog", "美式发音"))
        self.AmEPhoneticCheckBox.setText(_translate("Dialog", "美式英标"))
        self.BrEPhoneticCheckBox.setText(_translate("Dialog", "英式英标"))
        self.BrEPronRadioButton.setText(_translate("Dialog", "英式发音"))
        self.sentenceCheckBox.setText(_translate("Dialog", "例句"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("Dialog", "设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), _translate("Dialog", "日志"))