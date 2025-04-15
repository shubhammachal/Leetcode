class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case 
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        #generate triangle recursively
        triangle = self.generate(numRows - 1)
        
        # current row
        current_row = [1]
        
        # previous row needed to sum the elements
        prev = triangle[-1]
        
        # Calculate middle elements using previous row
        for i in range(len(prev)-1):
            current_row.append(prev[i] + prev[i+1])
        
        # add the final 1 
        current_row.append(1)
        
        # Add the new row to the triangle and return
        triangle.append(current_row)
        return triangle