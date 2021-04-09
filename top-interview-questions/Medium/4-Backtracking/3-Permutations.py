def dfs(n_left, n_right_march, pre, rst_set):
    if n_left == 0 and n_right_march==0:
        rst_set.add(pre)
        return
    if n_left>0:
        dfs(n_left-1, n_right_march+1, pre+'[', rst_set)
    if n_right_march>0:
        dfs(n_left, n_right_march-1, pre+']', rst_set)


if __name__ == '__main__':
    print('------------------')
    rst_set = set()
    pre = ''
    dfs(2, 0, pre, rst_set)
    print(rst_set)
