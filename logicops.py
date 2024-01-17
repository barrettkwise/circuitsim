def safety_check(gate: str) -> bool:
    if gate in operations:
        return True
    else:
        return False


def NOT(a: str) -> str:
    if a == "1":
        return "0"
    else:
        return "1"


def AND(a: str, b: str) -> str:
    if a == "1" and b == "1":
        return "1"
    else:
        return "0"


def OR(a: str, b: str) -> str:
    if a == "1" or b == "1":
        return "1"
    else:
        return "0"


def XOR(a: str, b: str) -> str:
    if a != b:
        return "1"
    else:
        return "0"


def NAND(a: str, b: str) -> str:
    return NOT(AND(a, b))


def NOR(a: str, b: str) -> str:
    return NOT(OR(a, b))


def XNOR(a: str, b: str) -> str:
    return NOT(XOR(a, b))


operations = {
    "NOT": NOT,
    "AND": AND,
    "OR": OR,
    "XOR": XOR,
    "NAND": NAND,
    "NOR": NOR,
    "XNOR": XNOR,
}
