# Form implementation generated from reading ui file './spr.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 426)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.inputImie = QtWidgets.QTextEdit(parent=Dialog)
        self.inputImie.setGeometry(QtCore.QRect(150, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputImie.setFont(font)
        self.inputImie.setObjectName("inputImie")
        self.inputNazwisko = QtWidgets.QTextEdit(parent=Dialog)
        self.inputNazwisko.setGeometry(QtCore.QRect(150, 80, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.inputNazwisko.setFont(font)
        self.inputNazwisko.setObjectName("inputNazwisko")
        self.rezerwacja = QtWidgets.QPushButton(parent=Dialog)
        self.rezerwacja.setGeometry(QtCore.QRect(90, 280, 291, 91))
        self.rezerwacja.setObjectName("rezerwacja")
        self.checkWizytaPrywatna = QtWidgets.QCheckBox(parent=Dialog)
        self.checkWizytaPrywatna.setGeometry(QtCore.QRect(270, 210, 191, 51))
        self.checkWizytaPrywatna.setChecked(True)
        self.checkWizytaPrywatna.setObjectName("checkWizytaPrywatna")
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 151, 111))
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radioInternista = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioInternista.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.radioInternista.setObjectName("radioInternista")
        self.radioPediatra = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioPediatra.setGeometry(QtCore.QRect(10, 40, 121, 31))
        self.radioPediatra.setObjectName("radioPediatra")
        self.radioDermatolog = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioDermatolog.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.radioDermatolog.setObjectName("radioDermatolog")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Zarezerwuj Wizyte"))
        self.label.setText(_translate("Dialog", "Imie:"))
        self.label_2.setText(_translate("Dialog", "Nazwisko:"))
        self.rezerwacja.setText(_translate("Dialog", "Rezerwuj"))
        self.checkWizytaPrywatna.setText(_translate("Dialog", "Wizyta prywatna"))
        self.radioInternista.setText(_translate("Dialog", "Internista"))
        self.radioPediatra.setText(_translate("Dialog", "Pediatra"))
        self.radioDermatolog.setText(_translate("Dialog", "Dermatolog"))


