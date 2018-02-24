def outer():
    x = "hello"

    def inner():
        return x

    def inner_2():
        return x + " world"

    #print(inner())
    #print(inner_2())

    return inner, inner_2

#print(outer())
#func_1 = outer()
#print(func_1())

f1, f2 = outer()
print(f1())
