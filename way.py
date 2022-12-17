from maze import *

# def way():
class way
    def __init__():
        self.maze=generate_maze()
        self.n_row=maze.shape[0]
        self.n_col=maze.shape[1]
        self.prob_maze=maze.copy()
        self.prob_maze=initialize_prob(prob_maze)
        self.prob_maze_new=initialize_prob(prob_maze)
        # print(prob_maze)
        self.right=[0, 1]
        self.left=[0, -1]
        self.down=[1, 0]
        self.up=[-1, 0]

    #iterate over rows

    #down operation
    def down_step(self):
        for row in range(self.n_row):
            for col in range(self.n_col):
                prev_cell=prob_maze+self.down[0]
                print()
                # self.prob_maze_new=

    def initialize_prob(self):
        #initialize_prob
        
        n_zeros=prob_maze.size-np.count_nonzero(prob_maze)
        # print(n_zeros)
        for row in range(self.prob_maze.shape[0]):
            for col in range(self.prob_maze.shape[1]):
                if self.prob_maze[row][col]==0:
                    self.prob_maze[row][col]=1/n_zeros
                else:
                    self.prob_maze[row][col]=0
        # return self.prob_maze
# way()


