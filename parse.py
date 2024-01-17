class CircuitParser:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.title = ""
        self.circuit = {}

    def parse(self) -> dict:
        with open(self.filepath, "r") as file:
            circuit = file.read()

            lines = circuit.split("\n")
            current_line = None
            for line in lines:
                if line.startswith("."):
                    current_line = line[1:].strip(":{} ")
                    self.circuit[current_line] = []
                elif (
                    line.strip()
                    and current_line is not None
                    and not line.startswith(("!", "#", "}"))
                ):
                    self.circuit[current_line].append(line.strip().split(", "))

        return self.circuit