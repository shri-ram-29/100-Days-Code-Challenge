class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate("", n, n, result)
        return result

    def generate(self, curr, open_count, close_count, result):
        if open_count == 0 and close_count == 0:
            result.append(curr)
            return
        
        if open_count > 0:
            self.generate(curr + "(", open_count - 1, close_count, result)

        if close_count > open_count:
            self.generate(curr + ")", open_count, close_count - 1, result)