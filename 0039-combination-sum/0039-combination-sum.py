
class Solution:
    def combinationSum(self, candidates, target):

        result = []
        current = []

        def backtrack(start, total):

            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                current.append(candidates[i])

                # Same index is allowed because reuse is unlimited
                backtrack(i, total + candidates[i])

                # Backtrack: remove the last number
                current.pop()

        backtrack(0, 0)

        return result   