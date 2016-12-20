#!/usr/bin/python
# -*- coding : utf-8 -*-
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
import dataconstruct as dt


class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args)
        self.setWindowTitle('Memento by Meliodas')
        label = QLabel(self.tr(u'Search Bar'))
        self.LineEdit = QLineEdit()
        self.TextEdit = QTextEdit()
        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.addWidget(self.LineEdit)
        vbox.addWidget(self.TextEdit)
        self.setLayout(vbox) 

        # create connection
        self.connect(self.LineEdit, SIGNAL("returnPressed(void)"), self.exect)

    def exect(self):
        search = str(self.LineEdit.text())
        result = dt.datasearch(search, dt.createdata("/home/meliodas/PycharmProjects/memento/mementoUnix"))
        resulte = ""
        comment = 0
        if len(result) < 2:
            comment = 1
        for sol in result:
            resulte += " ".join(sol[:-2]) + " ".join(sol[3])*comment + "\n"
        self.TextEdit.setText(resulte)
  
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_())