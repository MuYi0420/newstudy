def discounts(price, rate):
    final_price=price*rate
    # print （old_price)  结果为全局变量，可以访问，不可修改
    old_price = 50
    print ('修改后的old_price的值是1:',old_price)    #新建一个old_price的局部变量，与全局变量无关
    return final_price
old_price = float(input('请输入原价： '))
rate = float(input("请输入折扣率： "))
new_price=discounts(old_price, rate)
print ('修改后的old_price的值是2:',old_price)
