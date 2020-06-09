num = int(input("Enter a length: "))

def fibonacci():
    n1, n2 = 0,1
    count = 0
    while(count < num):
        m = n1 + n2
        n1 = n2
        n2 = m
        count = count + 1
        print(n1)

fibonacci()
    

