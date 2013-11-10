#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HeesangLee
#
# Created:     19/08/2013
# Copyright:   (c) HeesangLee 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import (Qt, SIGNAL,QTimer)
from PyQt4.QtGui import (QApplication, QDialog, QLineEdit, QTextBrowser,
        QVBoxLayout,QPushButton,QLabel,QGraphicsScene )
from PyQt4 import QtGui

import os

import uiTranslator
from translate import Translator


class Dlg_Translator(QDialog,uiTranslator.Ui_Dialog):
    lang_code = {"Afrikaans":"af","Albanian":"sq","Arabic":"ar","Azerbaijani":"az","Basque":"eu","Bengali":"bn","Belarusian":"be","Bulgarian":"bg","Catalan":"ca","Chinese Simplified":"zh-CN","Chinese Traditional":"zh-TW","Croatian":"hr","Czech":"cs","Danish":"da","Dutch":"nl","English":"en","Esperanto":"eo","Estonian":"et","Filipino":"tl","Finnish":"fi","French":"fr","Galician":"gl","Georgian":"ka","German":"de","Greek":"el","Gujarati":"gu","Haitian Creole":"ht","Hebrew":"iw","Hindi":"hi","Hungarian":"hu","Icelandic":"is","Indonesian":"id","Irish":"ga","Italian":"it","Japanese":"ja","Kannada":"kn","Korean":"ko","Latin":"la","Latvian":"lv","Lithuanian":"lt","Macedonian":"mk","Malay":"ms","Maltese":"mt","Norwegian":"no","Persian":"fa","Polish":"pl","Portuguese":"pt","Romanian":"ro","Russian":"ru","Serbian":"sr","Slovak":"sk","Slovenian":"sl","Spanish":"es","Swahili":"sw","Swedish":"sv","Tamil":"ta","Telugu":"te","Thai":"th","Turkish":"tr","Ukrainian":"uk","Urdu":"ur","Vietnamese":"vi","Welsh":"cy","Yiddish":"yi"}
    readText=[]
    def __init__(self, parent=None):
        super(Dlg_Translator, self).__init__(parent)
        self.setupUi(self)
        self.makeSignalSlot()
        self.myUi()
##        self.printLangKeys()

    def myUi(self):
        sortedLangCode = self.lang_code.keys()
        sortedLangCode.sort()
        self.cb_fromLang.addItems(sortedLangCode)
        self.label.setText("Program started")

    def printLangKeys(self):
        trans = Translator(to_lang="ko")
        langkeys=self.lang_code.keys()
        langkeys.sort()
        for lang in langkeys:
            print lang+" : "+trans.translate(lang)

    def makeSignalSlot(self):
        self.pb_open.clicked.connect(self.fromFileOpen)
        self.pb_translate.clicked.connect(self.doTranslate)

    def fromFileOpen(self):
        options = QtGui.QFileDialog.Options()
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                "Open Original text file", "C:\HeesangLee\Android\Dev\Dev_Data\\",
                "Text Files (*.txt);;All Files (*)")
        if fileName:
            readFile = open(fileName,'r')
            previewTxt=''
            for line in readFile:
                self.readText.append(line)
                previewTxt += line
            self.tb_preview.setText(previewTxt)
            self.originalFileName = os.path.basename(str(fileName))
            self.label.setText(self.originalFileName+" is selected")

    def doTranslate(self):
        openDirName = self.getOpenFileName()
        trans = Translator(to_lang="ko")
        trans.from_lang = self.lang_code[str(self.cb_fromLang.currentText())]
        self.label.setText("Under translating")
        for langCode in self.lang_code.keys():
            try:
                writeFile = open(openDirName+"\\"+langCode+"_"+self.originalFileName,'w')
                transResult=''
                trans.to_lang = self.lang_code[langCode]
                for line in self.readText:
                    try:
                        transResult += trans.translate(line).encode('utf-8')+"\n"
                    except:
                        transResult += trans.translate(line)+'\n'
                writeFile.write(transResult)
                writeFile.close()
            except:
                print langCode
                print self.readText
                break

        self.label.setText("Working done")



    def getOpenFileName(self):
        dirName = QtGui.QFileDialog.getExistingDirectory(self,
                    "Select Save directory","C:\HeesangLee\Android\Dev\Dev_Data\\",
                    QtGui.QFileDialog.ShowDirsOnly)
        return dirName

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg=Dlg_Translator()
    dlg.show()
    dlg.exec_()




































