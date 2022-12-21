class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for i in accounts:
            currentwealth = 0
            for j in i:
                currentwealth += j
            maxwealth = max(maxwealth,currentwealth)
        return maxwealth
