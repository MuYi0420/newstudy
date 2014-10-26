def SaySome(name, words):
	print (name +':'+ words)
SaySome('Muyi','I love you')
SaySome(words='I love you',name='MuYi')   #关键字参数

def SaySome2(name='Muyi', words='I love you'):   #默认参数
	print (name +':'+ words)
SaySome2()
def SaySome3(*params):
    print ('length: ' ,len(params))
    print ('second:' ,params[1])
    
