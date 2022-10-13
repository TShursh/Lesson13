# Глубина рекурсии:

# def recurs(count):
#     print(count)
#     count += 1
#     recurs(count)
#
# recurs(1)

def summ(ls):
    if len(ls) == 1:
        return ls[0]

    return ls[0] + summ(ls[1:])


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
