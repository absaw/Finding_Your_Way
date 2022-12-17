from maze import *

# def way():
class way:
    
    def __init__(self,file_path):
        self.maze=generate_maze(file_path)
        # print(self.maze)
        self.n_row=self.maze.shape[0]
        self.n_col=self.maze.shape[1]
        self.p_now=self.maze.copy()
        self.p_next=np.zeros(self.maze.shape)
        self.init_probabilities()
        # print(self.p_now)
        self.right=[0, 1]
        self.left=[0, -1]
        self.down=[1, 0]
        self.up=[-1, 0]

    #iterate over rows

    #down operation
    def down_step(self):
        for row in range(self.n_row):
            for col in range(self.n_col):
                if self.maze[row][col]!=5:
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
            # print("Row Done->",row)
            # self.print_state()
        self.p_now=self.p_next.copy()
    
    def right_step(self):
        for col in range(self.n_col):
            for row in range(self.n_row):

                if self.maze[row][col]!=5:
                    if col==0:
                        p_in=0
                        if self.maze[row][col+1]==0:
                            p_out=self.p_now[row][col]
                        else:
                            p_out=0
                            # self.p_next[row][col]=0

                        # self.p_next[row][col]=p_in-p_out
                    elif col==self.n_col-1:
                        p_out=0
                        #Deciding p_in
                        prev_col=col-1
                        if self.maze[row][prev_col]==5:
                            p_in=0
                        else:
                            p_in=self.p_now[row][prev_col]
                    else:
                        # p_next[row][col]=0
                        #Deciding p_in
                        prev_col=col-1

                        if self.maze[row][prev_col]==5:
                            p_in=0
                        else:
                            p_in=self.p_now[row][prev_col]
                        #Deciding p_out
                        next_col=col+1
                        p_out=0
                        if self.maze[row][next_col]==5:
                            p_out=0
                        else:
                            p_out=self.p_now[row][col]
                    self.p_next[row][col]=self.p_now[row][col]+p_in-p_out
            # print("Row Done->",row)
            # self.print_state()
        self.p_now=self.p_next.copy()
    
    def left_step(self):
        for col in range(self.n_col-1,-1,-1):
            for row in range(self.n_row):

                if self.maze[row][col]!=5:
                    if col==self.n_col-1:
                        p_in=0
                        if self.maze[row][col-1]==0:
                            p_out=self.p_now[row][col]
                        else:
                            p_out=0
                            # self.p_next[row][col]=0

                        # self.p_next[row][col]=p_in-p_out
                    elif col==0:
                        p_out=0
                        #Deciding p_in
                        prev_col=col+1
                        if self.maze[row][prev_col]==5:
                            p_in=0
                        else:
                            p_in=self.p_now[row][prev_col]
                    else:
                        # p_next[row][col]=0
                        #Deciding p_in
                        prev_col=col+1

                        if self.maze[row][prev_col]==5:
                            p_in=0
                        else:
                            p_in=self.p_now[row][prev_col]
                        #Deciding p_out
                        next_col=col-1
                        p_out=0
                        if self.maze[row][next_col]==5:
                            p_out=0
                        else:
                            p_out=self.p_now[row][col]
                    self.p_next[row][col]=self.p_now[row][col]+p_in-p_out
            # print("Row Done->",row)
            # self.print_state()
        self.p_now=self.p_next.copy()
    
    def up_step(self):
        for row in range(self.n_row-1,-1,-1):
            for col in range(self.n_col):
                if self.maze[row][col]!=5:
                    if row==self.n_row-1:
                        p_in=0
                        if self.maze[row-1][col]==0:
                            p_out=self.p_now[row][col]
                        else:
                            p_out=0
                            # self.p_next[row][col]=0

                        # self.p_next[row][col]=p_in-p_out
                    elif row==0:
                        p_out=0
                        #Deciding p_in
                        prev_row=row+1
                        if self.maze[prev_row][col]==5:
                            p_in=0
                        else:
                            p_in=self.p_now[prev_row][col]
                    else:
                        # p_next[row][col]=0
                        #Deciding p_in
                        prev_row=row+1
                        if self.maze[prev_row][col]==5:
                            p_in=0
                        else:
                            p_in=self.p_now[prev_row][col]
                        #Deciding p_out
                        next_row=row-1
                        p_out=0
                        if self.maze[next_row][col]==5:
                            p_out=0
                        else:
                            p_out=self.p_now[row][col]
                    self.p_next[row][col]=self.p_now[row][col]+p_in-p_out
            # print("Row Done->",row)
            # self.print_state()
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
    def print_sum(self,x):
        return np.sum(x)
    def print_state(self):
        print("\n\n Print State->")
        print("Maze->\n")
        print(self.maze)
        print("\nP_now->\n")
        print(np.sum(self.p_now))
        print(self.p_now)
        print("\nP_next->\n")
        print(np.sum(self.p_next))
        print(self.p_next)

# way()


if __name__=="__main__":
    # file_path='/Users/abhishek.sawalkar/Library/Mobile Documents/com~apple~CloudDocs/AI Project/Finding_Your_Way/Schematics/Schema_2.txt'
    file_path='Schematics/Schema_1.txt'
    way=way(file_path)
    # way.print_state()

    # == Down Testing
    way.down_step()
    way.print_state()
    # way.down_step()
    # way.print_state()
    # way.down_step()
    # way.print_state()
    # == Up Testing
    # way.up_step()
    # way.print_state()
    # way.up_step()
    # way.print_state()
    # way.up_step()
    # way.print_state()
    # way.up_step()
    # way.print_state()
    # == Right Testing
    # way.right_step()
    # way.print_state()
    # way.right_step()
    # way.print_state()
    # way.right_step()
    # way.print_state()
    # way.right_step()
    # way.print_state()
    # == left Testing
    # way.left_step()
    # way.print_state()
    # way.left_step()
    # way.print_state()
    # way.left_step()
    # way.print_state()
    # way.left_step()
    # way.print_state()
    # way.left_step()
    # way.print_state()
    # way.left_step()
    # way.print_state()
    # way.left_step()
    # way.print_state()

    