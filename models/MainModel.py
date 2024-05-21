# [MainModel.py]

from models.tools.File_selector import File_selector
from models.Minizinc import Minizinc
# from tests.QueensProblem.QueensProblemParser import QueensProblemParser
from models.PUICAProblem.PUICAProblemParser import PUICAProblemParser as Parser

debug = True


def print_debug(message):
    new_message = "[MainModel.py]: " + message
    if debug:
        print(new_message)


class MainModel:
    def __init__(self):
        self.instancia_minizinc = Minizinc()
        self.resultado = None
        self.set_modelo("./models/PUICAProblem/PUICA-model.mzn")

    def set_modelo(self, nuevo_modelo):
        self.instancia_minizinc.set_model(nuevo_modelo)

    def set_datos(self):
        file = File_selector.select()

        if len(file) == 0:
            return None

        parsed = Parser.parse_input_file_to_dzn(file)
        self.instancia_minizinc.set_data(parsed["path"])

        return parsed

    def check_minizinc(self):
        try:
            self.instancia_minizinc.check_version()
        except Exception as e:
            return str(e)
        return "OK"

    def set_solver(self, nuevo_solver):
        self.instancia_minizinc.set_solver(nuevo_solver)

    def set_resultado(self, nuevo_resultado):
        self.resultado = nuevo_resultado

    def get_modelo(self):
        return self.instancia_minizinc.model

    def get_datos(self):
        return self.instancia_minizinc.data

    def get_solver(self):
        return self.instancia_minizinc.solver

    def get_lista_solvers(self):
        return self.instancia_minizinc.get_solver_list()

    def iniciar(self):
        self.resultado = self.instancia_minizinc.solve()
