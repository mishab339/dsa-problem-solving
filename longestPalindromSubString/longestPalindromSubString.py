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

# Manacher's algoritham
# time complexity = O(n)
# space complexity = O(n)



def longestPalindrome(s):
    s_prime = "#" + "#".join(s) + "#"
    radii = [0 for _ in range(len(s_prime))] # length of the palindrome from center ot one end
    center = 0
    right_border = 0
    max_radius = 0
    largest_palindrome_center = 0
    for i in range(len(s_prime)):
        mirror = center - (i - center)
        #if the current letter with in the palindrome
        if i < right_border:
            
            #if the mirror palindrome does not extend beyond the border of the palindrome centered at 'center'
            if radii[mirror] < right_border - i:
                radii[i] = radii[mirror]
                continue
            #if the mirror palindrome extends beyond or up to the border of the palindrome centered at 'center'
            #   then we know that the radius of the palindrome centered at 's_prime[i]' is >= right_border - i
            else: 
                radii[i] = right_border - i
            
        # now we need to explore beyond the minimum guaranteed length
        # if 's_prime[i]' is not within a larger palindrome, then 'radii[i]' would be 0 and we'd be exploring from scratch
        while i - 1 - radii[i] >= 0 \
            and i + 1 + radii[i] < len(s_prime) \
            and s_prime[i - 1 - radii[i]] == s_prime[i + 1 + radii[i]]:
                radii[i] += 1
        
        #if the palindrome centered at "i" extended beyond the palindrome centered at 'center'
        if i + radii[i] > right_border:
            #reset center and right_border to 'i' and 'i + radii[i]' because the current palindrome is the
            # palindrome that reaches the furthest to the right
            center = i
            right_border = i + radii[i]
        if radii[i] > max_radius:
            max_radius = radii[i]
            largest_palindrome_center = i
    start_index = (largest_palindrome_center - max_radius) // 2
    return s[start_index : start_index + max_radius]


start = datetime.datetime.now()
print("Mancher's algorithm")
print(longestPalindrome("forgeeksskeegfor"))
end = datetime.datetime.now()
print(end-start)



