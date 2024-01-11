def reverse_string_3(sentence:str)->str:
    pass

    start = 0
  
    
    s_arr = sentence.split(" ")
    end = len(s_arr)-1
    while start < end:
        print(s_arr)
        s_arr[start] , s_arr[end] = s_arr[end] ,s_arr[start]
        start += 1
        end -=1
        
    
  
    start =end=0
    
    for s in s_arr:
        result = s.split(' ')
        end = len(result)-1
        while (start < end):
            result[start],result[end] = result[end], result[start]
            start += 1
            end -=1
        start = 0
        s = "".join(result)
        print(s)
    
    print(s_arr)
    
            
        
  
    

reverse_string_3("The quick brown fox jumped over a lazy dog")