class Solution(object):
    def maxProfit(self, prices):
        buy, prof = float('inf'), 0
        for i in prices:
            buy, prof = min(i, buy), max(prof, i-buy)
        return prof