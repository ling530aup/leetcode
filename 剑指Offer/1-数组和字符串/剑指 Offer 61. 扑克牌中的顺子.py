class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        ls_without_0 = [num for num in nums if num != 0]
        count_0 = len([num for num in nums if num == 0])
        nmax = max(ls_without_0)
        nmin = min(ls_without_0)

        nmax = max(nmax, nmin + 4)
        nmin = min(nmin, nmax - 4)
        correct_set = set(range(nmin, nmax + 1))
        return len(correct_set - set(ls_without_0)) == count_0
