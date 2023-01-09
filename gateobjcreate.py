#Create gate object for each gate
class GateObject():
    def __init__(self, line: list) -> None:
        self.type = line[0]
        self.in1 = line[1]
        if len(line) < 4:
            self.in2 = ""
            self.out = [line[2], None]
        else:
            self.in2 = line[2]
            self.out = [line[3], None]
        