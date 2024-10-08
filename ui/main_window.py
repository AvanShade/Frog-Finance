from PyQt6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Frog Finance")
        self.setGeometry(100, 100, 1366, 768) # TODO: Determine final app size

