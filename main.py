import sys
from PyQt5.QtWidgets import QApplication
from logic import CalculatorWindow

app = QApplication(sys.argv)

logic = CalculatorWindow()

sys.exit(app.exec_())