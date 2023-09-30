def only_ints(x,i):
    return True if type(x) is int and type(i) is int else False

print(only_ints(1,'a'))