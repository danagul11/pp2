def multiply(mylist):
    a = 1
    for i in mylist:
        a *= i
    return a
list = [8, 2, 3, -1, 7]
print(multiply(list))