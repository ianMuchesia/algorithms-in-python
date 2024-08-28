null_array = [ 1,5,None, 7,2,9,None, 4]
persistence = []
result = []

for i in range(len(null_array)):
    if null_array[i] is not None:
        persistence.append(null_array[i])
    else:
        if len(persistence):
            result.append(persistence)
        persistence = []
        continue
       
   
if len(persistence):
    result.append(persistence)     
        
print(result)
        
        
    