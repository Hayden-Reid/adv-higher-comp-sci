def readfile(file):
    scores=[[None]*15 for index in range(6)]
    with open(file) as readfile:
        line=readfile.readline().rstrip("\n")
        linecounter=0
        while line:
            items=line.split(',')
            for index in range(len(items)):
                scores[linecounter][index]=items[index]
                
            linecounter+=1
            line=readfile.readline().rstrip("\n")
    return scores


def dispresults(scores):
    for x in range(len(scores)-1):
        result = scores[x+1][0]+" "
        totalpercentage=0
        
        for y in range(len(scores[x+1])-1):
            result+=str(round(int(scores[x+1][y+1])/int(scores[0][y+1])*100))+"% "
            totalpercentage+=round(int(scores[x+1][y+1])/int(scores[0][y+1])*100)
        
        result+="average = " + str(round(totalpercentage/(len(scores[x+1])-1)))+"%"
        print (result)
        
scores=readfile("TextFile1.txt")
dispresults(scores)
        
