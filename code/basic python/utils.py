def find_max(nums):
    largest=nums[0]

    for i in nums:
        if i>largest:
            largest=i
    return(largest)
