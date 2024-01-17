import parse as ps
import simulator as s
import subprocess as sp


class Interface:
    def __init__(
        self, input_path: str, output_to_file: bool = False, output_path: str = None
    ) -> None:
        self.input_path = input_path

        if output_to_file:
            if output_path is None:
                sp.run(["touch", "output.txt"])
                output_path = "output.txt"

            self.output_path = output_path
            self.save_to_file()

        else:
            self.show()

    def show(self) -> list:
        parser = ps.CircuitParser(self.input_path)
        lines = parser.parse()
        sim = s.Simulator(lines)
        result = sim.simulate()
        return result

    def save_to_file(self) -> None:
        parser = ps.CircuitParser(self.input_path)
        lines = parser.parse()
        sim = s.Simulator(lines)
        result = sim.simulate()
        result.insert(0, parser.title)
        if self.output_path is not None:
            with open(self.output_path, "w") as output:
                for gate in result:
                    if isinstance(gate, str):
                        output.write(f"Circuit name: {gate}\n")
                        continue
                    output.write(f"Gate type: {gate.type}\n")
                    output.write(f"{gate.in1.id}: {gate.in1.value}\n")
                    if gate.type != "NOT":
                        output.write(f"{gate.in2.id}: {gate.in2.value}\n")
                    output.write(f"{gate.out.id}: {gate.out.value}\n\n")

        print(f"Output written to {self.output_path}.")
        return None