from Minizinc import Minizinc

mzInstance = Minizinc()
mzInstance.set_model("nqueens.mzn")
mzInstance.set_data("nqueens.dzn")
mzInstance.set_solver("Gecode")
result = mzInstance.solve()
print(result)
