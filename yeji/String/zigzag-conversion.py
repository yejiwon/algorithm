class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = dict()
        index = 0
        direction = 0
        
        down = 1
        up = -1
        
        for char in s:
            if index == 0:
                direction = down
            elif index == numRows-1:
                direction = up
           
            zigzag[index] = zigzag.get(index, '') + char
            index += direction
        
        return ''.join(zigzag.values())