class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_positions = {}
        min_pickup = float('inf')
        
        for i, card in enumerate(cards):
            if card in card_positions:
                pickup = i - card_positions[card] + 1
                min_pickup = min(min_pickup, pickup)
            card_positions[card] = i
        return min_pickup if min_pickup != float('inf') else -1
