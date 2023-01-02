class Simulator():
    def __init__(self,  line: tuple):
        self.line = line

    # simulates lines individually
    def single(self):

        # find pairs of ins and outs
        def find_next(target: str):
            gate_inds = []
            gate_ind = 0
            for gate in self.line:
                if gate[len(gate)-2] == target:
                    gate_inds.append([gate_ind, 2])

                if gate[len(gate)-3] == target:
                    gate_inds.append([gate_ind, 1])

                gate_ind += 1

            return gate_inds

        # use pairs to change gate values
        for i in self.line:
            if i[len(i)-1].isalpha():
                g = Gates(i)
                next_in = find_next(i[len(i)-1])
                for ind in next_in:
                    self.line[ind[0]][ind[1]] = g.find_output()
                    yield self.line
            else:
                continue

class Gates():
    def __init__(self, gate: list):
        self.gate = gate

    def find_output(self) -> str:
        if self.gate[0] == "not":
            return Gates.NOT(self.gate[1])

        elif self.gate[0] == "and":
            return Gates.AND(self.gate[1], self.gate[2])

        elif self.gate[0] == "or":
            return Gates.OR(self.gate[1], self.gate[2])

        elif self.gate[0] == "nand":
            return Gates.NOT(Gates.AND(self.gate[1], self.gate[2]))

        elif self.gate[0] == "nor":
            return Gates.NOT(Gates.OR(self.gate[1], self.gate[2]))

        elif self.gate[0] == "xor":
            return Gates.XOR(self.gate[1], self.gate[2])

        elif self.gate[0] == "xnor":
            return Gates.NOT(Gates.XOR(self.gate[1], self.gate[2]))

        else:
            print("Gate not supported.")

    def NOT(a) -> str:
        if a == "1":
            return "0"
        else:
            return "1"

    def AND(a, b) -> str:
        if a == "1" and b == "1":
            return "1"
        else:
            return "0"

    def OR(a, b) -> str:
        if a == "1" or b == "1":
            return "1"
        else:
            return "0"

    def XOR(a, b) -> str:
        if a != b:
            return "1"
        else:
            return "0"
