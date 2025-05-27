from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButtton, QFileDialog
class ConverterUI(QWidget):
 def __init__(self):
  super().__init__()
  self.initUI()
 def initUI(self):
  self.layout = QVBoxLayout()
  self.btn_convert = QPushButton('Konwertuj')
  self.layout.addWidget(self.btn_convert)
  self.setLayout(self.layout)
  self.setWindowTitle('Konwerter plików')
if __name__ == "__main__":
 app = QApplication([])
 window = ConverterUI()
 window.show()
 app.exec()
