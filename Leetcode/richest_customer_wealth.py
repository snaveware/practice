from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richestWealth = 0

        for customer in accounts:
            wealth = 0

            for money in customer:
                wealth += money
            
            if wealth > richestWealth:
                richestWealth = wealth
        
        return richestWealth