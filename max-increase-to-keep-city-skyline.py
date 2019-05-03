class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hSkyline = [0] * len(grid)
        vSkyline = [0] * len(grid[0])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                hSkyline[x] = (hSkyline[x], grid[x][y])[hSkyline[x] < grid[x][y]]
                vSkyline[y] = (vSkyline[y], grid[x][y])[vSkyline[y] < grid[x][y]]

        sum = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                lowest = (hSkyline[x], vSkyline[y])[hSkyline[x] > vSkyline[y]]
                if grid[x][y] < lowest:
                    sum += lowest - grid[x][y]
        return sum