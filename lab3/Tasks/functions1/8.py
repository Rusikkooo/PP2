def spy_game(nums):
    cnt  = []
    my_list = [0,0,7]
    for i in range(len(nums)):
        if nums[i]==0:
            cnt.append(nums[i])
        if nums[i]==7:
            cnt.append(nums[i])
    
    if cnt == my_list:
        return True 
    
    return False 
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))