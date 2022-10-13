import timeit

print("list: ", timeit.timeit("[1,2,3,4,5,6,7,8,9,10]", number=1_000_000_000))
print("tuple: ", timeit.timeit("(1,2,3,4,5,6,7,8,9,10)", number=1_000_000_000))

# git config --global user.name TShursh
# git config --global user.email tati.irtik@gmail.com