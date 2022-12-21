from Maze import *
from collections import defaultdict
import random
# def way():
class Way:
    
    def __init__(self,file_path):
        self.maze=generate_maze(file_path)
        # print(self.maze)
        self.n_row=self.maze.shape[0]
        self.n_col=self.maze.shape[1]
        self.drone_maze=self.maze.copy()
        self.p_now=self.maze.copy()
        self.p_next=np.zeros(self.maze.shape)
        self.init_probabilities()
        self.init_drone()
        # print(self.p_now)
        self.right=[0, 1]
        self.left=[0, -1]
        self.down=[1, 0]
        self.up=[-1, 0]
        self.move_list=[]
        

    #iterate over rows
    def init_drone(self):
        foundLoc=False
        while not foundLoc:
            r=random.randint(0, self.n_row-1)
            c=random.randint(0, self.n_col-1)
            if self.drone_maze[r][c]!=5:
                foundLoc=True
        self.drone=[r,c]
        self.drone_maze[r][c]=10
    
    def drone_move(self,dir):
        self.drone_maze[self.drone[0],self.drone[1]]=0
        next_r=self.drone[0]+dir[0]
        next_c=self.drone[1]+dir[1]
        if next_r>=0 and next_r<self.n_row and next_c>=0 and next_c<self.n_col:
            if self.maze[next_r][next_c]==5:
                next_r=self.drone[0]
                next_c=self.drone[1]
        else:
            next_r=self.drone[0]
            next_c=self.drone[1]

        # if next_c>=0 and next_c<self.n_col:
        #     if self.maze[next_r][next_c]==5:
        #         next_c=self.drone[1]
        # else:
        #     next_c=self.drone[1]
        self.drone[0]=next_r
        self.drone[1]=next_c
        self.drone_maze[next_r][next_c]=10
            

        # self.drone_maze[self.drone[0],self.drone[1]]=0
        # next_r=self.drone[0]+dir[0]
        # next_c=self.drone[1]+dir[1]
        # if next_r<0 or next_r>self.n_row-1:
        #     next_r=self.drone[0]
        # if next_c<0 or next_c>self.n_row-1:
        #     next_c=self.drone[1]
        # if self.drone_maze[next_r][next_c]==5:
        # self.drone[0]=next_r
        # self.drone[1]=next_c
        # self.drone_maze[next_r][next_c]=10

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
        self.drone_move(self.down)
        self.move_list.append("Down")
    
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
        self.drone_move(self.right)
        self.move_list.append("Right")

    
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
        self.drone_move(self.left)
        self.move_list.append("Left")


    
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
        self.drone_move(self.up)
        self.move_list.append("Up")
    
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
        print("Drone Maze->\n")
        print(self.drone_maze)
        print("\nP_now->\n")
        print(np.sum(self.p_now))
        print(self.p_now)
        print("Non Zeros->",np.count_nonzero(self.p_now))

        print("Move List ->",*self.move_list)
        print("No. of Steps ->",len(self.move_list))
        # print("\nP_next->\n")
        # print(np.sum(self.p_next))
        # print(self.p_next)
    
    def random_step(self):
        ch=random.choice([1,2,3,4])
        if ch==1:
            self.down_step()
            # self.move_list.append(1)
        elif ch==2:
            self.left_step()
            # self.move_list.append(2)
        elif ch==3:
            self.up_step()
            # self.move_list.append(3)
        elif ch==4:
            self.right_step()
            # self.move_list.append(4)

    def get_max_list(self):
        self.max_value=np.max(self.p_now)
        print("MAx value = ",self.max_value)
        self.max_list=[]
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.p_now[r][c]==self.max_value:
                    self.max_list.append([r,c])
        return self.max_list
    
    def get_non_zero_list_prob(self):
        self.non_zero_list=[]
        self.non_zero_dict=defaultdict()
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.p_now[r][c]!=0:
                    self.non_zero_list.append([r,c])
                    self.non_zero_dict[(r,c)]=self.p_now[r][c]
        self.non_zero_dict=dict(sorted(self.non_zero_dict.items(), key=lambda item: item[1]))
        #List sorted in non-decreasing order of probabilities
        return list(self.non_zero_dict.keys())
        # return self.non_zero_list
    
    def get_non_zero_list(self):
        self.non_zero_list=[]
        self.non_zero_dict=defaultdict()
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.p_now[r][c]!=0:
                    self.non_zero_list.append([r,c])
                    self.non_zero_dict[(r,c)]=self.p_now[r][c]
        self.non_zero_dict=dict(sorted(self.non_zero_dict.items(), key=lambda item: item[1]))
        #List sorted in non-decreasing order of probabilities
        return list(self.non_zero_dict.keys())
        # return self.non_zero_list
    def plot_maze(self,arr):
        # print(maze)
        # plt.imshow(arr, "Dark2")
        plt.imshow(arr, "ocean")
        plt.show()

# way()


def main2():

    file_path='Schematics/Schema_1.txt'
    # file_path='/Users/abhishek.sawalkar/Library/Mobile Documents/com~apple~CloudDocs/AI Project/Finding_Your_Way/Schematics/Schema_2.txt'
    way=way(file_path)
    # n_iterations=
    #First taking random step
    # way.random_step()
    # way.print_state()
    for k in range(n_iterations):
        # max_list=way.get_max_list()
        print("\n\n Step Number ->",k)
        if k<way.n_row-1:
            way.left_step()
        elif k<2*way.n_col-1:
            way.up_step()
        elif k<3*way.n_col-1:
            way.right_step()
        elif k<4*way.n_col-1:
            way.left_step()
        # elif k<5*way.n_col-1:
        #     way.right_step()
        
        # way.plot_maze(way.maze)
        # way.print_state()
        # way.plot_maze(way.p_now)
    way.print_state()
    # way.plot_maze(way.p_now)
    print("Max Prob Value = ",way.get_max_list())
    non_zero_list=way.get_non_zero_list()
    print("Non Zero Prob list = ",non_zero_list)
    print("Drone at -> ",way.drone)
    if way.drone in non_zero_list:
        print("Yes")
        print("prob = ",way.p_now[way.drone[0],way.drone[1]])
    else:
        print("No")




if __name__=="__main__":
    file_path='/Users/abhishek.sawalkar/Library/Mobile Documents/com~apple~CloudDocs/AI Project/Finding_Your_Way/Schematics/Schema_2.txt'
    file_path='Schematics/Schema_1.txt'
    way=Way(file_path)
    # way.print_state()
    # way.plot_maze(way.p_now)
    # == Down Testing
    way.down_step()
    way.plot_maze(way.p_now)
    # way.print_state()
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

    # = Combined Testing
    # n_iterations=10000
    # threshold_reached=False
    # for k in range(n_iterations):
    #     ch=random.choice([1,2,3,4])
    #     if ch==1:
    #         way.down_step()
    #     elif ch==2:
    #         way.right_step()
    #     elif ch==3:
    #         way.left_step()
    #     elif ch==4:
    #         way.up_step()
    #     # way.print_state()
    #     for i in range(way.n_row):
    #         for j in range(way.n_col):
    #             if way.p_now[i][j]>=0.5:
    #                 threshold_reached=True
    #                 break
    #     if threshold_reached:
    #         print("Threshold reached at ",k)
    #         # way.print_state()
    #         break
        



    