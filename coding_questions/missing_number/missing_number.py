array = [9,6,4,2,3,5,7,0,1]
#array = [3,4,-1,1]

def swap(a, b, array):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp
    
def firstMissingPositive(nums) -> int:
    for idx, i in enumerate(nums):
        if idx == 0:
            continue

        step = idx

        while step > 0:
            #print(f'comparing {nums[idx]} and {nums[idx - step]}')
            if nums[idx] < nums[idx - step]:
                swap(idx - step, idx, nums)
            step -= 1

    #print(f'sorted array: {nums}')

    for idx, i in enumerate(nums):
        # remove negative numbers (also remove zero)
        if i <= 0:
            nums.pop(idx)
            
        if len(nums) == 0 or nums[0] != 1:
            return 1

        # If there are no gaps, increment and return the next integer 
        if idx+1 == len(nums):
            return nums[idx] + 1
        
        if nums[idx+1] == (nums[idx] + 1):
            # ok, natural progression
            continue
        else:
            # only positives
            if nums[idx] + 1 <= 0:
                continue
            # here is the missing one
            return (nums[idx] + 1)

print(firstMissingPositive(array))
