# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiTranslator.ui'
#
# Created: Mon Aug 19 16:48:38 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 387)
        self.tb_preview = QtGui.QTextBrowser(Dialog)
        self.tb_preview.setGeometry(QtCore.QRect(20, 10, 361, 291))
        self.tb_preview.setObjectName(_fromUtf8("tb_preview"))
        self.cb_fromLang = QtGui.QComboBox(Dialog)
        self.cb_fromLang.setGeometry(QtCore.QRect(20, 350, 181, 22))
        self.cb_fromLang.setObjectName(_fromUtf8("cb_fromLang"))
        self.pb_open = QtGui.QPushButton(Dialog)
        self.pb_open.setGeometry(QtCore.QRect(220, 350, 75, 23))
        self.pb_open.setObjectName(_fromUtf8("pb_open"))
        self.pb_translate = QtGui.QPushButton(Dialog)
        self.pb_translate.setGeometry(QtCore.QRect(310, 350, 75, 23))
        self.pb_translate.setObjectName(_fromUtf8("pb_translate"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 320, 351, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Translator", None))
        self.pb_open.setText(_translate("Dialog", "&Open", None))
        self.pb_translate.setText(_translate("Dialog", "&Translate", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))

