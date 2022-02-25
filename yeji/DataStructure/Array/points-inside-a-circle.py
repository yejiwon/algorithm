class Solution:
    def _isInCircle(self, x, y, r):
        return x*x + y*y <= r*r 
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        for query in queries:
            count = 0
            for point in points:
                x = point[0] - query[0]
                y = point[1] - query[1]
                r = query[2]
                
                if self._isInCircle(x, y, r):
                    count += 1
            answer.append(count)
        
        return answer