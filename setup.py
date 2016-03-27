#!/usr/bin/env python

import sys
import os
from cx_Freeze import setup, Executable

base = None
include_files = []


if sys.platform == 'win32':
    base = 'Win32GUI'
    PYQT5_DIR = r'D:\Python34\Lib\site-packages\PyQt5'
    include_files = [
        (os.path.join(PYQT5_DIR, "qml", "QtQuick.2"), "QtQuick.2"),
        (os.path.join(PYQT5_DIR, "qml", "QtQuick"), "QtQuick"),
        (os.path.join(PYQT5_DIR, "qml", "QtGraphicalEffects"), "QtGraphicalEffects"),
        'calculate.qml'
    ]

packages = ['decimal','sys','os','calculate','sip','PyQt5.QtQml','PyQt5.QtCore','PyQt5.QtGui','PyQt5.QtQuick','PyQt5.QtNetwork']

options = {
'build_exe':{'packages':packages, 'include_files': include_files},
}

executables = [Executable('main.py', base=base, targetName='calculate.exe')]

setup(
    name="calculate",
    version="1.0.0",
    author='zz',
    description="A calculate.",
    options=options,
    executables=executables,
)
