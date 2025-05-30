from typing import List


class Solution:
    def __init__(self):
        self.edges = []

    def dfs(self, dist: List[int], node: int, d: int) -> List[int]:
        """Recursive DFS to fill array of distances from node"""
        # no edge out of node
        if node == -1:
            return dist

        # edge has not been visited
        if dist[node] == -1:
            dist[node] = d  # fill distance
            return self.dfs(dist, self.edges[node], d + 1)  # recursive call
        else:
            return dist  # edge has been visited (cycle)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.edges = edges  # set edges for use in dfs
        dist1 = [-1] * len(edges)  # initialize empty distance arrays
        dist2 = [-1] * len(edges)

        dist1 = self.dfs(dist1, node1, 0)  # fill distance arrays with dfs
        dist2 = self.dfs(dist2, node2, 0)

        ans = -1
        minmax = float('inf')
        # loop through distance arrays to find node with minimum max(n1, n2)
        for i, (n1, n2) in enumerate(zip(dist1, dist2)):

            if n1 == -1 or n2 == -1:  # node is unreachable
                continue

            if max(n1, n2) < minmax:
                ans = i
                minmax = max(n1, n2)

        return ans

