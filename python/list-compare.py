list1 = [123]
list2 = [234]
s1 = list1 > list2         #false
list1 = [123,345]
list2 = [234,123]
s2 = list1 > list2         #false ,只比较第一个
s3 = list1 < list2         #true
list3 = [123,45]
s4 = ( list1 == list3 )    #false ,全部都一样才行
list4 = list(range(10))
list4.reverse()
list5 = [32,51,2352,3,24,6435,2]
list5.sort()
list5.sort(reverse=True)
print (s1,s2,s3,s4,list4,list5)
list6 = list(range(10))
list7 = list6
list8 = list6[:]
print (list6,list7,list8)
list6.reverse()           # 不能list6=list6.reverse()，会出现None 
print (list6,list7,list8) #等于号只是相当于多了一个指向列表的标签，而分片是重新建一个列表
list6=list6.reverse()
print (list6)
