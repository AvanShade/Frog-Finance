import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from ui.main_window import MainWindow

def main():
    app = QApplication([]) # Initialize application

    mainWindow = MainWindow() # Create main window (UI)
    mainWindow.show() # Show main window

    sys.exit(app.exec()) # Start event loop

if __name__ == '__main__':
    main()
