def count_consonants_string(word:str):
    vowels = "aeiou"
    
    count = 0
    for w in word:
        if w not in vowels and w != " " and w.isalpha():
            count+=1
    
    return count
            
            
            
def recursive_count_consonants(word:str,count=0,index=0):
    
    vowels = { "a", "e", "i", "o", "u"}
    if index == len(word)-1:
        return count
    
    if word[index] not in vowels and word[index] != " " and word[index].isalpha():
        return recursive_count_consonants(word,count+1, index+1)
    else:
        return recursive_count_consonants(word,count,index+1) 
    
    

def recursive_count_consonants_2(word:str,index=0):
    
    vowels = { "a", "e", "i", "o", "u"}
    if index == len(word)-1:
        return 0
    
    if word[index] not in vowels and word[index] != " " and word[index].isalpha():
        return 1 + recursive_count_consonants_2(word, index+1)
    else:
        return recursive_count_consonants_2(word,index+1) 
    
    
def recursive_count_consonants(input_str):
    vowels = { "a", "e", "i", "o", "u"}

    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])
    
    
input_str = "welcome to educative!"

print(count_consonants_string(input_str))

print(recursive_count_consonants(input_str))
    
print(recursive_count_consonants_2(input_str))