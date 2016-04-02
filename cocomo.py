from PyQt4 import QtGui  
import sys  
import cocomo_model 
import math 
import os  


class CocomoAppn(QtGui.QMainWindow, cocomo_model.Ui_MainWindow): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.a = self.b = self.c = self.d = self.kloc = 0
        self.setupUi(self)  
        self.radioButton.toggled.connect(self.radioButton_clicked)
        self.radioButton_2.toggled.connect(self.radioButton_2_clicked)
        self.radioButton_3.toggled.connect(self.radioButton_3_clicked) 
                                 
    def radioButton_clicked(self, enabled):
        if enabled:
            self.kloc = long(self.textEdit.toPlainText())
            self.a = 2.4
            self.b = 1.05
            self.c = 2.5
            self.d = 0.38
            self.display()

    def radioButton_2_clicked(self, enabled):
        if enabled:
            self.kloc = long(self.textEdit.toPlainText())
            self.a = 3.0
            self.b = 1.12
            self.c = 2.5
            self.d = 0.35 
            self.display()      	
        	
    def radioButton_3_clicked(self, enabled):
        if enabled:
            self.kloc = long(self.textEdit.toPlainText())
            self.a = 3.6
            self.b = 1.20
            self.c = 2.5
            self.d = 0.32
            self.display()

    def display(self):
        efforts = self.a * math.pow(self.kloc, self.b)
        devtime = self.c * math.pow(efforts, self.d)
        staff_size = efforts/devtime
        self.label_6.setText(str(round(efforts)) + " person-months")
       	self.label_6.setStyleSheet('color: red') 
        self.label_7.setText(str(round(devtime)) + " months")
        self.label_7.setStyleSheet('color: red')
        self.label_8.setText(str(round(staff_size)) + " person")
        self.label_8.setStyleSheet('color: red')
        
def main():
    app = QtGui.QApplication(sys.argv)  
    model = CocomoAppn()  
    model.show()  
    sys.exit(app.exec_())  


if __name__ == '__main__':  
    main()  