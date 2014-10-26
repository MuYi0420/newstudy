member = ['A','B','C']
print (member)
member.append('D')
print (member)
member.extend(['E','F'])   #extend 括号里的对象为列表，而非元素，不能member.extend('E','F')
print (member)
member.insert(1,'G')
print (member)
member = [1,2,'C',[4,5],6，7,8,9]
print (member)       #列表里的元素可以为所有东西！
member.remov('C')    #必须知道元素的名字
print (member)
del member[1]        #del member 表示删除整个列表
print (member)
member.pop()
print (member)
member.pop(1)        #删除位置为第2个元素
print (member)
