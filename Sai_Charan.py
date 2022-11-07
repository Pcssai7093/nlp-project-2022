def genBigrams(i):
    str=[]
    for j in range(0,len(i)-1):
            str.append(i[j:j+2])
    return str

def createBIndex(arr):
    d=dict()
    for i in arr:
        temp=[]
        temp=genBigrams(i)
        for j in temp:
            if(d.get(j)==None):
                d[j]=[]
                d[j].append(i)
            else:
                d[j].append(i)
    return d
