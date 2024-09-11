#https://leetcode.com/problems/minimum-bit-flips-to-convert-number/?envType=daily-question&envId=2024-09-11
#두 수가 1과 0이 다른 것만 count 하면 된다.
#XOR 연산시 1과 0이 다를때만 1이 나온다
#XOR연산 후 끝 비트부터 and 연산을 통해 1일 시에만 count를 + 해주면 된다.

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        sol = 0
        while result:
            if result & 1 == 1:
                sol = sol+1
            result >>= 1
        return sol           class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        sol = 0
        while result:
            if result & 1 == 1:
                sol = sol+1
            result >>= 1
        return sol
