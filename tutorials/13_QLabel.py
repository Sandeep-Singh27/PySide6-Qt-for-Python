from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap

app = QApplication([])

label = QLabel()
label.setPixmap(QPixmap("images/otje.webp"))
label.setScaledContents(True)
label.show()

app.exec()