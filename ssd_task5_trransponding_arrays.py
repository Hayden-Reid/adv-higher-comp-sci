from array import ArrayType


row=5
col=2

def createArray():
    array=[[None]*col for index in range(row)]
    return array

def fillArray(array):
    num=0
    for x in range(row):
        for y in range(col):
            num=num+1
            array[x][y]=num
    return array


#transpose here
def transposeArray(array):
    col=5
    row=2
    array2=[[0]*col for index in range(row)]
    for i in range(col):
        for j in range(row):
            array2[j][i]=array[i][j]
    return array2
            
    




array=createArray()
array=fillArray(array)
array2=transposeArray(array)
print(array)
print(array2)