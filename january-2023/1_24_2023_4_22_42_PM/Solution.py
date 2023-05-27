# https://leetcode.com/problems/snakes-and-ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        N = n*n
        vis = set([1])

        def label_to_coord(l):
            r = n - math.ceil(l/n)
            c = (l%n - 1) % n if math.ceil(l/n)%2 else (n-l%n)%n
            return (r,c)

        q = deque([(1,0)])

        while q:
            label, step = q.popleft()
            for v in range(label+1, label+7):
                if v not in vis:
                    vis.add(v)
                    r, c = label_to_coord(v)
                    x = v if board[r][c] == -1 else board[r][c]
                    if x == N:
                      return step + 1
                    q.append((x, step + 1))

        return -1





