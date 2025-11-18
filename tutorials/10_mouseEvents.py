from PySide6.QtCore import QSize, Qt 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        self.label = QLabel()
        self.setCentralWidget(self.label)


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Left")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Right")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Middle")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

'''
.button() 	Specific button that triggered this event
.buttons() 	State of all mouse buttons (OR'ed flags)
.globalPos() 	Application-global position as a QPoint
.globalX() 	Application-global horizontal X position
.globalY() 	Application-global vertical Y position
.pos() 	Widget-relative position as a QPoint integer
.posF() 	Widget-relative position as a QPointF float
'''