import parse as ps
import simulator as s


class Interface():
    def __init__(self, path: str):
        self.path = path

    def show(self):
        parser = ps.CircuitParser(self.path)
        lines = parser.show()
        print(f"Circuit name: {parser.title}")
        sim = s.Simulator(lines)
        return sim.simulate()


i = Interface("example.txt")
for c in i.show():
    print(f"Gate type: {c.type}")
    print(f"{c.in1.id}: {c.in1.value}")
    if c.type != "NOT":
        print(f"{c.in2.id}: {c.in2.value}")
    print(f"{c.out.id}: {c.out.value}")
    print("\n")
