
import string
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
    
 print(words) 