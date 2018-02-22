def two_sum(nums, target):
    print(nums,target)
    res = []
    for i,iv in enumerate(nums) :
        for j,jv in enumerate(nums[i+1:]):
            if(iv+jv == target):
                res.append(i)
                res.append(j+1)
                break
    return res

def two_sum_2(nums,target):
    print(nums," ",target)
    res = {} 
    for i,iv in enumerate(nums):
        diff = target - iv
        if diff in res:
            return [res[diff],i]
        else:
            res[iv]=i
    return res


nums=[2,7,11,15]
target = 9 
res = two_sum_2(nums,target)
print(res)
