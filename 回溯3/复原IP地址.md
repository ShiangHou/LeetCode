# 复原IP地址
力扣93

## 初步思路

题目要求说是先给数字，给完数字之后，按照IP地址进行切割，并且返回所有符合要求的切割方式

IP的要求是，每个分割后的数必须是0-255之间，并且以0开头（如果是0只能单独一个0）

初步的想法是说我按照点来去做，即写一个递归，跟分割回文串差不多

f(s,start,path) start是切割点的坐标，s是字符串本身，path是存入的路径

如果i过界了，直接返回

然后i从0开始往后，for循环从start到len，不对，由于这里最长只能是255，所以最多只能往后3个，即start+4

切下来的如果是合法的，那么就保存一下，继续，从i+1位置去切（递归），如果不合法，就继续就行
```python 
cclass Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.f(0,s,[])
        return self.ans

    def f(self,start,s,path):
        # if (start > (len(s)-1) and len(path) < 4) or (start < (len(s)-1 )and len(path)>=4) :#没到终点超过4块或者到了中点少于四块
        #     return 
        if len(path) == 4:#如果切出来了四个
            if start == len(s):#并且还正好走到了头（覆盖全
                self.ans.append(".".join(path.copy()))
            return
        for i in range(start,start+4):#每一层最多只能切3个
            #判断是不是合法的
            if self.isVaild(s[start:i+1]):#是合法的，就切一刀，存一下，然后递归
                path.append(s[start:i+1])
                self.f(i+1,s,path)
                path.pop()
            else:
                continue
    def isVaild(self,s:str):
        if not s:
            return False
        if int(s)>255:
            return False

        if s[0] == "0" and len(s) >1:
            return False
        return True
```
这里可以不把0这个放到循环里面写，可以放在isvaild里面