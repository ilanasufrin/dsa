"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.

"""

class Solution(object):
    def unique_paths(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        return self.helper(0,0,obstacleGrid,{})
    
    def helper(self, i, j, obstacleGrid, cache):
        if (i,j) in cache:
            return cache[(i,j)]
        
        # Boundary checking
        if i == len(obstacleGrid):
            return 0

        # Boundary checking
        if j == len(obstacleGrid[0]):
            return 0
        
        # We are at an obstacle
        if obstacleGrid[i][j] == 1:
            return 0

        # Finally we've reached the finish
        if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
            return 1
    
        num_paths = self.helper(i+1, j, obstacleGrid, cache) + self.helper(i, j+1, obstacleGrid, cache)
        
        cache[(i,j)] = num_paths

        return num_paths


if __name__ == '__main__':
    grid = [[0,0,0], [0,1,0], [0,0,0]]
    solution = Solution()

    print(solution.unique_paths(grid)) #should be 2