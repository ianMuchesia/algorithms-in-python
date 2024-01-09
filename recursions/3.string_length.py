input_str = "LucidProgramming"



def string_length(words:str):
    count = 0
    for w in words:
        count += 1
        
    return count


def recursive_string_length(words:str,count=0):
   
    if words == "":
        return count
    else:
        return recursive_string_length(words[1:],count + 1)
    

def recursive_string_lenght_option_2(words:str):
    if words == "":
        return 0
    else:
        return 1 + recursive_string_lenght_option_2(words[1:])

print(string_length(input_str))
print(recursive_string_length(input_str))
print(recursive_string_lenght_option_2(input_str))
    
    