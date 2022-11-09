import Sai_Charan as sc
import Chandra_Sekhar as cs
import Raghavendra as rv
import Metrics as m

# * need to be in other file bargav's contribution-------
arr = []
with open("sortdict.txt",encoding="utf-8") as f:
    for line in f:
        temp = line.strip("\n")
        arr.append(temp)

# * --------------
Bindex=sc.createBIndex(arr)

    
def suggestSpelling(string):
    print ("checking word")
    if(cs.checkSpelling(string,arr)==False):
        slist=cs.suggestedList(string,Bindex)
        return (rv.my_ranker(slist))
    else:
        return string 


list1 = ['అంకకాండు', 'అంకగణితం', 'అంకణము', 'అంకము', 'అంకపాళ', 'అంపొంకములు', 'అంకము', 'అంకమ్మ', 'అంకవిద్య', 'అంకాట', 'అంకాడు', 
'అంకాపొంకములు', 'అంకరించు', 'అంకితం', 'అంకితము', 'అంకియ', 'అంకియము', 'అంకిలి', 'అంకిలిపడు','అంకకాండు', 'అంకగణితం', 'అంకణము', 'అంకము', 'అంకపాళ', 'అంపొంకములు', 'అంకము', 'అంకమ్మ', 'అంకవిద్య', 'అంకాట', 'అంకాడు', 
'అంకాపొంకములు', 'అంకరించు', 'అంకితం', 'అంకితము', 'అంకియ', 'అంకియము', 'అంకిల', 'అంకిలిపడు']
#Random list
list2 = ['అంకకాండు', 'అంకగణితం', 'అంకణము', 'అంకనము', 'అంకపాళి', 'అంకపొంకములు', 'అంకము', 'అంకమ్మ', 'అంకవిద్య', 'అంకాట', 'అంకాడు', 
'అంకాపొంకములు', 'అంకారించు', 'అంకితం', 'అంకితము', 'అంకియ', 'అంకియము', 'అంకిలి', 'అంకిలిపడు','అంకకాండు', 'అంకగణితం', 'అంకణము', 'అంకనము', 'అంకపాళి', 'అంకపొంకములు', 'అంకము', 'అంకమ్మ', 'అంకవిద్య', 'అంకాట', 'అంకాడు', 
'అంకాపొంకములు', 'అంకారించు', 'అంకితం', 'అంకితము', 'అంకియ', 'అంకియము', 'అంకిలి', 'అంకిలిపడు']

print (m.findPrecision(list1,list2,suggestSpelling))
