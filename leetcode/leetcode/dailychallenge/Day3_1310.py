#https://leetcode.com/problems/xor-queries-of-a-subarray/?envType=daily-question&envId=2024-09-13
#Time Limite Exceeded (41/46)

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in queries:
            x = i[0]
            y = i[1]
            sol = arr[x]
            # print(f"init = {sol}")
            for target in range(x, y):
                    # print(f"target+1 = {target+1}")
                    # print(f"arr[target+1] = {arr[target+1]}")
                    sol = sol ^ arr[target+1]
                    # print(f"sol = {sol}")
            ans.append(sol)
        return ans
