def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError(Cannot divide by zero)
    return a / b


def main():
    print(Addition:, add(10, 5))
    print(Subtraction:, sub(10, 5))
    print(Division:, divide(10, 5))
def main():
    print(Addition:, add(10, 5))
    print(Subtraction:, sub(10, 5))


if __name__ == __main__:
    main() 
