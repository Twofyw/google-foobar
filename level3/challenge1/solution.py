from collections import deque

class Maze:
    def __init__(self, map):
        self.map = map
        self.dist = {(0, 0): 1}  # [no_punch_dist, punch_dist]
        self.w, self.h = len(map), len(map[0])

    def shortest_length(self):
        """

        :return: The length of the shortest path from the prison door (0,0) to the escape pod (w-1,h-1).
        """
        # black_nodes = []  # m[coord] =
        grey_nodes = deque([(0, 0)])  # i, j, look_for_punch
        # while grey_nodes:
        while True:
            v = i, j = grey_nodes.popleft()
            d = self.dist[v]
            self.map[i][j] = 1  # Don't add itself to neighbors
            for neighbor in self.neighbors(*v):
                print neighbor, d + 1
                grey_nodes.append(neighbor)
                self.dist[neighbor] = d + 1
                if neighbor == (self.w-1, self.h-1):
                    return d + 1

    def neighbors(self, i, j):
        """
        Candidates must follow the following rules:
            1. Space candidates at (i, j) mush either be not explored or gives access to path of shorter distance
            2. A wall should be punched only if the neighbors of the wall leads to a space not explored or gives access to a shorter path
        :param i:
        :param j:
        :return:
        """
        for (candidate_i, candidate_j), (opposite_i, opposite_j) in (
                ((i-1, j), (i-2, j)),
                ((i+1, j), (i+2, j)),
                ((i, j-1), (i, j-2)),
                ((i, j+1), (i, j+2))):
            if 0 <= candidate_i < self.w and 0 <= candidate_j < self.h:
                if self.dist[(opposite_i, opposite_j)]
                if self.dist[(candidate_i, candidate_j)] > self.dist[(i, j)] + 1:
                if self.map[candidate_i][candidate_j] != 1:
                    yield candidate_i, candidate_j,


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
