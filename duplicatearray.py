array =[1,2,3,2,1]

def duplicatearray():
    

    for i in range(0, len(array)):    
        for j in range(i+1, len(array)):    
            if(array[i] == array[j]):    
                print(array[j])
 

duplicatearray()