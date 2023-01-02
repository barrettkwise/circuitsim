import parse as ps
import simulator as s

if __name__ == "__main__":
    parser = ps.CircuitParser("netlist.txt")
    lines = parser.show()
    for line in lines:
        sim = s.Simulator(lines[line])
        for i in sim.single():
            print(i)