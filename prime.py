num = int(input("Enter a number: "))

def IsPrime():
    flag = False
    for i in range(2,(num // 2)+1):
        if num%i == 0:
            flag = True
            break

    if num == 1:
        print("1 is neither prime nor composite")
    if flag == False:
        print("This is prime number")
    else:
        print("This is not prime number")

            
IsPrime()
