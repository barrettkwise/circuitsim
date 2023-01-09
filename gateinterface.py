#Stores gate logic
class Gates():
    def __init__(self, gate: object):
        self.gate = gate

    def find_output(self) -> str:
        if self.gate.type == "not":
            return Gates.NOT(self.gate.in1)

        elif self.gate.type == "and":
            return Gates.AND(self.gate.in1, self.gate.in2)

        elif self.gate.type == "or":
            return Gates.OR(self.gate.in1, self.gate.in2)

        elif self.gate.type == "nand":
            return Gates.NOT(Gates.AND(self.gate.in1, self.gate.in2))

        elif self.gate.type == "nor":
            return Gates.NOT(Gates.OR(self.gate.in1, self.gate.in2))

        elif self.gate.type == "xor":
            return Gates.XOR(self.gate.in1, self.gate.in2)

        elif self.gate.type == "xnor":
            return Gates.NOT(Gates.XOR(self.gate.in1, self.gate.in2))

        else:
            print("Gate not supported.")

    def NOT(a: str) -> str:
        if a == "1":
            return "0"
        else:
            return "1"

    def AND(a: str , b: str) -> str:
        if a == "1" and b == "1":
            return "1"
        else:
            return "0"

    def OR(a: str , b: str) -> str:
        if a == "1" or b == "1":
            return "1"
        else:
            return "0"

    def XOR(a: str , b: str) -> str:
        if a != b:
            return "1"
        else:
            return "0"
