from PyQt5.QtCore import QThread, pyqtSignal
class Worker(QThread):
 finished = pyqtSignal()
 error = pyqtSignal(str)
 def __init__(self, input_path, output_path):
  super().__init__()
  self.input_path = input_path
  self.output_path = output_path 
 def run(self):
  try:
   self.sleep(2)
   self.finished.emit()
  except Exception as e:   
   self.error.emit(str(e))
class ConverterUI(QWidget):
 def __init__(self):
  super().__init__()
  self.initUI()
  self.worker = None
