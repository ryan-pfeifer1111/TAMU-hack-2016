def sort(arr):
    for x in range (0,len(arr)):
        lowest = arr[x] 
        lowestIndex = x 
        for y in range (x+1,len(arr)):
            if(arr[y]<arr[lowestIndex]):
                lowest = arr[y] 
                lowestIndex = y 
        arr[lowestIndex] = arr[x] 
        arr[x] = lowest 
    return arr 

def median(arr):
    answer = -1 
    if(len(arr)%2==1):
        answer = arr[round(((len(arr))/(2)-.5))] 
    else:
        a1 = (float)(arr[round(((len(arr)-1)/(2)-.5))])
        a2 = (float)(arr[round(((len(arr)-1)/(2)+.5))])
        answer = (a1+a2)/2 
    print("Median: %s" %answer) 

def mean(arr):
    num = 0 
    for x in range (0,len(arr)):
        num = num + (float)(arr[x]) 
    answer = (float)(num/len(arr)) 
    print("Mean: %s" %answer) 
    return answer 

def Range(arr):
    answer = arr[len(arr)-1]-arr[0] 
    print("Range:  %s"%answer) 

def standardDev(arr,avg):
    average = avg 
    degreesOfFreedom = len(arr)-1 
    num = 0 
    for x in range (0,len(arr)):
        num = num + (arr[x]-avg)**2 
    s = (num/degreesOfFreedom)**(1/2) 
    print("Standard Deviation:  %s"%s) 

#''''''''''''''''''''''''''''''''''''''''''''''''#

print("Welcome to the data organizer!") 
arr = [] 
done = 1 
arrayLength = int(input("How many elements do you have?  ")) 
x = 0 
while(x<arrayLength):
    element = (float)(input("What is your next value?  ")) 
    arr.append(element) 
    x = x+1 
arr = sort(arr) 
print("Sorted array: %s" %arr) 
avg = mean(arr) 
median(arr) 
Range(arr) 
standardDev(arr,avg) 

    
