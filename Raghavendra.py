def my_ranker(ranks):

    ranklist={}
    p1=[x for k in ranks for x in k]

    for x in p1:
        if x in ranklist.keys():
            t=ranklist.get(x)+1
            ranklist.update({x:t})
        else:
            ranklist[x]=1

    ordered=[[0,0]]

    for x in ranklist:
        i=0
        for y in ordered:
            if(ranklist.get(x)>y[1]):
                ordered.insert(i,[x,ranklist.get(x)])
                break
            else:
                i=i+1

    ordered.remove([0,0])
    t=[ordered[0][0],ordered[0][1]]

    for x in ordered:
        if(x[1]==t[1]):
            if(len(x[0])<len(t[0])):
                t=x
        else:
            break
    return t[0]


ranks=[['abc','bcda','cdfh'],['dedhg','edde','cdfh'],['sdfg','dedhg','aedh','abc']]











