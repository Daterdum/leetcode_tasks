def isBadVersion(version: int) -> bool:
    if version > 10:
        return True


class Solution:
    def firstBadVersion(self, n: int, start=0) -> int:
        if n - start == 1:
            return n
        mid = int((n + start) / 2)

        if isBadVersion(mid):
            return self.firstBadVersion(n=mid, start=start)

        else:
            return self.firstBadVersion(n=n, start=(mid))