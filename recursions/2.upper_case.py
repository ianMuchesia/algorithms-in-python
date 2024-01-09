str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"


def iterate_uppercase(word:str):
    for w in word:
        if w.isupper():
            return w
        
        
def recursive_uppercase(word:str, index=0):
    
    if index == len(word)-1:
        return False
    
    if word[index].isupper():
        return word[index]
    else:
        return recursive_uppercase(word,index+1) 


print(iterate_uppercase(str_1))
print(recursive_uppercase(str_1))