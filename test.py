import parse as ps
import simulator as s

if __name__ == "__main__":
    parser = ps.CircuitParser("netlist.txt")
    lines = parser.show()
    for line in lines:
        print(line)
        sim = s.Simulator(lines[line])
        print(sim.single())