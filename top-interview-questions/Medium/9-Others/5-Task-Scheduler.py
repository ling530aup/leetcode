from typing import List
from collections import Counter


def leastInterval(tasks: List[str], n: int) -> int:
    count = sorted(Counter(tasks).items(), key=lambda x: x[1])
    last_line_count = 0
    most_n = count[-1][1]
    for item in count:
        if most_n == item[1]:
            last_line_count += 1

    return max((most_n - 1) * (n + 1) + last_line_count, len(tasks))


if __name__ == '__main__':
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2) == 12
