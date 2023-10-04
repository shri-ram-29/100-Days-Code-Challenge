class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s_count = [0]*10
        g_count = [0]*10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s_count[int(secret[i])] += 1
                g_count[int(secret[i])] += 1
        
        for i in range(10):
            cows += min(s_count[i], g_count[i])

        return f"{bulls}A{cows}B"