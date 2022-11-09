
def findPrecision(list1,list2,fun):
    size = len(list1)
    i=0
    matched = 0
    while (i<size):
        if(fun(list1[i])==list2[i]):
            matched=matched + 1
        i=i+1
    for i in range(1,40):
        print ("caculating accuracy...")
    return ("----------accuracy is: " + str(matched/size))