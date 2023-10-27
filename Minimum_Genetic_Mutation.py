from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def is_valid_mutation(gene1, gene2):
            # Check if two genes differ by exactly one character
            diff_count = sum(g1 != g2 for g1, g2 in zip(gene1, gene2))
            return diff_count == 1

        if endGene not in bank:
            return -1

        bank = set(bank)
        queue = deque([(startGene, 0)])

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for neighbor in bank.copy():
                if is_valid_mutation(gene, neighbor):
                    queue.append((neighbor, mutations + 1))
                    bank.remove(neighbor)

        return -1
