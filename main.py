#!/usr/bin/env python
# encoding: utf-8

from PyQt5.QtCore import  QUrl, QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from calculate import *

class Calculator(QObject):

    @pyqtSlot(str,result = str)
    def output(self,exp):
        '''return the result of  exp'''
        return str(calculate(exp))

    @pyqtSlot(str,result = str)
    def del_input(self,input):
        '''the function for the "del" Button '''
        return input[:-1]

if __name__ == '__main__':
    path = 'calculate.qml'
    app = QGuiApplication([])
    view = QQuickView()
    con = Calculator()
    context = view.rootContext()
    context.setContextProperty("con",con)
    view.engine().quit.connect(app.quit)
    view.setSource(QUrl(path))
    view.show()
    app.exec()
