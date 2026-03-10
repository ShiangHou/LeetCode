class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        self.f(candidates,target,0,())
        return self.ans
    def f(self,nums,target,i,path):#i是在nums下滑动的下标，path是单个搜集的路径
        if target < 0:
            return 
        if target == 0:
            self.ans.append(path.copy)
            return path
        if i >= len(nums):
            return 
        #用i,但用了就不能继续用了
        path.append(nums[i])
        self.f(nums,target-nums[i],i+1,path)

        #弹出
        path.pop()

        #不用i
        self.f(nums,target,i+1,path)

        return path