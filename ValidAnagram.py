# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# my first solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = {}
        hashmap2 = {}
        for i,j in zip(s,t):
            if i in hashmap1:
                hashmap1[i] += 1
            else:
                hashmap1[i] = 1
            if j in hashmap2:
                hashmap2[j] += 1
            else:
                hashmap2[j] = 1
        for l in hashmap1.keys():
            if not l in hashmap2:
                return False
            if hashmap1[l] != hashmap2[l]:
                return False
        return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         count = [0]*26

#         for x in s:
#             count[ord(x) - ord('a')] += 1

#         for x in t:
#             count[ord(x) - ord('a')] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sorted_s = sorted(s)
#         sorted_t = sorted(t)
#         return sorted_s == sorted_t
