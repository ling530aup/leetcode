class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        rt = [[1],[1,1]]
        if numRows < 2:
            return rt[:numRows]
        
        for i in range(2,numRows):
            ls = rt[i-1]
            new_ls = []
            for j in range(len(ls)-1):
                new_ls.append(ls[j]+ls[j+1])
            rt.append([1]+new_ls+[1])
        return rt
    
