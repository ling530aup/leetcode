from typing import List
from collections import Counter


def majorityElement(nums: List[int]) -> int:
    count = Counter(nums)
    for key in count:
        if count[key] > len(nums)/2:
            return key
    print(count)
    return None


if __name__ == '__main__':
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majorityElement([3, 2, 3]) == 3
