import gateobject as g


class Simulator:
    def __init__(self, circuit: dict) -> None:
        self.circuit = circuit
        self.gates = []

        for level, line in enumerate(circuit.values(), 0):
            for gate in line:
                self.gates.append(g.Gate(level, gate))

    def simulate(self):
        p_level = 0
        for p_level in range(len(self.circuit)):
            # values and ids of previous/initial line
            curr_ids = [
                gate.out.id for gate in self.gates if gate.priority == p_level]
            curr_vals = [
                gate.out.value for gate in self.gates if gate.priority == p_level]

            # ids of current line
            gates_to_check = [
                gate for gate in self.gates if gate.priority == p_level + 1]
            gate_ids_check = [
                gate.out.id for gate in self.gates if gate.priority == p_level + 1]

            for gate_c, gate in enumerate(gates_to_check, 0):
                gate_vals_check = [
                    gate.out.value for gate in self.gates if gate.priority == p_level + 1]
                if gate.in1.id in curr_ids:
                    index = curr_ids.index(gate.in1.id)
                    gate.in1.value = curr_vals[index]

                if gate_c != 0 and gate.in1.id in gate_ids_check:
                    index = gate_ids_check.index(gate.in1.id)
                    gate.in1.value = gate_vals_check[index]

                if gate.type != "NOT":
                    if gate.in2.id in curr_ids:
                        index = curr_ids.index(gate.in2.id)
                        gate.in2.value = curr_vals[index]

                    if gate_c != 0 and gate.in2.id in gate_ids_check:
                        index = gate_ids_check.index(gate.in2.id)
                        gate.in2.value = gate_vals_check[index]

                    gate.out.value = eval(gate.type)(
                        gate.in1.value, gate.in2.value)

                else:
                    gate.out.value = eval(gate.type)(gate.in1.value)

            p_level += 1

        return self.gates
