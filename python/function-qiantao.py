def fun1():
    print('fun1() is going')
    def fun2():
        print('fun2() is going')
    fun2()
def fun3():
    print('fun3() is going')
    fun1()
    fun4()
# fun3() wrong，fun4() is not defined
def fun4():
    print('fun4() is going')
fun3()    
