qwen vl 处理的pipeline

手写mlp

给一个字符，这个字符🈯只有012？这四种字符组成

？可以换成012其中任何一个

问把问好替换后，有多少种可能

整个字符不得出现连续相同的字符




示例 输入 input = 00?1?  output = 0


输入 012 输出 1

输入 0？？1？ 输出 6

问一共有多少种可能




# 思路

首先就是遍历一遍字符串，如果出现连续两个数字一样的，就return 0就行



```python 
s = '0??1?'
ans = []

s_list = [i for i in s]

choice = ['0','1','2']
def f(s_list,i):#主递归
    if i == len(s):#到末尾了，搜集一种可能性
        if f2("".join(s_list)):
            ans.append("".join(s_list))
        return 
    if s_list[i] == '?':#如果遇到了问号
        for j in choice:#遍历所有的可能
            if j != s_list[i-1]:
                s_list[i] = j#替换掉一个
                f(s_list,i+1)
                s_list[i] = "?"
            else:
                continue     
    else:
        f(s_list,i+1)


def f2(s):#判断一个字符串是不是合法的
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

f(s_list,0)
print(ans)
```

