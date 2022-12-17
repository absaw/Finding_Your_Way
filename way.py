from maze import *

# def way():
class way:
    
    def __init__(self):
        self.maze=generate_maze()
        self.n_row=self.maze.shape[0]
        self.n_col=self.maze.shape[1]
        self.p_now=self.maze.copy()
        self.p_next=np.zeros(self.maze.shape)
        self.init_probabilities()
        # print(p_now)
        self.right=[0, 1]
        self.left=[0, -1]
        self.down=[1, 0]
        self.up=[-1, 0]

    #iterate over rows

    #down operation
    def down_step(self):
        for row in range(self.n_row):
            for col in range(self.n_col):

                if row==0:
                    p_in=0
                    if self.maze[row+1][col]==0:
                        p_out=self.p_now[row][col]
                    else:
                        p_out=0
                        # self.p_next[row][col]=0

                    # self.p_next[row][col]=p_in-p_out
                elif row==self.n_row-1:
                    p_out=0
                    #Deciding p_in
                    prev_row=row-1
                    if self.maze[prev_row][col]==5:
                        p_in=0
                    else:
                        p_in=self.p_now[prev_row][col]
                else:
                    # p_next[row][col]=0
                    #Deciding p_in
                    prev_row=row-1
                    if self.maze[prev_row][col]==5:
                        p_in=0
                    else:
                        p_in=self.p_now[prev_row][col]
                    #Deciding p_out
                    next_row=row+1
                    p_out=0
                    if self.maze[next_row][col]==5:
                        p_out=0
                    else:
                        p_out=self.p_now[row][col]
                self.p_next[row][col]=self.p_now[row][col]+p_in-p_out
            self.p_now=self.p_next.copy()
    def init_probabilities(self):
        #init_probabilities
        n_zeros=self.p_now.size-np.count_nonzero(self.p_now)
        # print(n_zeros)
        for row in range(self.p_now.shape[0]):
            for col in range(self.p_now.shape[1]):
                if self.p_now[row][col]==0:
                    self.p_now[row][col]=1/n_zeros
                else:
                    self.p_now[row][col]=0
        # return self.p_now
        

# way()


if __name__=="__main__":

    way=way()
    print(np.sum(way.p_now))
    way.down_step()
    # way.down_step()
    # way.down_step()
    # way.down_step()
    # print(way.p_now)
    print(np.sum(way.p_now))

    