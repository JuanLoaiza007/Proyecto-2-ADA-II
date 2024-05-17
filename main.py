# [main.py]

from Minizinc import Minizinc
from tools.File_selector import File_selector
from QueensProblem.QueensProblemParser import Parser

mzInstance = Minizinc()
mzInstance.set_model(File_selector.select())
data = Parser.parse_input_file_to_dzn(File_selector.select())
mzInstance.set_data(data)
mzInstance.set_solver("Gecode")
result = mzInstance.solve()
print(result)


if __name__ == "__main__":
    from PUICAProblem.PUICAProblemParser import Parser
    Parser.test_parse_input_file_to_dzn()
