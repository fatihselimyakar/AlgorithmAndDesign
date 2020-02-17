import itertools

#############QUESTION1###############
def createBoxList( size ):
    boxes = []
    for i in range(0,(int)(size/2)):
        boxes.append("black")
    for i in range((int)(size/2),size):
        boxes.append("white")
    return boxes

def boxTail(boxList,low,middle):
    if(middle>=len(boxList)):
        return boxList
    boxList[low],boxList[middle]=boxList[middle],boxList[low]
    boxTail(boxList,low+2,middle+2)

def boxRec(boxList):
    return boxTail(boxList,1,(int)(len(boxList)/2))

#############QUESTION2###############

def findFakeCoin( arr ):
    if(len(arr)==1):
        return arr[0]
    if(len(arr)%2==0):
        if(sum( arr[0:(int)(len(arr)/2)] ) < sum( arr[(int)(len(arr)/2):len(arr)] )):
            return findFakeCoin(arr[0:(int)(len(arr)/2)])
        else:
            return findFakeCoin(arr[(int)(len(arr)/2):len(arr)])
    elif(len(arr)%2==1):
        if(sum( arr[0:(int)(len(arr)/2)] ) == sum( arr[(int)(len(arr)/2):len(arr)-1] )):
            return arr[len(arr)-1]
        elif(sum( arr[0:(int)(len(arr)/2)] ) < sum( arr[(int)(len(arr)/2):len(arr)-1] )):
            return findFakeCoin(arr[0:(int)(len(arr)/2)])
        else:
            return findFakeCoin(arr[(int)(len(arr)/2):len(arr)-1])

#############QUESTION3###############
quicksortSwapNum = 0
insertionSortSwapNum = 0
def insertionSort(arr): #decrease and conquer
    global insertionSortSwapNum
    for i in range(1,len(arr)):
        current=arr[i]
        position=i-1
        while position>=0 and current<arr[position]:
            arr[position+1]=arr[position]
            insertionSortSwapNum+=1
            position-=1
        arr[position+1]=current
    return insertionSortSwapNum

def rearrange(arr,low,high):
    global quicksortSwapNum
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            quicksortSwapNum+=1
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    quicksortSwapNum+=1
    return ( i+1 )

def quickSort(arr,low,high):#divide and conquer
    if high > low:
        index = rearrange(arr,low,high)
        quickSort(arr, low, index-1) 
        quickSort(arr, index+1, high)
    return quicksortSwapNum

#############QUESTION4###############
def findMedian(arr):
    insertionSort(arr)
    if(len(arr)%2==0):
        return (arr[(int)(len(arr)/2)]+arr[(int)(len(arr)/2-1)])/2
    else:
        return arr[(int)(len(arr)/2)]

#############QUESTION5###############
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

def optimalSubArray(arr):
    value=(max(arr)+min(arr))*(len(arr)/4)
    minMult=None
    minList=None
    for i in range(1,len(arr)+1):
        combs=itertools.combinations(arr,i)
        minList,minMult = (recSub((list)(combs),value,minList,minMult))
    return minList

def recSub(combs,value,minList,minMult):
    if(len(combs)==0):
        return minList,minMult
    elif(sum(combs[0])>=value):
        if( (minMult==None) or (multiply(combs[0])<minMult) ):
            minMult=multiply(combs[0])
            minList=combs[0]
    return recSub(combs[1:len(combs)],value,minList,minMult)

def main():
    print ("TEST FUNCTION")

    print ("\n**Box Test**")
    boxList=createBoxList(8)
    print ("Unchanged list:",boxList)
    boxRec(boxList)
    print ("Changed list:",boxList)

    print ("\n**Fake Coin Test**")
    coins=[2,2,1,2,2,2,2]
    print ("Coin list:",coins)
    print ("Fake coin:",findFakeCoin(coins))

    print ("\n**Insertion and quicksort test**")
    arr=[10,9,8,7,6,5,4,3,2,1]
    print ("Unsorted array:",arr)
    print ("Quicksort number of swap:",quickSort(arr,0,len(arr)-1))
    print ("Quicksorted array:",arr)
    arr2=[10,9,8,7,6,5,4,3,2,1]
    print ("Unsorted array:",arr2)
    print ("Insertion sort number of swap:",insertionSort(arr2))
    print ("Insertion sorted array:",arr2)

    print ("\n**Find median test**")
    arr3=[10,20,12,13,19,1]
    print ("Median array:",arr3)
    print ("Median is:",findMedian(arr3))

    print ("\n**Find optimal sub array**")
    arr4=[2,4,7,5,22,11]
    print ("Array is:",arr4)
    print ("Optimal sub array is:",optimalSubArray(arr4))

    


if __name__ == '__main__':
    main()