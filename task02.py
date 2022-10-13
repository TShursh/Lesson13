# числа Фибоначи  0 1 1 2 3 5 8 13 21 34 55

def fibonacci(index):
    first = 0
    second = 1

    if index < 2:
        return index
    for i in range(2, index + 1):
        third = first + second
        first = second
        second = third

    return third


def main():
    index = int(input("Input index: "))
    element = fibonacci(index)

    msg = f"fibonacci [{index}] ---> [{element}]"

    print(msg)


main()
