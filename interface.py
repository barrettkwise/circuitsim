import parse as ps
import simulator as s

def convert_dict(d):
    lists = [item for sublist in d.values() for item in sublist]
    t = tuple(lists)
    return t

class Interface():
    def __init__(self, path: str):
        self.path = path

    # Simulate each line seperately 
    def single(self):
        parser = ps.CircuitParser(self.path)
        lines = parser.show()
        for line in lines:
            sim = s.Simulator(lines[line])
            yield sim.simulate()
    
    # Simulate all lines together
    def multiple(self):
        parser = ps.CircuitParser(self.path)
        lines = parser.show()
        sim = s.Simulator(convert_dict(lines))
        return sim.simulate()