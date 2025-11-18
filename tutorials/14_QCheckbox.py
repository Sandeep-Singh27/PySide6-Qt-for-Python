from PySide6.QtCore import QSize, Qt 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        checkbox = QCheckBox("This is a checkbox")
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
