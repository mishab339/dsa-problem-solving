#using bruit force method
# time complexity = O(n^2)
# space complexity = O(1)
def maxWater(arr):
    n = len(arr)
    max_area = 0
    for i in range(n):
        for j in range(i+1,n):
            amount = min(arr[i],arr[j])*(j-i)

            max_area = max(max_area,amount)
    return max_area
import datetime

start = datetime.datetime.now()
arr = [2, 1, 8, 6, 4, 6, 5, 5]
print(maxWater(arr))
end = datetime.datetime.now()
print("Execution time:", end - start)

# using two pointers
# time complexity = O(n)
# space complexity = O(1)
def maxWater(arr):
    left = 0
    right = len(arr)-1
    res = 0
    while left<right:
        amount = min(arr[left],arr[right])*right-left
        res = max(res,amount)

        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    
    return res

start = datetime.datetime.now()
arr = [2, 1, 8, 6, 4, 6, 5, 5]
print(maxWater(arr))
end = datetime.datetime.now()
print("Execution time:", end - start)


