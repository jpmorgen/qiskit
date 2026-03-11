import matplotlib.pyplot as plt

from qiskit_algorithms.optimizers import SLSQP
from qiskit.circuit.library import n_local

num_qubits = 2
ansatz = n_local(num_qubits, "ry", "cz")
optimizer = SLSQP(maxiter=1000)

fig = ansatz.draw("mpl")

plt.show()
