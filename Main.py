import Sai_Charan as sc
import Chandra_Sekhar as cs
import Raghavendra as rv
import Metrics as m
import string

# * need to be in other file bargav's contribution-------
arr = []
with open("sortdict.txt",encoding="utf-8") as f:
    for line in f:
        temp = line.strip("\n")
        print ("reading training data......")
        arr.append(temp)

def remove_punc(string):
     punc = '''!()-[][0123456789][ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz ]{};:'"\, <>./?@#$%^&*_~'''
     for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
     return string
     
with open ("sortdict.txt","r",encoding='utf-8') as f:
 text=f.read()
 words= text.split()
 words = [remove_punc(i) for i in words]
 while("" in words):
  words.remove("")
 words.remove(words[0])
    
#  print(words) 
arr = arr + words
arr = set(arr)
arr = list(arr)
print (len(arr))
# * --------------

Bindex=sc.createBIndex(arr)

def suggestSpelling(string):
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

# print (m.findPrecision(list1,list2,suggestSpelling))