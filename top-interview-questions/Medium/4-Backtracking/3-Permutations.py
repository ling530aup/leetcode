from copy import copy

def dfs(nums, used, path, rst_set):
    if len(used) == len(nums):
        rst_set.append(copy(path))
    for num in nums:
        if num not in used:
            path.append(num)
            used.add(num)
            dfs(nums, used, path, rst_set)
            used.remove(num)
            path.pop()
            
if __name__ == '__main__':
    rst_set = []
    dfs([1,2,3], set(), [], rst_set)
    print(rst_set)
