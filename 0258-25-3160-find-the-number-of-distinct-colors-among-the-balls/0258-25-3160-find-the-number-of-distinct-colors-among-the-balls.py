class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}  #ball to color mapping
        color_count = {}    # number of balls using each color
        unique_colors = set()  # unique colors
        res = []
        
        for ball, color in queries:
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                # Decrease count of old color
                color_count[old_color] -= 1
                # Only remove if no other ball uses this color
                if color_count[old_color] == 0:
                    unique_colors.discard(old_color)
            
            # assign the new color
            ball_to_color[ball] = color
            # Increment count of new color
            color_count[color] = color_count.get(color, 0) + 1
            unique_colors.add(color)
            
            res.append(len(unique_colors))
        
        return res