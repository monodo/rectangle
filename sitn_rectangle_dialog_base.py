# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projets\rectangle\sitnRectangle\sitn_rectangle_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_sitnRectangleDialogBase(object):
    def setupUi(self, sitnRectangleDialogBase):
        sitnRectangleDialogBase.setObjectName(_fromUtf8("sitnRectangleDialogBase"))
        sitnRectangleDialogBase.resize(420, 300)
        self.gridLayout = QtGui.QGridLayout(sitnRectangleDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(sitnRectangleDialogBase)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.llnorth = QtGui.QLineEdit(sitnRectangleDialogBase)
        self.llnorth.setObjectName(_fromUtf8("llnorth"))
        self.gridLayout.addWidget(self.llnorth, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(sitnRectangleDialogBase)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.urnorth = QtGui.QLineEdit(sitnRectangleDialogBase)
        self.urnorth.setObjectName(_fromUtf8("urnorth"))
        self.gridLayout.addWidget(self.urnorth, 5, 1, 1, 1)
        self.lleast = QtGui.QLineEdit(sitnRectangleDialogBase)
        self.lleast.setObjectName(_fromUtf8("lleast"))
        self.gridLayout.addWidget(self.lleast, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(sitnRectangleDialogBase)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.ureast = QtGui.QLineEdit(sitnRectangleDialogBase)
        self.ureast.setObjectName(_fromUtf8("ureast"))
        self.gridLayout.addWidget(self.ureast, 3, 1, 1, 1)
        self.label = QtGui.QLabel(sitnRectangleDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.btnRun = QtGui.QPushButton(sitnRectangleDialogBase)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.gridLayout.addWidget(self.btnRun, 6, 1, 1, 1)

        self.retranslateUi(sitnRectangleDialogBase)
        QtCore.QMetaObject.connectSlotsByName(sitnRectangleDialogBase)

    def retranslateUi(self, sitnRectangleDialogBase):
        sitnRectangleDialogBase.setWindowTitle(_translate("sitnRectangleDialogBase", "sitn rectangle", None))
        self.label_4.setText(_translate("sitnRectangleDialogBase", "UR north", None))
        self.label_3.setText(_translate("sitnRectangleDialogBase", "LL east", None))
        self.label_2.setText(_translate("sitnRectangleDialogBase", "LL north", None))
        self.label.setText(_translate("sitnRectangleDialogBase", "UR east", None))
        self.btnRun.setText(_translate("sitnRectangleDialogBase", "Make this a rectangle!", None))

