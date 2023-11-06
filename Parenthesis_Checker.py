class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,string_symbol):
        s = []
        balanced = True
        index = 0
        while index < len(string_symbol) and balanced:
            symbol = string_symbol[index]
            if symbol in "([{":
                s.append(symbol)
            else:
                if not s:
                    balanced = False
                else:
                    top = s.pop()
                    if not self.matches(top, symbol):
                        balanced = False
            index += 1
        if balanced and not s:
            return True
        else:
            return False
    
    def matches(self, open, close):
        opens = "([{"
        closes = ")]}"
        return opens.index(open) == closes.index(close)