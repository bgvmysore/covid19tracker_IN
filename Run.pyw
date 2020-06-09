# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainform.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from appmod.functions import *

class Ui_Form(object):
    def __init__(self):
        self.getdat = getC19()

    def filldata(self):
        self.data = self.getdat.stateData(self.combox.currentText())
        self.actvar.setText(str(self.data['active']))
        self.curvar.setText(str(self.data['cured']))
        self.totvar.setText(str(self.data['total']))
        self.deavar.setText(str(self.data['death']))
        
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 575)
        Form.setMinimumSize(QtCore.QSize(0, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/vrs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("* {\n"
"font-family:Roboto, sans-serif;\n"
"font-size:20px;\n"
"margin:0px;\n"
"padding:0;\n"
"}\n"
"\n"
"QFrame#framemain {\n"
"background:#eee;\n"
"}\n"
"QFrame#Cards, QFrame#Cards_2, QFrame#Cards_3, QFrame#Cards_4 {\n"
"background:white;\n"
"border-radius:7px;\n"
"margin:10px;\n"
"border:1px solid #dfdfdf;\n"
"}\n"
"\n"
"QLabel#Header {\n"
"font-size:26px;\n"
"font-weight:bold;\n"
"background:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 150, 73, 255), stop:0.293785 rgba(255, 137, 137, 255), stop:0.638418 rgba(159, 229, 255, 255), stop:1 rgba(161, 255, 125, 255));\n"
"color:#222222;\n"
"padding:1em;\n"
"margin:0px 0px 10px 0px;\n"
"}\n"
"\n"
"QLabel#shead, QLabel#shead2, QLabel#shead3, QLabel#shead4 {\n"
"font-weight:bold;\n"
"padding:0px 10px;\n"
"}\n"
"\n"
"QLabel#shead{\n"
"color: rgb(255, 106, 0);\n"
"}\n"
"\n"
"QLabel#shead2{\n"
"color:rgb(77, 177, 0);\n"
"}\n"
"\n"
"QLabel#shead3{\n"
"color:rgb(0, 106, 198);\n"
"}\n"
"\n"
"QLabel#shead4{\n"
"color:rgb(255, 47, 47);\n"
"}\n"
"\n"
"QLabel#stateLabl{\n"
"padding:0px 1em;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QLabel#actvar, QLabel#curvar, QLabel#totvar, QLabel#deavar {\n"
"padding:0px 10px;\n"
"}\n"
"\n"
"QComboBox {\n"
"padding:0 0 0 1em ;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.framemain = QtWidgets.QFrame(Form)
        self.framemain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framemain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framemain.setObjectName("framemain")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.framemain)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Header = QtWidgets.QLabel(self.framemain)
        self.Header.setMinimumSize(QtCore.QSize(10, 20))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Header.setObjectName("Header")
        self.gridLayout_2.addWidget(self.Header, 0, 0, 1, 3)
        self.Cards_4 = QtWidgets.QFrame(self.framemain)
        self.Cards_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cards_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cards_4.setObjectName("Cards_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Cards_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.shead4 = QtWidgets.QLabel(self.Cards_4)
        self.shead4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.shead4.setObjectName("shead4")
        self.verticalLayout_4.addWidget(self.shead4)
        self.deavar = QtWidgets.QLabel(self.Cards_4)
        self.deavar.setObjectName("deavar")
        self.verticalLayout_4.addWidget(self.deavar)
        self.gridLayout_2.addWidget(self.Cards_4, 3, 2, 1, 1)
        self.Cards_2 = QtWidgets.QFrame(self.framemain)
        self.Cards_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cards_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cards_2.setObjectName("Cards_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Cards_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shead2 = QtWidgets.QLabel(self.Cards_2)
        self.shead2.setMinimumSize(QtCore.QSize(0, 0))
        self.shead2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.shead2.setObjectName("shead2")
        self.verticalLayout_2.addWidget(self.shead2)
        self.curvar = QtWidgets.QLabel(self.Cards_2)
        self.curvar.setObjectName("curvar")
        self.verticalLayout_2.addWidget(self.curvar)
        self.gridLayout_2.addWidget(self.Cards_2, 2, 2, 1, 1)
        self.combox = QtWidgets.QComboBox(self.framemain)
        self.combox.setMinimumSize(QtCore.QSize(250, 40))
        self.combox.setObjectName("combox")
        self.gridLayout_2.addWidget(self.combox, 1, 2, 1, 1)
        self.Cards_3 = QtWidgets.QFrame(self.framemain)
        self.Cards_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cards_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cards_3.setObjectName("Cards_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Cards_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.shead3 = QtWidgets.QLabel(self.Cards_3)
        self.shead3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.shead3.setObjectName("shead3")
        self.verticalLayout_3.addWidget(self.shead3)
        self.totvar = QtWidgets.QLabel(self.Cards_3)
        self.totvar.setObjectName("totvar")
        self.verticalLayout_3.addWidget(self.totvar)
        self.gridLayout_2.addWidget(self.Cards_3, 3, 0, 1, 1)
        self.Cards = QtWidgets.QFrame(self.framemain)
        self.Cards.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cards.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cards.setObjectName("Cards")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Cards)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shead = QtWidgets.QLabel(self.Cards)
        self.shead.setMaximumSize(QtCore.QSize(16777215, 50))
        self.shead.setObjectName("shead")
        self.verticalLayout.addWidget(self.shead)
        self.actvar = QtWidgets.QLabel(self.Cards)
        self.actvar.setObjectName("actvar")
        self.verticalLayout.addWidget(self.actvar)
        self.gridLayout_2.addWidget(self.Cards, 2, 0, 1, 1)
        self.stateLabl = QtWidgets.QLabel(self.framemain)
        self.stateLabl.setMinimumSize(QtCore.QSize(250, 40))
        self.stateLabl.setObjectName("stateLabl")
        self.gridLayout_2.addWidget(self.stateLabl, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.framemain, 0, 0, 1, 1)

        # Populate combobox and set default to Karnataka
        kindx = self.getdat.statenames.index("Karnataka")
        for i in self.getdat.statenames:
            self.combox.addItem(str(i))
        self.combox.setCurrentText(self.getdat.statenames[kindx])
        # Update entries when combobox is changed 
        self.combox.currentTextChanged.connect(self.filldata)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "COIVD19 TRACKER (IN)"))
        self.Header.setText(_translate("Form", "COVID19 TRACKER (IN)"))
        self.shead4.setText(_translate("Form", "DEATHS:"))
        self.deavar.setText(_translate("Form", "0000"))
        self.shead2.setText(_translate("Form", "CURED:"))
        self.curvar.setText(_translate("Form", "0000"))
        self.shead3.setText(_translate("Form", "TOTAL:"))
        self.totvar.setText(_translate("Form", "0000"))
        self.shead.setText(_translate("Form", "ACTIVE:"))
        self.actvar.setText(_translate("Form", "0000"))
        self.stateLabl.setText(_translate("Form", "PLACE :"))
        self.filldata()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
