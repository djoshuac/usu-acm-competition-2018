from enum import Enum
from heapq import heappush, heappop
#https://picoledelimao.github.io/blog/2015/12/06/solving-the-sliding-puzzle/

class DIR(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class Puzzle:

    def __init__(self, size):
        self.board = []
        self.path = []
        self.dimension = size
        self.lastMove = None
        self.readInBoard()

    def readInBoard(self):
        for _ in range(self.dimension):
            self.board.append([int(x) for x in input().strip().split(" ")])

    def printBoard(self):
        print(self.board)

    def getBlankSpace(self):
        #returns y, x of the 0 pos (row, col)
        for y, row in enumerate(self.board):
            if 0 in row:
                return (y, row.index(0))

    def swap(self, first, second):
        self.board[first[0]][first[1]], self.board[second[0]][second[1]] = self.board[second[0]][second[1]], self.board[first[0]][first[1]]

    def getMove(self, piece):
        blank = self.getBlankSpace()
        line = blank[0]
        col = blank[1]
        if line > 0 and piece == self.board[line-1][col]:
            return DIR.DOWN
        elif line < self.dimension-1 and piece == self.board[line+1][col]:
            return DIR.UP
        elif col > 0 and piece == self.board == self.board[line][col-1]:
            return DIR.RIGHT
        elif col < self.dimension-1 and piece == self.board[line][col+1]:
            return DIR.LEFT
        else:
            return None

    def move(self, piece):
        m = self.getMove(piece)
        if m:
            blank = self.getBlankSpace()
            line = blank[0]
            col = blank[1]
            if m == DIR.LEFT:
                self.swap((line, col), (line, col+1))
            elif m == DIR.RIGHT:
                self.swap((line, col), (line, col-1))
            elif m == DIR.UP:
                self.swap((line, col), (line+1, col))
            elif m == DIR.DOWN:
                self.swap((line, col), (line-1, col))
            self.lastMove = piece
        return m

    def search(self):
        states = []
        self.path = []
        states.


if __name__ == "__main__":
    size = int(input())
    puzz = Puzzle(size)
    puzz.printBoard()
    print(puzz.getBlankSpace())