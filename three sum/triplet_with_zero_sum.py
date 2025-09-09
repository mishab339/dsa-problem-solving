# time complexity = O(n^3)
# space complexity = O(1)
def findTriplet(arr):
    n = len(arr)
    res = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    res.append((arr[i], arr[j], arr[k]))
    return res

# Example usage:
arr = [-1,0,1,2,-1,-4]
print(findTriplet(arr))  # Output: [(0, -1, 1),

# using hashSet    
# time complexity = O(n^3)
# space complexity = O(n)
def findTriplet(arr):
    map = {}
    ans = []
    n = len(arr)
    for j in range(n):
        for k in range(j+1,n):
            val = -(arr[j]+arr[k])

            if val in map:
                ans.append([val,arr[j],arr[k]])
            
        if arr[j] not in map:
            map[arr[j]] = []
            map[arr[j]].append(j)
    
    return ans

arr = [-1,0,1,2,-1,-4]
print(findTriplet(arr))


# using two pointer method
# timecomplexity = O(n^2)
# space complexity = O(1)
def findTriplet(arr):
    arr.sort()
    n = len(arr)
    res = []

    for i, a in enumerate(arr):
        if i > 0 and a == arr[i-1]:
            continue
        l,r = i + 1,n - 1

        while l < r:
            threeSum = a + arr[l] + arr[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a,arr[l],arr[r]])
                l += 1
                while arr[l] == arr[l-1] and l < r:
                    l += 1
    
    return res

arr = [-1,0,1,2,-1,-4]
print(findTriplet(arr))
