
def suma(x: int, y: int, como_string: bool = False) -> int:
    if como_string:
        return str(x + y)
    else:
        return x + y


assert suma(1,2) == 3
assert suma(2,2) == 4
assert suma(3,2) == 5
assert suma(10,2) == 12
assert suma(1,1, como_string=True) == "2"
assert isinstance(suma(1,1, como_string=True), int) # simulación
assert suma(1,2) == 3