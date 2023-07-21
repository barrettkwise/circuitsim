import parse as ps
import simulator as s


class Interface:
    def __init__(self, path: str) -> None:
        self.path = path
        if str(input("Would you like to save the output to a file? (y/n): ")).lower() == "y":
            output_path = str(input("Enter the path to the output file: "))
            if output_path == "" or not output_path.endswith(".txt"):
                raise ValueError("Invalid file path")
            else:
                self.output_path = output_path

        else:
            self.output_path = None

    def show(self):
        parser = ps.CircuitParser(self.path)
        lines = parser.show()
        print(f"Circuit name: {parser.title}")
        sim = s.Simulator(lines)
        result = sim.simulate()
        if self.output_path is not None:
            with open(self.output_path, "w") as output:
                for gate in result:
                    output.write(f"Gate type: {gate.type}\n")
                    output.write(f"{gate.in1.id}: {gate.in1.value}\n")
                    if gate.type != "NOT":
                        output.write(f"{gate.in2.id}: {gate.in2.value}\n")
                    output.write(f"{gate.out.id}: {gate.out.value}\n\n")

        return result


i = Interface("example.txt")
for c in i.show():
    print(f"Gate type: {c.type}")
    print(f"{c.in1.id}: {c.in1.value}")
    if c.type != "NOT":
        print(f"{c.in2.id}: {c.in2.value}")
    print(f"{c.out.id}: {c.out.value}")
    print("\n")
