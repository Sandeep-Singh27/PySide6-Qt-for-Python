from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QDialog, QVBoxLayout
from PySide6.QtCore import Slot

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.line = QLineEdit("Write your name here...")
        self.button = QPushButton("Show Greetings")
        layout = QVBoxLayout(self)
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    @Slot()
    def greetings(self):
        print(f"Hello {self.line.text()}")

if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()
    app.exec()