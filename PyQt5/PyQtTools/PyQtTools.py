#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication
from GUI import MainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.resize(400, 300)
    mainWin.setWindowTitle('Simple')
    mainWin.show()

    status = app.exec()
    sys.exit(status)
