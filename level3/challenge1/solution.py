from collections import deque

class Maze:
    inf = float('inf')

    def __init__(self, map):
        self.map = map
        self.w, self.h = len(map), len(map[0])

    def shortest_path(self, sx, sy):
        dist = [[None for _ in range(self.h)] for _ in range(self.w)]
        dist[sx][sy] = 1

        grey_nodes = deque([(sx, sy)])
        while grey_nodes:
            x, y = grey_nodes.popleft()
            for nx, ny in self.neighbors(x, y):
                if dist[nx][ny] is None:
                    dist[nx][ny] = dist[x][y] + 1
                    if self.map[nx][ny] == 0:
                        grey_nodes.append((nx, ny))
        return dist

    def neighbors(self, i, j):
        for candidate_i, candidate_j in ((i-1, j),
                                         (i+1, j),
                                         (i, j-1),
                                         (i, j+1)):
            if 0 <= candidate_i < self.w and 0 <= candidate_j < self.h:
                yield candidate_i, candidate_j

    def shortest_length(self):
        tb = self.shortest_path(0, 0)
        bt = self.shortest_path(self.w - 1, self.h - 1)

        result = self.inf
        for i in range(self.w):
            for j in range(self.h):
                if tb[i][j] and bt[i][j]:
                    result = min(tb[i][j] + bt[i][j] - 1, result)
        return result


#
#     def shortest_length(self):
#         """
#
#         :return: The length of the shortest path from the prison door (0,0) to the escape pod (w-1,h-1).
#         """
#         # black_nodes = []  # m[coord] =
#         grey_nodes = deque([(self.w-1, self.h-1)])  # i, j, look_for_punch
#         # while grey_nodes:
#         while grey_nodes:
#             v = i, j = grey_nodes.popleft()
#             d = self.dist[v]
#             for neighbor in self.neighbors(i, j):
#                 if self.map[neighbor[0]][neighbor[1]]:  # is wall
#                     if self.is_punchable(neighbor):
#                         self.punchable_walls.append(neighbor)
#                 else:
#                     if self.dist.get(neighbor, self.inf) > d + 1:
#                         grey_nodes.append(neighbor)
#                         self.dist[neighbor] = d + 1
#         return self.dist[(0,0)] - max(self.wall_diff(v) for v in self.punchable_walls)
#
#     def wall_diff(self, v):
#         dist = [self.dist[v] for v in self.neighbors(*v) if self.dist.get(v) is not None]
#         if not dist:
#             return 0
#         return max(dist) - min(dist) - 2
#
#     def is_punchable(self, v):
#         # at least one of the neighbors hasn't been reached and at least two of the neighbors aren't wall
#         neighbors = list(self.neighbors(*v))
#         not_reached = [n for n in neighbors if n not in self.dist]
#         not_wall = [n for n in neighbors if not self.map[n[0]][n[1]]]
#         return len(not_reached) >= 1 and len(not_wall) >= 2
#
#     def neighbors(self, i, j):
#         """
#         Candidates must follow the following rules:
#             1. Space candidates at (i, j) mush either be not explored or gives access to path of shorter distance
#             2. A wall should be punched only if the neighbors of the wall leads to a space not explored or gives access to a shorter path
#         :param i:
#         :param j:
#         :param dist: Shortest distance from (0, 0) to (i, j)
#         :return:
#         """
#         for candidate_i, candidate_j in ((i-1, j),
#                                          (i+1, j),
#                                          (i, j-1),
#                                          (i, j+1)):
#             if 0 <= candidate_i < self.w and 0 <= candidate_j < self.h:
#                 yield candidate_i, candidate_j

                # if self.map[candidate_i][candidate_j]:
                #     self.walls.append()
                #
                # else:
                #     if self.dist[(candidate_i, candidate_j)] > dist + 1:
                #         yield candidate_i, candidate_j,


def solution(map):
    """
        A modification of the Dijkstra algorithm

    :param map: The map represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls.
    :return: The length of the shortest path from the prison door (0,0) to the escape pod (w-1,h-1).
    """
    # length[i][j] = the length of the shortest path from (i,j) to (w-1,h-1).
    # Modify the current location to -1 and continue searching from adjacent spaces.
    return Maze(map).shortest_length()


if __name__ == '__main__':
    print "test_case\t", "solution(test_case)"
    test_cases = [
        [[0, 0],
         [1, 0]],  # 3
        [[0, 0, 0, 0],
         [0, 0, 0, 1],
         [1, 1, 0, 0],
         [1, 1, 1, 0]],  # 7
        [[0, 1, 1, 0],
         [0, 0, 0, 1],
         [1, 1, 0, 0],
         [1, 1, 1, 0]],  # 7
        [[0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0]],  # 11
        ]
    for test_case in test_cases:
        result = solution(test_case)
        print test_case, "\t\t", result
