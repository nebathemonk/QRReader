import pyqrcode
import sys

done = False

while done == False:
    print('Welcome to the QR code creator')
    print('enter the number to select function')

    print('1: create new qr code')
    print('2: exit')
    selection = input('>>')

    if selection == '1':
        name = input('Enter the name you want to turn into a QR code:')
        qrString = "" + name + ".png"
        qrcode = pyqrcode.create(name)
        qrcode.png(name + ".png")
        print('QR code for ' + name + ' created.')
    if selection == '2':
        print('goodbye')
        done = True
        break

