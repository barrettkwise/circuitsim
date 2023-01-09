#Converts file to dictionary
class CircuitParser():
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.circuit = {}

    def show(self):
        self.parse()
        return self.circuit

    def parse(self):
        with open(self.filepath, "r") as output:
            line_c = 1
            for num, line in enumerate(output.readlines(), 1):

                if f".line{line_c}" in line:
                    lines = []
                    output.seek(0)
                    output = self.__skip(num+1, output)

                    while True:
                        line = output.readline()
                        if "}" in line:
                            break

                        line = line.strip()
                        lines.append(line.split(", "))

                    self.circuit.setdefault(f"Line {line_c}", tuple(lines))
                    line_c += 1

                else:
                    continue

    def __skip(self, skips: int, file):
        for i in range(0, skips-1):
            file.readline()

        return file
