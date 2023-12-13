def buy_and_sell_stock(arr):
    diff = 0
    
    prev = arr[0] 
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            prev = arr[i]
        if arr[i] != prev:
            new_diff = arr[i]-prev
            print(new_diff)
        if new_diff > diff:
            diff = new_diff
        
    max_price = 0
    min_price = arr[0]  
    for i in range(1,len(arr)):
        min_price = min(min_price, arr[i])
        
        max_price = max(max_price, arr[i]-min_price)
    return max_price
            

print(buy_and_sell_stock([310,315,275,295,260,270,290,230,255,250]))




            