
f=open("C:/Users/chandra sekhar/Desktop/chandra sekhar imp/SEM-5/NLP/project/code/group codes/data.txt","r",encoding='utf-8')
g=f.read()
arr1=' '.join(g.splitlines())
arr=arr1.split(" ")
print(arr)
# d={}
# tup=[]


# * sai charan's
def genBigrams(i):
    str=[]
    firstLast=''
    firstLast=i[len(i)-1]+i[0]
    str.append(firstLast)
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



