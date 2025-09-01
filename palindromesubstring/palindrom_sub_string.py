# Time complexity = O(n^3)
# spase complexity = O(1)

def isPalindrome(s, i, j):
    while i<j:
        if s[i] != s[j]:
            return False
        j-=1
        i+=1
    return True

def countPS(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1,n):
            if isPalindrome(s,i,j):
                count+=1
    return count
s = "abaab"
import datetime
start = datetime.datetime.now()
print(countPS(s))
end = datetime.datetime.now()
print(end-start)

# using dynamic programming 
# time complexity = O(n^2)
# space complexity = O(n^2)

def isPalindrome(s,i,j,memo):
    if i==j:
        return 1
    if j == i+1 and s[i]==s[j]:
        return 1
    if memo[i][j]!=-1:
        return memo[i][j]
    
    if s[i]==s[j] and isPalindrome(s,i+1,j-1,memo)==1:
        memo[i][j]=1
    else:
        memo[i][j] = 0
    
    return memo[i][j]

def countPS(s):
    n = len(s)
    memo = [[-1 for i in range(n)] for i in range(n)]

    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if isPalindrome(s,i,j,memo)==1:
                res+=1
    return res

start = datetime.datetime.now()
print(countPS("abaab"))
end = datetime.datetime.now()
print(end-start)