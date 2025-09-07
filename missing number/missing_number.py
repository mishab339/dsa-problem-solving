# time complexity = O(n)
def missingNumber(nums):
    n = len(nums)
    count = [0] * (len(nums) +1)
    
    for i in nums:
        count[i] += 1
    for i in range(n+1):
        if count[i] == 0:
            return i
        
print(missingNumber([3,0,1]))  # Output: 2


# time complexity = O(n) and space complexity = O(1)
def missingNumberXOR(nums):
    n = len(nums)
    xor_sum = 0

    for i in range(n):
        xor_sum ^= nums[i]
    for i in range(n+1):
        xor_sum ^= i
    return xor_sum

print(missingNumberXOR([3,0,1]))  # Output: 2

# time complexity = O(nlogn) due to sorting
def missingNumber(nums):
    nums.sort()
    n = len(nums)
    for i in range(n):
        if nums[i] != i:
            return i
    return n

print(missingNumber([3,0,1]))  # Output: 2

# time complexity = O(n) and space complexity = O(n)
def missingNumberGauss(nums):
    n = len(nums)
    st = set()

    for i in range(n):
        st.add(nums[i])
    
    for i in range(n+1):
        if i not in st:
            return i
    return -1
print(missingNumberGauss([3,0,1]))  # Output: 2

# time complexity = O(n) and space complexity = O(1)
def missingNumber(nums):
    n = len(nums)
    sum1=0 
    sum2=0
    for i in range(n+1):
        sum1+=i
    
    for i in range(n):
        sum2+=nums[i]
    
    return sum1-sum2

print(missingNumber([3,0,1]))  # Output: 2
