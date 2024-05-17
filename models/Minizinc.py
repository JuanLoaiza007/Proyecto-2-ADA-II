# [Minizinc.py]

import subprocess

debug = True


def print_debug(message):
    print("[Minizinc.py]: {}".format(str(message)))


class Minizinc:
    def __init__(self):
        self.model = None
        self.data = None
        self.solver = None

        self.solver_list = [
            "Chuffed",
            "COIN-BC",
            "findMUS",
            "Gecode",
            "Gecode Gist",
            "Globalizer",
            "OR Tools CP-SAT",
        ]

    def set_model(self, new_model_file):
        self.model = str(new_model_file)
        print_debug("El archivo del modelo es {}".format(str(new_model_file)))

    def set_data(self, new_data_file):
        self.data = str(new_data_file)
        print_debug("El archivo de datos es {}".format(str(new_data_file)))

    def set_solver(self, new_solver):
        if new_solver in self.solver_list:
            self.solver = str(new_solver)
            print_debug("El solver es {}".format(str(new_solver)))
        else:
            raise Exception(
                "Error, solver \'{}\' no esta en la lista de solvers usables.".format(str(new_solver)))

    def get_model(self):
        return self.model

    def get_data(self):
        return self.data

    def get_model(self):
        return self.model

    def get_solver_list(self):
        return self.solver_list

    def solve(self):

        if (self.model == None):
            raise Exception("Error, model es none.")
        if (self.data == None):
            raise Exception("Error, data es none.")
        if (self.solver == None):
            raise Exception("Error, solver es none.")

        command = ["minizinc", "--solver", self.solver, self.model, self.data]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            raise Exception(
                "Error al ejecutar comando: \'{}\' \n {}".format(str(command), str(result.stderr)))

        print_debug("El resultado es {}".format(str(result.stdout)))

        return result.stdout
