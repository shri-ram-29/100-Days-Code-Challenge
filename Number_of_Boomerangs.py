class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        result = 0
        for p in points:
            distance_counts = {}
            for q in points:
                if p == q:
                    continue
                d = distance(p, q)
                distance_counts[d] = distance_counts.get(d, 0) + 1
            
            for count in distance_counts.values():
                result += count * (count - 1)
        
        return result

        