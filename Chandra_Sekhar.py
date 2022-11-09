def checkSpelling(word,ary):
    print ("checking word .... " + word)
    for str in ary:
        if (str==word):
            return True
    return False

def suggestedList(word,bIndex):
    print ("generating possible words ... for word" + word)
    list=[]
    i=0 
    size=len(word)
    while(i<size-2):
        bigram=word[i]+word[i+1]
        if(bIndex.get(bigram)!=None):
            list.append(bIndex.get(bigram))
        i=i+1
    bigram=word[size-1]+word[0]
    if(bIndex.get(bigram)!=None):
            list.append(bIndex.get(bigram))
    return list    