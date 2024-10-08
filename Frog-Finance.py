from PyQt6.QtWidgets import QApplication, QLabel, QWidget

import sys

app = QApplication([])

window = QWidget()
window.setWindowTitle("Frog Finance")
window.setGeometry(100, 100, 1366, 768) # TODO: Determine final app size
window.show()

sys.exit(app.exec())