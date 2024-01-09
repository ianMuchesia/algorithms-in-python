

def find_repeated_sequences(s, k):
    start = 0
    
    end = k
    
    hashMap = {}
    
    output = []
    
    while end <= len(s)-1:
        if s[start:end] not in hashMap:
            hashMap[s[start:end]] = 1
        
        else:
            output.append(s[start:end])
            
        start+=1
        end+=1
            
        
    return output










input_str = "AAAAACCCCCAAAAACCCCCC"
print(find_repeated_sequences(input_str, 8))