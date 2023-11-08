from PyQt6 import QtCore, QtGui, QtWidgets
from spr import Ui_Dialog
import random

def money():
    print("Koszt wizyty: " + str(1) + "zł")
    print("dni: " + str(random.randrange(1,14)))
    print("specjalizacja: " + str(1) + "zł")



if __name__ == "__main__":
    import sys
    

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.rezerwacja.clicked.connect(money)
    sys.exit(app.exec())