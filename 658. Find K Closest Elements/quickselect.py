class Solution:
    def kClosest(self, points, K):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 616 ms, faster than 73.25% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 18.3 MB, less than 96.81% of Python online submissions for K Closest Points to Origin.
        :param points:
        :param K:
        :return:
        """
        self.sort(points, 0, len(points) - 1, K)
        return points[:K]

    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p + 1, r, K)
            else:
                self.sort(points, l, p - 1, K)

    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        return a