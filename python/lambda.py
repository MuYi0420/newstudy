g = lambda x : 2 * x + 1
print (g(5))
h = lambda x , y : x + y
print (h(5,6))
list(filter(None, [1, 0, False, True])) #过滤False的数
def odd(x):
    return x % 2
temp = range(10)
show=filter(odd, temp)
print (list(show))
show=list(filter(lambda x: x % 2 ,range(10)))  #将range里的值带入前边的函数，并筛选出结果为True的range
print (show)
show=list(map(lambda x: x * 2 ,range(10))) #将range里的值带入前边的函数
print (show)
