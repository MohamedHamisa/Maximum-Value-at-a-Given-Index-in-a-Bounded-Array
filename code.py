class Solution:
    def maxValue(self, n, index, maxSum):
        curr, base = n, 1
        
        left = right = index
        
        while (left > 0 or right < n - 1) and curr + (right - left + 1) <= maxSum:
            curr += (right - left + 1)
            base += 1
            left = max(0, left-1)
            right = min(n-1, right+1)
        
        return base + (maxSum - curr)//n






