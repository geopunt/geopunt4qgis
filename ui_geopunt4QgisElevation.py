# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisElevation.ui'
#
# Created: Wed Jul 16 23:18:53 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_elevationDlg(object):
    def setupUi(self, elevationDlg):
        elevationDlg.setObjectName(_fromUtf8("elevationDlg"))
        elevationDlg.resize(574, 419)
        elevationDlg.setMinimumSize(QtCore.QSize(300, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntElevationSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elevationDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(elevationDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.drawBtn = QtGui.QPushButton(elevationDlg)
        self.drawBtn.setAutoDefault(False)
        self.drawBtn.setObjectName(_fromUtf8("drawBtn"))
        self.horizontalLayout_2.addWidget(self.drawBtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addDHMbtn = QtGui.QPushButton(elevationDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDHMbtn.sizePolicy().hasHeightForWidth())
        self.addDHMbtn.setSizePolicy(sizePolicy)
        self.addDHMbtn.setAutoDefault(False)
        self.addDHMbtn.setDefault(False)
        self.addDHMbtn.setObjectName(_fromUtf8("addDHMbtn"))
        self.horizontalLayout_2.addWidget(self.addDHMbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.graphWgt = QtGui.QWidget(elevationDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWgt.sizePolicy().hasHeightForWidth())
        self.graphWgt.setSizePolicy(sizePolicy)
        self.graphWgt.setObjectName(_fromUtf8("graphWgt"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.graphWgt)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout.addWidget(self.graphWgt)
        self.toolbar = QtGui.QWidget(elevationDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.toolbar)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.nrOfsampleLbl = QtGui.QLabel(self.toolbar)
        self.nrOfsampleLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nrOfsampleLbl.setObjectName(_fromUtf8("nrOfsampleLbl"))
        self.horizontalLayout_4.addWidget(self.nrOfsampleLbl)
        self.nrOfSampleSpin = QtGui.QSpinBox(self.toolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nrOfSampleSpin.sizePolicy().hasHeightForWidth())
        self.nrOfSampleSpin.setSizePolicy(sizePolicy)
        self.nrOfSampleSpin.setSuffix(_fromUtf8(""))
        self.nrOfSampleSpin.setMinimum(10)
        self.nrOfSampleSpin.setMaximum(750)
        self.nrOfSampleSpin.setSingleStep(10)
        self.nrOfSampleSpin.setProperty("value", 50)
        self.nrOfSampleSpin.setObjectName(_fromUtf8("nrOfSampleSpin"))
        self.horizontalLayout_4.addWidget(self.nrOfSampleSpin)
        self.verticalLayout.addWidget(self.toolbar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveLineBtn = QtGui.QPushButton(elevationDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveLineBtn.sizePolicy().hasHeightForWidth())
        self.saveLineBtn.setSizePolicy(sizePolicy)
        self.saveLineBtn.setAutoDefault(False)
        self.saveLineBtn.setObjectName(_fromUtf8("saveLineBtn"))
        self.horizontalLayout.addWidget(self.saveLineBtn)
        self.savePntBtn = QtGui.QPushButton(elevationDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePntBtn.sizePolicy().hasHeightForWidth())
        self.savePntBtn.setSizePolicy(sizePolicy)
        self.savePntBtn.setAutoDefault(False)
        self.savePntBtn.setObjectName(_fromUtf8("savePntBtn"))
        self.horizontalLayout.addWidget(self.savePntBtn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mgsLbl = QtGui.QLabel(elevationDlg)
        self.mgsLbl.setText(_fromUtf8(""))
        self.mgsLbl.setObjectName(_fromUtf8("mgsLbl"))
        self.horizontalLayout_3.addWidget(self.mgsLbl)
        spacerItem3 = QtGui.QSpacerItem(389, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.buttonBox = QtGui.QDialogButtonBox(elevationDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(elevationDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), elevationDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), elevationDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(elevationDlg)

    def retranslateUi(self, elevationDlg):
        elevationDlg.setWindowTitle(_translate("elevationDlg", "Hoogteprofiel", None))
        self.drawBtn.setText(_translate("elevationDlg", "Teken de profiellijn", None))
        self.addDHMbtn.setText(_translate("elevationDlg", "Voeg hoogtemodel toe als laag", None))
        self.nrOfsampleLbl.setText(_translate("elevationDlg", "Aantal profielpunten", None))
        self.saveLineBtn.setText(_translate("elevationDlg", "Profiellijn opslaan ", None))
        self.savePntBtn.setText(_translate("elevationDlg", "Profielpunten opslaan", None))

import resources_rc