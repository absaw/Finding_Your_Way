from maze import *

def way():

    maze=generate_maze()
    prob_maze=maze.copy()
    print(prob_maze)
    right=[0, 1]
    left=[0, -1]
    down=[1, 0]
    up=[-1, 0]
def initialize_prob(prob_maze):
    #initialize_prob
    n_zeros=prob_maze.size-np.count_nonzero(prob_maze)
    print(n_zeros)
    for row in range(prob_maze.shape[0]):
        for col in range(prob_maze.shape[1]):
            if prob_maze[row][col]==0:
                prob_maze[row][col]=1/n_zeros
    return prob_maze
way()


