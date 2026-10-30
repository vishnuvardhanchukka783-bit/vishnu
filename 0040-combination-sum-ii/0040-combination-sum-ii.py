
class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        result = []
        current = []

        def backtrack(start, total):

            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate candidates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                # i + 1 means each number is used only once
                backtrack(i + 1, total + candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, 0)

        return result