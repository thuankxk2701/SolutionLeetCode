# https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int, last_idx: int = 0, solution: List[int] = []) -> List[List[int]]:
        if target == 0:
            return [solution[:]]        
        if target < 0:
            return []        
        result = []        
        for idx in range(last_idx, len(candidates)):
            solution.append(candidates[idx])
            result.extend(self.combinationSum(candidates, target - candidates[idx], idx, solution))
            solution.pop()            
        return result