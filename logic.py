from PyQt5 import QtWidgets
from ui_calc_md import Ui_Calc

class CalculatorWindow(QtWidgets.QMainWindow,Ui_Calc):

    firstNum = None
    userIsTapingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_dot.clicked.connect(self.dot_pressed)

        self.pushButton_plus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_ymnoj.clicked.connect(self.binary_operation_pressed)
        self.pushButton_delenie.clicked.connect(self.binary_operation_pressed)

        self.pushButton_rovno.clicked.connect(self.rovno_pressed)

        self.pushButton_del.clicked.connect(self.del_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_ymnoj.setCheckable(True)
        self.pushButton_delenie.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()

        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or
                self.pushButton_ymnoj.isChecked() or self.pushButton_delenie.isChecked()) and (not self.userIsTapingSecondNumber)):
            newLable = format(float(button.text()), '.15g')
            self.userIsTapingSecondNumber = True
        else:
            if (('.' in self.label.text()) and (button.text() == "0")):
                newLable = format(self.label.text() + button.text(), '.15')
            else:
                newLable = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(newLable)

    def dot_pressed(self):
        self.label.setText(self.label.text() + '.')

    def binary_operation_pressed(self):
        button = self.sender()

        self.firstNum = float(self.label.text())

        button.setChecked(True)

    def rovno_pressed(self):

        secondNum = float(self.label.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLable = format(labelNumber, '.15g')
            self.label.setText(newLable)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLable = format(labelNumber, '.15g')
            self.label.setText(newLable)
            self.pushButton_minus.setChecked(False)

        elif self.pushButton_ymnoj.isChecked():
            labelNumber = self.firstNum * secondNum
            newLable = format(labelNumber, '.15g')
            self.label.setText(newLable)
            self.pushButton_ymnoj.setChecked(False)

        elif self.pushButton_delenie.isChecked():
            labelNumber = self.firstNum / secondNum
            newLable = format(labelNumber, '.15g')
            self.label.setText(newLable)
            self.pushButton_delenie.setChecked(False)

        self.userIsTapingSecondNumber = False

    def del_pressed(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_ymnoj.setChecked(False)
        self.pushButton_delenie.setChecked(False)

        self.userIsTapingSecondNumber = False

        self.label.setText("0")


