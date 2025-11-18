from PySide6.QtCore import QSize, Qt 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setWindowTitle("My App")
        self.label = QLabel()
        self.label.setMaximumSize(QSize(600,400))
        self.label.setMouseTracking(True)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self,e):
        self.label.setText("Mouse Moved")

    def mousePressEvent(self, event):
        self.label.setText("Mouse Pressed")

    def mouseDoubleClickEvent(self, event):
        self.label.setText("Mouse Doubled Pressed")
    
    def mouseReleaseEvent(self,event):
        self.label.setText("Mouse Release Pressed")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
