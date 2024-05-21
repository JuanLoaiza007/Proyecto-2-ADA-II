# [AboutUsController.py]

from views.AboutUsView import Ui_MainWindow
from models.AboutUsModel import AboutUsModel


class AboutUsController:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = AboutUsModel()
        self.MainWindow = main_window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_volver.clicked.connect(self.volver)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    def volver(self):
        from controllers.MainController import controlador_principal
        self.controlador_principal = controlador_principal()
        self.controlador_principal.mostrar(self.MainWindow)
