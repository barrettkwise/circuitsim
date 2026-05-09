from logicops import *


class Gate:
    def __init__(self, priority: int, gate_info: list) -> None:
        self.priority = priority
        if safety_check(gate_info[0].upper()):
            self.type = gate_info[0].upper()
        else:
            raise ValueError(f"Invalid gate type: {gate_info[0]}")

        if self.priority == 0:
            self.in1 = GatePort("Priority 0 Input", gate_info[1])
            if self.type == "NOT":
                self.out = GatePort(gate_info[2], eval(self.type)(self.in1.value))
            else:
                self.in2 = GatePort("Priority 0 Input", gate_info[2])
                self.out = GatePort(
                    gate_info[3], eval(self.type)(self.in1.value, self.in2.value)
                )

        else:
            if gate_info[1] == "0" or gate_info[1] == "1":
                self.in1 = GatePort(
                    f"Und. Priority {self.priority} Input", gate_info[1]
                )
            else:
                self.in1 = GatePort(gate_info[1], "None")

            if self.type == "NOT":
                self.out = GatePort(gate_info[2], "None")

            else:
                if gate_info[2] == "0" or gate_info[2] == "1":
                    self.in2 = GatePort(
                        f"Und. Priority {self.priority} Input", gate_info[2]
                    )
                else:
                    self.in2 = GatePort(gate_info[2], "None")

                self.out = GatePort(gate_info[3], "None")


class GatePort:
    def __init__(self, gid: str, value: str) -> None:
        self.id = gid
        self.value = value