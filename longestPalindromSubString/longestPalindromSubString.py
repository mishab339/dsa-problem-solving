# Time complexity = O(n^3)
# space complexity = O(1)

def checkPal(s,low,high):
    while low<high:
        if s[low] != s[high]:
            return False
        low+=1
        high-=1
    return True
def longestPalindromeSubString(s):
    maxLength = 1
    start = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if checkPal(s,i,j) and (j-i+1) > maxLength:
                start = i
                maxLength = j-i+1
    return s[start:start+maxLength]

import datetime

start = datetime.datetime.now()
print(longestPalindromeSubString("forgeeksskeegfor"))
end = datetime.datetime.now()

print(end-start)


# Time complaxity = O(n^2)
# space complaxity = O(n^2)

# using Dynamic programming

def getLongestPal(s):
    n = len(s)
    maxLength = 1
    start = 0
    dp = [[False]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            if maxLength == 1:
                start = i
                maxLength = 2
    
    for length in range(3,n+1):
        for i in range(n-length+1):
            j = i + length - 1

            if s[i] == s[j] and dp[i+1][j-1] == True:
                dp[i][j] = True
                if length>maxLength:
                    start = i
                    maxLength = length
    return s[start:start+maxLength]

start = datetime.datetime.now()
print(getLongestPal("forgeeksskeegfor"))
end = datetime.datetime.now()
print(end - start)
        
# time complexity = O(n^2)
# space complexity = O(1)

def getLongestPal2(s):

    n = len(s)
    maxLength = 1
    start = 0
    for i in range(n):
        for j in range(2):
            low , high = i, i+j

            while low >= 0 and high < n and s[low] == s[high]:
                currentLength = high - low + 1
                if currentLength > maxLength:
                    maxLength = currentLength
                    start = low
                low -= 1
                high += 1
    return s[start:start+maxLength]

start = datetime.datetime.now()
print(getLongestPal2("forgeeksskeegfor"))
end = datetime.datetime.now()
print(end-start)


