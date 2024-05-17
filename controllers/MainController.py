# [MainController.py]

import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
from views.MainView import Ui_MainWindow
from models.MainModel import MainModel
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from models.tools.temporizador import Temporizador

debug = True


def print_debug(message):
    new_message = "[MainController.py]: " + message
    if debug:
        print(new_message)


class WorkerThread(QThread):
    """
    Clase de Hilo Trabajador para ejecutar procesamiento en segundo plano y conservar la ventana recibiendo eventos.
    """

    def __init__(self, modelo):

        super().__init__()
        self.modelo = modelo

    def run(self):
        try:
            self.modelo.iniciar()
        except Exception as e:
            self.modelo.set_resultado(None)
            print_debug("WorkerThread Error -> {}".format(str(e)))


class controlador_principal:
    # Funcion para inicializar
    def cargar(self, main_window):

        self.modelo = MainModel()

        self.MainWindow = main_window
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_cargarArchivo.clicked.connect(self.cargar_archivo)
        self.ui.box_solver.currentIndexChanged.connect(
            self.cambiar_solver)
        self.ui.btn_iniciar.clicked.connect(self.iniciar)
        self.ui.btn_sobre.clicked.connect(self.mostrar_sobre_nosotros)
        # Evento para cierre de programa
        self.MainWindow.destroyed.connect(self.cerrar_ventana)

        self.cargar_solvers()
        self.ui.lbl_archivo_cargado.setText("No hay archivo cargado")

    # Funciones de ventana
    def cerrar_ventana(self):

        def cierre_forzoso():
            print_debug(
                "cerrar_ventana() -> Absorbí el error de cerrar el hilo de procesamiento")
            os._exit(0)

        try:
            self.hilo_procesamiento.exit()
            os._exit(0)
        except AttributeError:
            cierre_forzoso()
        except RuntimeError:
            cierre_forzoso()

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    def block_focus(self):
        """
        Funcion intuitiva para mostrar que la ventana principal NO es la que esta recibiendo eventos, ayuda a mostrar que el flujo de trabajo esta ocurriendo en otra ventana.
        """
        self.MainWindow.setEnabled(False)
        self.ui.centralwidget.setEnabled(False)
        self.ui.centralwidget.setVisible(False)
        self.MainWindow.setFixedSize(self.MainWindow.size())

    def little_block_focus(self):
        """
        Funcion intuitiva para mostrar que la ventana principal esta procesando sin embargo el flujo de trabajo esta actualmente en ella.
        """
        self.MainWindow.setEnabled(False)
        self.ui.centralwidget.setEnabled(False)
        self.MainWindow.setFixedSize(self.MainWindow.size())

    def unblock_focus(self):
        """
        Funcion intuitiva para revertir block_focus() y little_block_focus(), muestra que el flujo de trabajo esta ocurriendo en la ventana principal y habilita los eventos.
        """
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.MainWindow.setEnabled(True)
        self.ui.centralwidget.setEnabled(True)
        self.ui.centralwidget.setVisible(True)

    def mostrar_dialogo(self, titulo, mensaje):
        self.block_focus()
        Temporizador.iniciar(1)

        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_dialog.setModal(True)
        new_dialog.show()
        new_ui.lbl_title.setText(titulo)
        new_ui.lbl_body.setText(mensaje)

        new_dialog.exec()

        self.unblock_focus()

    def cargar_solvers(self):
        lista_solvers = self.modelo.get_lista_solvers()
        self.ui.box_solver.addItems(lista_solvers)

    # Funciones específicas
    def cargar_archivo(self):

        self.block_focus()
        Temporizador.iniciar(1)

        try:
            respuesta = self.modelo.set_datos()
            if (respuesta != None):
                self.ui.txtE_entrada.setText(
                    "=== Interpretacion ===\n{}".format(str(respuesta["content"])))
                self.ui.lbl_archivo_cargado.setText(respuesta["filename"])
        except ValueError:
            titulo = "Error"
            mensaje = "Este archivo no es un archivo de datos válido."
            self.mostrar_dialogo(titulo, mensaje)

        self.ui.txtE_resultado.setText("")
        self.unblock_focus()

    def cambiar_solver(self):
        indice_solver = self.ui.box_solver.currentIndex()
        nombre_solver = self.ui.box_solver.currentText()

        self.ui.txtE_resultado.setText("")

        print_debug("ItemComboBox is {}. {}".format(
            indice_solver, nombre_solver))

        self.modelo.set_solver(nombre_solver)

    def mostrar_resultado(self):
        if (self.modelo.resultado == None):
            titulo = "Error"
            mensaje = "Ha ocurrido un error interno y no hay resultado, porfavor contacte a soporte.\nSi usted es soporte, que la fuerza lo acompañe."
            self.mostrar_dialogo(titulo, mensaje)

        self.unblock_focus()
        self.ui.txtE_resultado.setText(self.modelo.resultado)

    def iniciar(self):

        if self.modelo.get_datos() == None:
            titulo = "Error"
            mensaje = "Debe cargar datos antes de iniciar el solver."
            self.mostrar_dialogo(titulo, mensaje)
            return None

        self.little_block_focus()

        self.hilo_procesamiento = WorkerThread(self.modelo)
        self.hilo_procesamiento.finished.connect(
            self.mostrar_resultado)
        self.hilo_procesamiento.start()

    def mostrar_sobre_nosotros(self):
        from controllers.AboutUsController import controlador_sobre_nosotros
        self.controlador_sobre_nosotros = controlador_sobre_nosotros()
        self.controlador_sobre_nosotros.mostrar(self.MainWindow)
