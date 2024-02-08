from typing import List
def two_sum(nums:List[int],target:int):
    hashmap = {}
    
    for i in range(len(nums)):
        print(hashmap, " ",nums[i])
        if nums[i] in hashmap:
            
            print(hashmap[nums[i]],nums[i])
            return True
        else:
            print(hashmap)
            hashmap[target - nums[i]] = nums[i]
    
    print(False)
    return False
    

two_sum([-2,1,2,4,7,11],9)