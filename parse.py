from io import FileIO
# Converts file to dictionary

class CircuitParser:
    @staticmethod
    def __skip(skips: int, file: FileIO) -> FileIO:
        for i in range(0, skips - 1):
            file.readline()

        return file

    def __init__(self, filepath: str) -> None
        self.filepath = filepath
        self.title = ""
        self.circuit = {}

    def show(self) -> dict:
        self.parse()
        return self.circuit

    def parse(self) -> None
        with open(self.filepath, "r") as input:
            line_c = 1
            for num, line in enumerate(input.readlines(), 1):
                if "!" in line:
                    self.title = line[1:]

                if f".line{line_c}" in line:
                    lines = []
                    input.seek(0)
                    input = CircuitParser.__skip(num + 1, input)

                    while True:
                        line = input.readline()
                        if "}" in line:
                            break

                        line = line.strip()
                        lines.append(line.split(", "))

                    self.circuit.setdefault(f"Line {line_c}", tuple(lines))
                    line_c += 1

                else:
                    continue
