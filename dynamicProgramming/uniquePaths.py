"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

"""

class Solution(object):
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.helper(0, 0, m, n, {})
    
    def helper(self, i, j, m, n, cache):
        if (i,j) in cache:
            return cache[(i,j)]

        # If we have reached the bottom, there is only 1 path
        if i == m-1:
            return 1

        # If we have reached the right side, there is only 1 path
        if j == n-1:
            return 1

        num_paths = 0
        
        num_paths += (self.helper(i+1, j, m, n, cache)) + (self.helper(i, j+1, m, n, cache))
        
        cache[(i,j)] = num_paths

        return num_paths



if __name__ == '__main__':
    solution = Solution()

    print(solution.unique_paths(100,100)) #should be 22750883079422934966181954039568885395604168260154104734000