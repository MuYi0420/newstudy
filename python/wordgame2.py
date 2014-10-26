print ('------------------a easy game----------------')
temp = input("please guess a number: ")
guess = int(temp)
n=1
while guess != 8 and n <= 3:
    print (str(n)+' time\n')
    temp = input('sorry, you are wrong!')
    guess = int(temp)
    if guess == 8:
        print ('you are right!')
    else:
        print ('SORRY,YOU ARE WRONG!')
    n=n+1
print ('game over')
    
