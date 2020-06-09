import array as arr
arr = [10,60,26,35,40]
def largestelement():
    max = arr[0]
    
    for i in range(1,5):
        if(arr[i] > max):
            max = arr[i]
            print("The largest element is:",max)

largestelement()
