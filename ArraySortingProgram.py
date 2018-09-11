import random
#selection sort
arr = [] 
for z in range (0,10):
    arr.append(round(random.random()*10)) 
print(arr) 
#arr is randomly generated and has 10 elemetns
#arr is an unsorted array
for x in range (0,len(arr)):
    lowest = arr[x] 
    lowestIndex = x 
    for y in range (x+1,len(arr)):
        if(arr[y]<arr[lowestIndex]):
            lowest = arr[y] 
            lowestIndex = y 
    arr[lowestIndex] = arr[x] 
    arr[x] = lowest 
print(arr) 
#the end result is a sorted version of the arr array
    
                
    
