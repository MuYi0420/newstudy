def FunX(x):
    def FunY(y):
        return x * y
    return FunY
i = FunX(8)
print (type(i))
print (i(5))
print (FunX(8)(5))
def Fun1():
    x=5
    def Fun2():
        nonlocal x   #不加这个nonlocal会报错，因为相对于Fun2()，x为外部变量，不能修改，只能调用
        x *= x
        return x
    return Fun2()
Fun1()
