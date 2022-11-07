
def findPrecision(list1,list2,fun):
    size = len(list1)
    i=0
    matched = 0
    while (i<size):
        if(fun(list1[i])==list2[i]):
            matched=matched + 1
        i=i+1
    return (matched/size)