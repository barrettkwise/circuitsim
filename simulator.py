import gateobject as g
from logicops import *


class Simulator:
    def __init__(self, circuit: dict) -> None:
        self.circuit = circuit
        if self.circuit is None:
            self.gates = []
        else:
            self.gates = []
            temp_gates = [gate for tup in circuit.values() for gate in tup]
            if not all([isinstance(value, list) for value in temp_gates]):
                self.gates = temp_gates

            else:
                for level, line in enumerate(circuit.values(), start=0):
                    for gate in line:
                        self.gates.append(g.Gate(level, gate))

    def __find_gate(self, output_id: str) -> g.Gate:
        for gate in self.gates:
            if gate.out.id == output_id:
                return gate

    def simulate(self) -> list:
        for p_level in range(1, len(self.circuit)):
            gates_to_check = [gate for gate in self.gates if gate.priority == p_level]

            for gate in gates_to_check:
                # ids of gate outputs with simulated values
                stored_ids = [
                    gate.out.id for gate in self.gates if gate.out.value in ["0", "1"]
                ]
                curr_gate_index = self.gates.index(gate)
                for iteration_count, pid in enumerate(stored_ids):
                    if gate.in1.id == pid:
                        gate.in1.value = self.__find_gate(pid).out.value

                    if gate.type != "NOT":
                        if gate.in2.id == pid:
                            gate.in2.value = self.__find_gate(pid).out.value
                    else:
                        if iteration_count == len(stored_ids) - 1:
                            if gate.type == "NOT":
                                gate.out.value = eval(gate.type)(gate.in1.value)
                                self.gates[curr_gate_index] = gate

                            else:
                                gate.out.value = eval(gate.type)(
                                    gate.in1.value, gate.in2.value
                                )
                                self.gates[curr_gate_index] = gate

                        else:
                            continue

                    if gate.type == "NOT":
                        gate.out.value = eval(gate.type)(gate.in1.value)
                        self.gates[curr_gate_index] = gate

                    else:
                        gate.out.value = eval(gate.type)(gate.in1.value, gate.in2.value)
                        self.gates[curr_gate_index] = gate

        return self.gates