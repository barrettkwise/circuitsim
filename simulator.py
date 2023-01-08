import gateinterface
import gateobjcreate
class Simulator():
    def __init__(self,  line: tuple) -> None:
        self.line = line
        self.gates = [gateobjcreate.GateObject(gate) for gate in self.line]
    
    def finder(self, target: str) -> object:
        for gate in self.gates:
            if target in gate.out[0]:
                return gate

    # simulates lines individually
    def single(self) -> list:
        for gate in self.gates:
            if gate.in1.isalpha():
                tar1 = gate.in1
                out1 = self.finder(tar1)
                g = gateinterface.Gates(out1)
                gate.in1 = g.find_output()

            if gate.in2.isalpha():
                tar2 = gate.in2
                out2 = self.finder(tar2)
                g = gateinterface.Gates(out2)
                gate.in2 = g.find_output()
            
            g = gateinterface.Gates(gate)
            gate.out[1] = g.find_output()

            #print(gate.type, gate.in1, gate.in2, gate.out)

        return self.gates