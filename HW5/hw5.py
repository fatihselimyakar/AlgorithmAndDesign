######################QUESTION1##########################
def minCostBussiness(city1,city2):
    PN=[0 for i in range(len(city1))]
    PS=[0 for i in range(len(city2))]
    PN[0]=city1[0]
    PS[0]=city2[0]
    for i in range(1,len(city1)):
        PN[i]=city1[i]+min(PN[i-1],10+PS[i-1])
        PS[i]=city2[i]+min(PS[i-1],10+PN[i-1])
    return min(PN[len(city1)-1],PS[len(city2)-1])

##############QUESTION2################
def maxSymposiums(symposiums): 
    selects=[]
    i = 0
    selects.append(i)
    for j in range(len(symposiums) ): 
        if symposiums[j][0] >= symposiums[i][1]: 
            selects.append(j)
            i = j 
    return selects

##################QUESTION3#####################

sumSize, tempSize = 200,100 #hardcoded indexes 
def fillZeros(arr,size1,size2):
    arr = [[0 for x in range(size1)] for y in range(size2)]
    for i in range(0,size2):
        for j in range(0,size1):
            arr[i][j]=0
    return arr
  
dp=None
mark=None
dp = fillZeros(dp,sumSize,tempSize)  
mark = fillZeros(mark,sumSize,tempSize)
  
setArray=[]
def zeroSubsetCount(i, s, arr, n) : 
    if (i==n): 
        if (s==0) : 
            return 1;  
        else: 
            return 0;  
    if (mark[i][s+tempSize]): 
        return dp[i][s+tempSize];  
    mark[i][s+tempSize]=1;  
    dp[i][s+tempSize] = (zeroSubsetCount(i+1,s+arr[i],arr,n)+zeroSubsetCount(i+1,s,arr,n))
    #print(dp[i][s+tempSize])
    return dp[i][s + tempSize];  
  
def wrapperZeroSubset(arr, n):
    return zeroSubsetCount(0, 0, arr, n)>1

#################################QUESTION4##############################
def alignmentString(str1,str2,mm,gap,match):

    m=len(str1)
    n=len(str2)
    dp=None
    dp=fillZeros(dp,n+m+1,n+m+1)

    for i in range(0,n+m+1):
        dp[i][0]=i*gap
        dp[0][i]=i*gap

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(str1[i-1]==str2[j-1]):
                dp[i][j]=dp[i-1][j-1]+match
            else:
                dp[i][j]=max(dp[i-1][j-1]+mm,dp[i-1][j]+gap,dp[i][j-1]+gap)

    length=m+n
    i=m
    j=n
    posX=length
    posY=length

    arrStr1=[0 for x in range(length+1)]
    arrStr2=[0 for x in range(length+1)]

    while(not (i==0 or j==0)):
        if(str1[i-1]==str2[j-1]):
            arrStr1[posX] = str1[i-1]
            posX-=1
            arrStr2[posY] = str2[j-1]
            posY-=1
            i-=1
            j-=1
        elif(dp[i - 1][j - 1] + mm == dp[i][j]):
            arrStr1[posX] = str1[i-1]
            posX-=1
            arrStr2[posY] = str2[j-1]
            posY-=1
            i-=1
            j-=1
        elif(dp[i - 1][j] + gap == dp[i][j]):
            arrStr1[posX] = str1[i - 1]; 
            arrStr2[posY] = '-'; 
            posX-=1
            posY-=1
            i-=1
        elif(dp[i][j - 1] + gap == dp[i][j]):
            arrStr1[posX] = '-'; 
            arrStr2[posY] = str2[j-1]; 
            posX-=1
            posY-=1
            j-=1
    while(posX>0):
        if (i > 0):
            i-=1
            arrStr1[posX] = str1[i]; 
            posX-=1   
        else:
            arrStr1[posX]='-' 
            posX-=1
    while(posY>0):
        if (j > 0):
            j-=1
            arrStr2[posY] = str1[j]; 
            posY-=1
        else:
            arrStr2[posY]='-' 
            posY-=1

    id = 1; 
    for i in range(length,0,-1):
        if(arrStr2[i]=='-' and arrStr1[i]== '-'):
            id=i+1
            break

    total=0
    wordCounter=0
    limit=min(len(str1),len(str2))
    #print(dp[m][n])
    for i in range(id,length+1):
        print(arrStr1[i],end='')
        if(limit!=wordCounter):
            if(arrStr1[i]!='-' and arrStr2[i]!='-' ):
                wordCounter+=1
                if(arrStr1[i]==arrStr2[i]):
                    total+=2
                else:
                    total-=2
            else:
                total-=1
    print()
    for i in range(id,length+1):
        print(arrStr2[i],end='')
    print()
    print("The cost is:",total)

#################################QUESTION5##############################
def ancientComputer(numbs): 
    totalOperations = 0
    templateNumbs = numbs.copy()
    opInOneStage = min(templateNumbs)
    templateNumbs.remove(opInOneStage)
    while(len(templateNumbs)!=0):
        minElement = min(templateNumbs)
        templateNumbs.remove(minElement)
        opInOneStage += minElement
        totalOperations += opInOneStage
    return totalOperations
  
# driver code 
def main():
    NY=[1,3,20,30]
    SF=[50,20,2,4]
    print("Minimum cost in business:",minCostBussiness(NY,SF))

    symp = [[1,2], [3,4], [0,6], [5,7], [8,9], [5,9]] 
    print("Selected symposiums(indexwise):",maxSymposiums(symp))

    arr = [ 1,2,3,-3,-2,2];  
    n = len(arr);  
    print ("Is there any 0 sum subset:",wrapperZeroSubset(arr,n))

    alignmentString("SLIME","ALIGNMENT",-2,-1,1)

    A = [20,40,10,50]  
    print("Needed minimum operations:",ancientComputer(A))
  
if __name__== "__main__":
  main()