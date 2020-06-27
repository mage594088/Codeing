class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        result = []
        self.helpers(n, n, '', result)
        return result
    
    def helpers(self, l, r, item, result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helpers(l-1, r, item + '(', result)
        if r > 0:
            self.helpers(l, r-1, item + ')', result)