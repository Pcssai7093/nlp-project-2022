import Sai_Charan as sc
import Chandra_Sekhar as cs
import Raghavendra as rv

# * need to be in other file bargav's contribution-------
f=open("C:/Users/chandra sekhar/Desktop/chandra sekhar imp/SEM-5/NLP/project/code/group codes/data.txt","r",encoding='utf-8')
g=f.read()
arr1=' '.join(g.splitlines())
arr=arr1.split(" ")
print(arr)
# * --------------


Bindex=sc.createBIndex(arr)
string="కాలేజ"
if(cs.checkSpelling(string,arr)==False):
    slist=cs.suggestedList(string,Bindex)
    print (rv.my_ranker(slist))