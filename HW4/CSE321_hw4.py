#############QUESTION1-B###############
def oneChangeToSpecial(matrix):
    for i in range (0,len(matrix)-1):
        for j in range (0,len(matrix[0])-1):
            #the 1-a's formula's left and rightsides
            leftside=matrix[i][j] + matrix[i+1][j+1]
            rightside=matrix[i][j+1] + matrix[i+1][j]
            #if it does not fit the formula then add the diff to fit
            if  leftside > rightside:
                diff=leftside-rightside
                matrix[i][j+1]+=diff

#############QUESTION1-C###############
def mergeSort(arr): 
    if len(arr) >1: 
        #finding mid of array and divide the 2 halves
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:]
        #Sorting the halves 
        mergeSort(left) 
        mergeSort(right)
        i = j = k = 0
        # Copy the temp arrays
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1

#merge sorts the all of rows in the matrix and appends first element in matrix the return array
def leftmostMin(matrix):
    lmElements=[]
    for i in range(len(matrix)):
        mergeSort(matrix[i])
        lmElements.append(matrix[i][0])
    return lmElements

#############QUESTION2###############

def findkth( arr1,arr2,k,index1,index2 ):
    size1=len(arr1)
    size2=len(arr2)
    #base cases
    if(index1==size1):
        return arr2[index2+k-1]
    if(index2==size2):
        return arr1[index1+k-1]
    if(k==0 or k>(size1-index1)+(size2 - index2)):
        return -1
    if(k==1):
        if(arr1[index1]<arr2[index2]):
            return arr1[index1]
        else:
            return arr2[index2]
    #the process: includes find middle of two arrays and returns elements
    current = (int)(k/2)
    if(current-1 >= size1-index1):
        if(arr1[size1 - 1]< arr2[index2 + current -1]):
            return arr2[index2 + (k-(size1-index1)-1)]
        else:
            return findkth(arr1,arr2,k-current,index1,index2+current)
    if(current -1 >= size2-index2):
        if(arr1[size2-1]<arr2[index2+current-1]):
            return arr1[index1 + (k-(size2-index2)-1)]
        else:
            return findkth(arr1,arr2,k-current,index1+current,index2)
    elif(arr1[current+index1-1]<arr2[current+index2-1]):
        return findkth(arr1,arr2,k-current,index1+current,index2)
    else:
        return findkth(arr1,arr2,k-current,index1,index2+current)

################QUESTION 3#####################
def maxSumOfLeftRight(arr, left, middle, length) : 
    resArray=[]
    #Include elements on left of mid. 
    sum = 0 
    leftSum = float("-inf") 
    for i in range(middle, left-1, -1) : 
        sum = sum + arr[i]  
        if (sum > leftSum) : 
            leftSum = sum 
            resArray.append(arr[i])

    sum = 0
    rightSum = float("-inf")
    for i in range(middle + 1, length + 1) : 
        sum = sum + arr[i] 
        if (sum > rightSum) : 
            rightSum = sum 
            resArray.append(arr[i])

    return leftSum + rightSum,resArray; 
  
  
def maxContSum(arr, left, length) :   
    #only one element 
    if (left == length) : 
        return arr[left],None
    middle = (left + length) // 2
  
    msas1=maxContSum(arr, left, middle)[0]
    msas2=maxContSum(arr, middle+1, length)[0]
    mcs=maxSumOfLeftRight(arr, left, middle, length)
    res=mcs[1]
    return max(msas1,msas2,mcs[0]),res

################QUESTION4#####################
ct=0
def coloring(Graph, color, vertexPos, c):  
    global ct
    nOfVertex=len(Graph[0])
    if color[vertexPos] != -1 and color[vertexPos] != c:  
        return False 
    # color this pos as c and all its neighbours and 1-c  
    color[vertexPos] = c  
    res = True 
    for i in range(0,nOfVertex):
        ct+=1  
        if Graph[vertexPos][i]:  
            if color[i] == -1:  
                res = res & coloring(Graph, color, i, 1-c)   
            if color[i] !=-1 and color[i] != 1-c:  
                return False 
        if not res:  
            return False 
    return True 
   
def findBipartite(Graph):  
    color = [-1] * len(Graph[0])  
    pos = 0 
    return coloring(Graph, color, pos, 1)

################QUESTION5###################
def findBestDay(cost,price):
    gainArray=[]
    #for the reporting make money
    noDayMakeMoney=True
    #fills gain array with gains and gain's days
    for i in range(0,len(cost)-1):
        gain=price[i+1]-cost[i]
        gainArray.append([gain,i+1])
        if gain > 0:
            noDayMakeMoney=False
    #sorts the gain array's first dimension
    mergeSort(gainArray)
    return gainArray[len(cost)-2][1],noDayMakeMoney

#Driver code
def main():
    #Question1b's test scenerio
    matrix=[[37,23,22,32],[21,6,7,10],[53,34,30,31],[32,13,9,6],[43,21,15,8]]
    oneChangeToSpecial(matrix)
    print ("one changed matrix:",matrix)

    #Question1c's test scenerio
    matrix1=[[10,17],[17,22],[24,28],[11,13],[45,44],[36,33],[75,66]]
    print ("leftmost minimums are:",leftmostMin(matrix1))

    #Question2's test scenerio
    arr1=[2, 3, 9]
    arr2=[1, 4, 15,20]
    print("Kth element is:",findkth(arr1,arr2,6,0,0))

    #Question3's test scenerio 
    arr = [5, -6, 6, 7, -6, 7, -4, 3] 
    resArr=[]
    max_sum,resArr = maxContSum(arr, 0, len(arr)-1)
    print("Maximum contiguous sum is %d. Maximum array is:" %(max_sum),resArr)

    #Question4's test scenerio
    G = [[0, 1, 0, 1, 0],  
    [1, 0, 1, 0, 1],  
    [0, 1, 0, 1, 0],  
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]]
    print ("Is bipartite?:%r" %(findBipartite(G)))

    #Question5's test scenerio
    cost = [5,11,2,21,5,7,8,12,13,None]
    price = [None,7,9,5,21,7,13,10,14,20]
    result=findBestDay(cost,price)
    print ("Day %d's gain is maximum. There is no day make money: %r"  %(result[0],result[1]))



if __name__ == '__main__':
    main()