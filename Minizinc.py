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

    def set_model(self, new_model):
        self.model = str(new_model)

    def set_data(self, new_data):
        self.data = str(new_data)

    def set_solver(self, new_solver):
        if new_solver in self.solver_list:
            self.solver = str(new_solver)
        else:
            raise Exception(
                "Error, solver \'{}\' no esta en la lista de solvers usables.".format(str(new_solver)))

    def parse_input_file_to_dzn(self, input_file_path):

        with open(input_file_path, 'r') as file:
            line = file.readline().strip()
        try:
            n = int(line)
        except ValueError:
            raise ValueError(
                "El contenido del archivo no es un número válido: {}".format(str(line)))

        dzn_content = "n = {};".format(str(n))
        dzn_file_path = input_file_path.rsplit('.', 1)[0] + ".dzn"

        with open(dzn_file_path, 'w') as dzn_file:
            dzn_file.write(dzn_content)

        return dzn_file_path

    def parse_solver_output(self, output):
        lines = output.strip().split("\n")
        result = {}
        for line in lines:
            if "=" in line:
                var, value = line.split("=")
                result[var.strip()] = value.strip()
        return result

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
                "Error en ejecución del comando:\n {}".format(str(result.stderr)))

        return (result.stdout)
