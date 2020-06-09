

def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    r = 0
    length = len(str(num))
    while(num>0):
        r = num % 10
        sum = sum + (r**length)
        num = num // 10

    if(temp == sum):
        print("{} is Armstrong Number".format(temp))
    else:
        print("{} is Not Armstrong Number".format(temp))


armstrong()
        