
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == '*':
                    # Zero occurrences of previous character
                    dp[i][j] = dp[i][j - 2]

                    # One or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]     