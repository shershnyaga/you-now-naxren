from PyQt5.QtWidgets import *
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image, ImageFilter

app = QApplication([])
main_win = QWidget()
list1 = QListWidget(main_win)
#list2 = QListWidget(main_win)
labe = QLabel(main_win)
labe.move(360,40)
labe.resize(360,340)
knopka = QPushButton(main_win)
knopka.move(500,300)
knopka.setText('Обзор')
sdir = ''
putj = ""

knopka1 = QPushButton(main_win)
knopka1.move(10,400)
knopka1.setText('cherno')



knopka2 = QPushButton(main_win)
knopka2.move(100,400)
knopka2.setText('razmito')
def f1():
    global sdir
    sdir = QFileDialog.getExistingDirectory()
    exty = ['.jpg', '.jpeg', 'png', '.bmp', 'gif' ]
    files = os.listdir(sdir)
    files2 = filtr(files,exty)
    list1.clear()
    for f in files2:
        list1.addItem(f)
        
knopka.clicked.connect(f1)


def filtr(files, extens):   
    result = []
    for f in files:
        for ext in extens:
            if f.endswith(ext):
                result.append(f)
    return result

def loader():
    global wdir, putj, sdir
    f = list1.currentItem().text()
    putj = os.path.join(sdir, f)
    image = Image.open(putj)
    pix = QPixmap(putj)
    labe.setPixmap(pix)
    #w = image.width
    #h = image.height()
list1.currentRowChanged.connect(loader)


def HB():
    global wdir, putj, sdir
    imag = Image.open(putj)
    HB1 = imag.convert('L')
    itog = sdir + 'changed.jpg'
    HB1.save(itog)
    pix = QPixmap(itog)
    pix = pix.scaled(300,300,Qt.KeepAspectRatio)
    labe.resize(300,300)
    labe.setPixmap(pix)
knopka1.clicked.connect(HB)



main_win.show()
app.exec_()
