# using Recursion
# time complexity = O(2^n)
# space complexity = O(n) for recursion stack

def wordBreakRec(start,s,dictionary):
    if start == len(s):
        return 1
    
    n = len(s)
    prefix = ""
    for j in range(start,n):
        prefix += s[j]
        if prefix in dictionary and wordBreakRec(j+1,s,dictionary) == 1:
            return 1 
    return 0

def wordBreak(s,dictionary):
    return wordBreakRec(0,s,dictionary)

import datetime
s = "ilike"
dictionary = ["i","like","gft"]
start = datetime.datetime.now()
print("true" if wordBreak(s,dictionary) else "false")
end = datetime.datetime.now()
print(end-start)

# using dinamic programming (top down approach)
# time complexity = O(n^2)
# space complexity = O(n+m)

def wordBreakRec(ind,s,dictionary,dp):
    if ind>=len(s):
        return True
    if dp[ind] != -1:
        return dp[ind] == 1
    possible = False
    for temp in dictionary:
        if len(temp)>len(s)-ind:
            continue
        if s[ind:ind+len(temp)] == temp:
           possible |= wordBreakRec(ind+len(temp),s,dictionary,dp)
    dp[ind] = 1 if possible else 0
    return possible

def wordBreak(s,dictionary):
    n = len(s)
    dp = [-1] * (n+1)
    return wordBreakRec(0,s,dictionary,dp)

import datetime
s = "catsandog"
dictionary = ["cats","dog","sand","and","cat"]
start = datetime.datetime.now()
print("true" if wordBreak(s,dictionary) else "false")
end = datetime.datetime.now()
print(end-start)

# using dynamic programming (bottom up approach)
# time complexity = O(n*m*k)
# space complexity = O(n)
def wordBreak(s,dictionary):
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(1,n+1):
        for w in dictionary:
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:start+len(w)] == w:
                dp[i] = True
                break
    return dp[n]

s = "ilike"
dictionary = ["i","like","gft"]
start = datetime.datetime.now()
print("true" if wordBreak(s,dictionary) else "false")
end = datetime.datetime.now()
print(end-start)