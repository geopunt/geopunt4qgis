# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisBatchGeoCode.ui'
#
# Created: Sun Jan  5 18:06:43 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_batchGeocodeDlg(object):
    def setupUi(self, batchGeocodeDlg):
        batchGeocodeDlg.setObjectName(_fromUtf8("batchGeocodeDlg"))
        batchGeocodeDlg.resize(531, 457)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntBatchgeocodeSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        batchGeocodeDlg.setWindowIcon(icon)
        batchGeocodeDlg.setWindowOpacity(1.0)
        batchGeocodeDlg.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(batchGeocodeDlg)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.inputWgt = QtGui.QWidget(batchGeocodeDlg)
        self.inputWgt.setObjectName(_fromUtf8("inputWgt"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.inputWgt)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputTxt = QtGui.QLineEdit(self.inputWgt)
        self.inputTxt.setEnabled(True)
        self.inputTxt.setMinimumSize(QtCore.QSize(200, 0))
        self.inputTxt.setObjectName(_fromUtf8("inputTxt"))
        self.horizontalLayout.addWidget(self.inputTxt)
        self.inputBtn = QtGui.QPushButton(self.inputWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputBtn.sizePolicy().hasHeightForWidth())
        self.inputBtn.setSizePolicy(sizePolicy)
        self.inputBtn.setAutoDefault(False)
        self.inputBtn.setDefault(False)
        self.inputBtn.setFlat(False)
        self.inputBtn.setObjectName(_fromUtf8("inputBtn"))
        self.horizontalLayout.addWidget(self.inputBtn)
        self.verticalLayout.addWidget(self.inputWgt)
        self.delimWgt = QtGui.QWidget(batchGeocodeDlg)
        self.delimWgt.setObjectName(_fromUtf8("delimWgt"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.delimWgt)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_1 = QtGui.QLabel(self.delimWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout_2.addWidget(self.label_1)
        self.delimSelect = QtGui.QComboBox(self.delimWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delimSelect.sizePolicy().hasHeightForWidth())
        self.delimSelect.setSizePolicy(sizePolicy)
        self.delimSelect.setObjectName(_fromUtf8("delimSelect"))
        self.delimSelect.addItem(_fromUtf8(""))
        self.delimSelect.addItem(_fromUtf8(""))
        self.delimSelect.addItem(_fromUtf8(""))
        self.delimSelect.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.delimSelect)
        self.delimEdit = QtGui.QLineEdit(self.delimWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delimEdit.sizePolicy().hasHeightForWidth())
        self.delimEdit.setSizePolicy(sizePolicy)
        self.delimEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.delimEdit.setText(_fromUtf8(""))
        self.delimEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.delimEdit.setObjectName(_fromUtf8("delimEdit"))
        self.horizontalLayout_2.addWidget(self.delimEdit)
        self.verticalLayout.addWidget(self.delimWgt)
        self.adresWgt = QtGui.QWidget(batchGeocodeDlg)
        self.adresWgt.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adresWgt.sizePolicy().hasHeightForWidth())
        self.adresWgt.setSizePolicy(sizePolicy)
        self.adresWgt.setObjectName(_fromUtf8("adresWgt"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.adresWgt)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.adresWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.adresColSelect = QtGui.QComboBox(self.adresWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adresColSelect.sizePolicy().hasHeightForWidth())
        self.adresColSelect.setSizePolicy(sizePolicy)
        self.adresColSelect.setObjectName(_fromUtf8("adresColSelect"))
        self.horizontalLayout_4.addWidget(self.adresColSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.adresWgt)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.huisnrSelect = QtGui.QComboBox(self.adresWgt)
        self.huisnrSelect.setObjectName(_fromUtf8("huisnrSelect"))
        self.horizontalLayout_6.addWidget(self.huisnrSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.adresWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.gemeenteColSelect = QtGui.QComboBox(self.adresWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gemeenteColSelect.sizePolicy().hasHeightForWidth())
        self.gemeenteColSelect.setSizePolicy(sizePolicy)
        self.gemeenteColSelect.setObjectName(_fromUtf8("gemeenteColSelect"))
        self.horizontalLayout_3.addWidget(self.gemeenteColSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.validateBtn = QtGui.QPushButton(self.adresWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateBtn.sizePolicy().hasHeightForWidth())
        self.validateBtn.setSizePolicy(sizePolicy)
        self.validateBtn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.validateBtn.setAutoDefault(True)
        self.validateBtn.setObjectName(_fromUtf8("validateBtn"))
        self.horizontalLayout_5.addWidget(self.validateBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.adresWgt)
        self.outPutTbl = QtGui.QTableWidget(batchGeocodeDlg)
        self.outPutTbl.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.outPutTbl.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.outPutTbl.setObjectName(_fromUtf8("outPutTbl"))
        self.outPutTbl.setColumnCount(0)
        self.outPutTbl.setRowCount(0)
        self.verticalLayout.addWidget(self.outPutTbl)
        self.buttonWgt = QtGui.QWidget(batchGeocodeDlg)
        self.buttonWgt.setObjectName(_fromUtf8("buttonWgt"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.buttonWgt)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout.addWidget(self.buttonWgt)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.addToMapKnop = QtGui.QPushButton(batchGeocodeDlg)
        self.addToMapKnop.setEnabled(False)
        self.addToMapKnop.setCheckable(False)
        self.addToMapKnop.setAutoDefault(True)
        self.addToMapKnop.setDefault(False)
        self.addToMapKnop.setFlat(False)
        self.addToMapKnop.setObjectName(_fromUtf8("addToMapKnop"))
        self.horizontalLayout_9.addWidget(self.addToMapKnop)
        self.buttonBox = QtGui.QDialogButtonBox(batchGeocodeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.line = QtGui.QFrame(batchGeocodeDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.statusBar = QtGui.QWidget(batchGeocodeDlg)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.statusBar)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.statusMsg = QtGui.QLabel(self.statusBar)
        self.statusMsg.setFrameShape(QtGui.QFrame.Panel)
        self.statusMsg.setFrameShadow(QtGui.QFrame.Sunken)
        self.statusMsg.setText(_fromUtf8(""))
        self.statusMsg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusMsg.setObjectName(_fromUtf8("statusMsg"))
        self.horizontalLayout_8.addWidget(self.statusMsg)
        self.statusProgress = QtGui.QProgressBar(self.statusBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusProgress.sizePolicy().hasHeightForWidth())
        self.statusProgress.setSizePolicy(sizePolicy)
        self.statusProgress.setMinimumSize(QtCore.QSize(200, 0))
        self.statusProgress.setMaximum(10)
        self.statusProgress.setProperty("value", 0)
        self.statusProgress.setTextVisible(True)
        self.statusProgress.setInvertedAppearance(False)
        self.statusProgress.setObjectName(_fromUtf8("statusProgress"))
        self.horizontalLayout_8.addWidget(self.statusProgress)
        self.verticalLayout.addWidget(self.statusBar)

        self.retranslateUi(batchGeocodeDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), batchGeocodeDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(batchGeocodeDlg)

    def retranslateUi(self, batchGeocodeDlg):
        batchGeocodeDlg.setWindowTitle(_translate("batchGeocodeDlg", "Batch geocodeer adressen", None))
        self.inputBtn.setText(_translate("batchGeocodeDlg", "Open", None))
        self.label_1.setText(_translate("batchGeocodeDlg", "Separator: ", None))
        self.delimSelect.setItemText(0, _translate("batchGeocodeDlg", "Puntcomma", None))
        self.delimSelect.setItemText(1, _translate("batchGeocodeDlg", "Comma", None))
        self.delimSelect.setItemText(2, _translate("batchGeocodeDlg", "Tab", None))
        self.delimSelect.setItemText(3, _translate("batchGeocodeDlg", "Ander: ", None))
        self.label_2.setText(_translate("batchGeocodeDlg", "Adres (straat <huisnr>, <gemeente>):", None))
        self.label_3.setText(_translate("batchGeocodeDlg", "(Optioneel) Huisnummer kolom: ", None))
        self.label.setText(_translate("batchGeocodeDlg", "(Optioneel) Gemeente kolom:", None))
        self.validateBtn.setText(_translate("batchGeocodeDlg", "Valideer", None))
        self.outPutTbl.setSortingEnabled(True)
        self.addToMapKnop.setText(_translate("batchGeocodeDlg", "Voeg valide adressen toe aan de kaart", None))

import resources_rc
