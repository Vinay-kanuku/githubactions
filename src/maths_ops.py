
def add(a,b) -> int:
    return a+b

def sub(a,b) -> int:
    return a-b

def mul(a,b) -> int:
    return a*b

def div(a,b) -> float:
    if a == 0:
        return 0

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

if __name__ == "__main__":
    print(add(1,2))
    print(sub(1,2))
    print(mul(1,2))
    print(div(1,2))

