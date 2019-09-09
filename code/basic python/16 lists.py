names = ["bangalore","mysore","managlore","hubli"]
print(names)


names[0]="Banglore"
print(names)

# Find the largest element in the list

nums = [1,23,33,4,53,6,7,8,9,10]
largest=nums[0]

for i in nums:
    if i>largest:
        largest=i

print(largest)

## List operations
nums=[1,2,5,3,5,4,5]
nums.append(10)
print(nums)
nums.pop()
print(nums)

nums.insert(0,111)
print(nums)
nums.remove(5)
print(nums)

print(nums.index(3))

print(nums.count(5))

#exercise : remove duplicates in a list

nums = [1,2,3,5,3,6,5,4]
nums2=[]
print(f"Removing dups from {nums}")
for item in nums:
    if item not in nums2:
        nums2.append(item)

print(nums2) 
