from collections import Counter


def topKFrequent(nums, k):
    ls = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in ls[:k]]


if __name__ == "__main__":
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print(topKFrequent(nums, k))
