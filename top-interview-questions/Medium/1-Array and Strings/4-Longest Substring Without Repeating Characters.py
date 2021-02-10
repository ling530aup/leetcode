#Longest Substring Without Repeating Characters
'''


思路： 通向双指正解决

i = 0, j = 1  满足不重复条件

子串， 移动j 判断新增加字符是否造成重复。
如果有， 移动i， 如果没有，移动j 并且尝试更新已知最大长度
'''