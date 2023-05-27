from logicops import *

# Create gate object for each gate


class Gate():
    def __init__(self, priority: int, line: list) -> None:
        self.priority = priority
        self.type = line[0].upper()

        if self.priority == 0:
            self.in1 = GatePort("Priority 0 Input", line[1])
            if self.type == "NOT":
                self.out = GatePort(line[2], eval("NOT")(self.in1.value))
            else:
                self.in2 = GatePort("Priority 0 Input", line[2])
                self.out = GatePort(line[3], eval(self.type)(
                    self.in1.value, self.in2.value))

        else:
            if line[1] == "0" or line[1] == "1":
                self.in1 = GatePort(
                    f"Und. Priority {self.priority} Input", line[1])
            else:
                self.in1 = GatePort(line[1], "None")

            if self.type == "NOT":
                self.out = GatePort(line[2], "None")

            else:
                if line[2] == "0" or line[2] == "1":
                    self.in2 = GatePort(
                        f"Und. Priority {self.priority} Input", line[2])
                else:
                    self.in2 = GatePort(line[2], "None")

                self.out = GatePort(line[3], "None")


class GatePort():
    def __init__(self, id: str, value: str) -> None:
        self.id = id
        self.value = value
