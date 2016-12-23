import pyqrcode
import sys

name = pyqrcode.create('admin')
name.png('testQR.png')

