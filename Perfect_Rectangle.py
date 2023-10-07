class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        total_area = 0
        
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            total_area += (x2 - x1) * (y2 - y1)
            corners ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}
        if not rectangles or not corners:
            return False
        min_x = min(corners, key=lambda x: x[0])[0]
        min_y = min(corners, key=lambda x: x[1])[1]
        max_x = max(corners, key=lambda x: x[0])[0]
        max_y = max(corners, key=lambda x: x[1])[1]
        
        bounding_area = (max_x - min_x) * (max_y - min_y)
        return total_area == bounding_area and corners == {(min_x, min_y), (max_x, max_y), (min_x, max_y), (max_x, min_y)}
