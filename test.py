from qiskit.quantum_info import Statevector

sv = Statevector([0.6+ 0.8j, 0, 0, 0, 0])
print(sv.dim)