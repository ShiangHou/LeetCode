# 找出字符串中第一个匹配的下标
力扣28
## KMP算法
问题：一个字符串a，一个字符串b，a字符串包含了b字符串，需要返回a中包含字符串的开始的下标

比如abcdecd，cd，那么就需要返回2（2和5也可以，一般是最左边，kmp都支持）

不包含的话返回-1

暴力方法就是说，挨个挨个去试就行了，复杂度是O(nm)

KMP可以做到m+n，具体的思想是，我们在暴力解法的时候做了很多的无用功，当一次失败的时候，是继续i+1，从而导致重复

## 初步思路
KMP量身定制的题目 

```python 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        _next = self.get_next(needle)
        i, j = 0, 0
        n, m = len(haystack), len(needle)
        while i < n and j < m:
            if j == -1 or haystack[i] == needle[j]:
                i += 1 
                j += 1
            else:
                j = _next[j]
        return i - j if j == m else -1
            
    def get_next(self, s:str) -> list:
        if len(s) == 1:
            return [-1]
        next_nums = [0] * len(s)
        next_nums[0] = -1
        next_nums[1] = 0
        i = 2
        cn = 0
        while i < len(s):
            if s[i-1] == s[cn]:
                cn += 1              
                next_nums[i] = cn    
                i += 1
            elif cn > 0:
                cn = next_nums[cn]   
            else:
                next_nums[i] = 0
                i += 1
        return next_nums

```
