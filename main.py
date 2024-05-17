# [main.py]

from Minizinc import Minizinc
from tools.File_selector import File_selector

mzInstance = Minizinc()
mzInstance.set_model(File_selector.select())
data = mzInstance.parse_input_file_to_dzn(File_selector.select())
mzInstance.set_data(data)
mzInstance.set_solver("Gecode")
result = mzInstance.solve()
print(result)
