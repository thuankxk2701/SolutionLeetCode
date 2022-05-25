# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict ={}
        for v in strs:
            if str(sorted(v)) in tmp_dict:
                tmp_dict[str(sorted(v))] += [v]
            else:
                tmp_dict[str(sorted(v))] = [v]
        return tmp_dict.values()