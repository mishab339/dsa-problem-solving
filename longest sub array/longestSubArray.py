def longestSubString(s):
    charArray = set()
    l=0
    res = 0
    for i in range(len(s)):
        while s[i] in charArray:
            charArray.remove(s[l])
            l+=1
        charArray.add(s[i])
        res = max(res,i-l+1)
    return res

print(longestSubString("abcabcabc"))