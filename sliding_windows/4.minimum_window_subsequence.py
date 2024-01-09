def min_window(str1, str2):
    
    p = q = 0
    
    while q < len(str2) and p < len(str1):
        
        if str2[q] == str1[p]:
            q+=1
        
        p+=1
    
   
    
   
    return ""


min_window("abcdebdde", "bde")