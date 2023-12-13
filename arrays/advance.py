def advance_game(arr):
    furthest_reached = 0
    last_index = len(arr)-1
    i=0
    while i<= furthest_reached and furthest_reached<last_index:
       furthest_reached = max(furthest_reached,arr[i] + i)
       i+=1
    return furthest_reached>=last_index 