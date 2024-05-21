# [main.py]

from controllers.MainController import MainController
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    MainController = MainController()
    MainController.mostrar(main_window)
    sys.exit(app.exec_())
