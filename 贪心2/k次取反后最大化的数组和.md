# k次取反后最大化的数组和

力扣1005

##初步思路

这题说是，给一个k，执行以下操作k次


这个思路的话，首先就是找到绝对值最大的负数，然后把它反转回来

如果没有负数（或者反转回来后还剩下）的一些“不得不”的操作，

思考一下，如果是偶数，那么无所谓

所以转化为，“不得不”的操作其实就只有1次

那么就选那个最小的正数就行


## python技巧

```python 


nums = [2, -5, 1, -4, 3]

# 按照绝对值从小到大排序
nums.sort(key=abs)
print(nums)  # 输出: [1, 2, 3, -4, -5]

# 按照绝对值从大到小排序（贪心算法里极其常用！）
nums.sort(key=abs, reverse=True)
print(nums)  # 输出: [-5, -4, 3, 2, 1]

nums = [2, -5, 1, -4, 3]

# 按照绝对值从大到小排序
new_nums = sorted(nums, key=abs, reverse=True)

print(new_nums) # 输出: [-5, -4, 3, 2, 1]
print(nums)     # 输出: [2, -5, 1, -4, 3] （原数组没变）

```

## 答案

```python 
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        new_nums = sorted(nums,key = abs,reverse = True)#先按照绝对值排序
        i = 0
        while k > 0 and i < len(new_nums):#把所有的负斩杀掉
            if new_nums[i] < 0:
                new_nums[i] *= -1
                k -= 1
            i += 1
        if k %2 !=0:#如果最后k还没用完，并且是一个奇数，就舍弃掉最小的，即数组最后一个（绝u地址最小）
            new_nums[-1] *= -1
        return sum(new_nums)
```
