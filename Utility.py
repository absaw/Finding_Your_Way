from collections import defaultdict
from Maze import *
from BFS import *
import math
from datetime import datetime
from time import time
import pickle
def print_dict(d):
    for key,value in d.items():
        print(key," : ",value)

# if __name__=="__main__":
def main():
    start = time()

    # #=========== Log file =======================
    # # filename_txt="Results/Utility4.txt"
    # filename_txt="/Users/abhishek.sawalkar/Library/Mobile Documents/com~apple~CloudDocs/AI Project/BetterSmarterFasterCircleOfLife/Results/Utility17.txt"
    # # filename_csv="Results/AgentOne.csv"
    # file=open(filename_txt,"w")
    # # csvfile = open(filename_csv, "a")
    # # csv_writer=csv.writer(csvfile)
    # # fields=['Date Time','Simulation Number','Number of Graphs','Won','Died','Hanged','Comments']
    # # csv_writer.writerow(fields)
    # text = "\n\n\n======  Start Time  =========->  " + \
    #     datetime.now().strftime("%m/%d/%y %H:%M:%S")
    # file.write(text)
    # # file.write("\nNo. of Simulations = 30")
    # # file.write("\nNo. of trials for each simulation = 100")
    # # csv_writer.writerow(["Execution Started"])
    #============================================
    file_path='/Users/abhishek.sawalkar/Desktop/520 Video Lectures/Finding_Your_Way/Schematics/Schema_1.txt'
    maze=generate_maze(file_path)
    n_row=maze.shape[0]
    n_col=maze.shape[1]

    state_dict=defaultdict()
    final_utility=defaultdict()

    right=[0, 1]
    left=[0, -1]
    down=[1, 0]
    up=[-1, 0]
    # Defining State dictionary
    for pos_1_r in range(0,n_row):
        for pos_1_c in range(0,n_col):
            for pos_2_r in range(0,n_row):
                for pos_2_c in range(0,n_col):
                    if maze[pos_1_r,pos_1_c] != 5 and maze[pos_2_r,pos_2_c] != 5:

                        key=[(pos_1_r,pos_1_c),(pos_2_r,pos_2_c)]
                            # print(key)
                        # key=sorted(key)
                            # print(key)
                        key=(key[0][0],key[0][1],key[1][0],key[1][1])
                        if key not in state_dict.keys():

                            state_dict[key]=[0,0] #reward, utility
                            final_utility[key]=0

    #Reading the stored graph
    # G = nx.read_gpickle("StoredGraph/Graph1.gpickle")
    # G = nx.read_gpickle("/Users/abhishek.sawalkar/Library/Mobile Documents/com~apple~CloudDocs/AI Project/BetterSmarterFasterCircleOfLife/StoredGraph/Graph1.gpickle")
    
    #======Distance Dictionary Generation =========
    # dist_dict=defaultdict()
    # for pos_1_r in range(0,n_row):
    #     for pos_1_c in range(0,n_col):
    #         for pos_2_r in range(0,n_row):
    #             for pos_2_c in range(0,n_col):
    #                 if maze[pos_1_r,pos_1_c] != 5 and maze[pos_2_r,pos_2_c] != 5:
    #                     key=[(pos_1_r,pos_1_c),(pos_2_r,pos_2_c)]
    #                     # print(key)
    #                     # key=sorted(key)
    #                     # print(key)
    #                     key=(key[0][0],key[0][1],key[1][0],key[1][1])
    #                     if key not in dist_dict.keys():
    #                         distance=len(get_bfs_path(maze, n_row, n_col, (pos_1_r,pos_1_c), (pos_2_r,pos_2_c)))-1
    #                         # print(distance)
    #                         dist_dict[key]=distance
    # print(dist_dict)
    # dist_file = open("StoredDistances/dist_dict_schema1.pkl", "wb")
    # pickle.dump(dist_dict, dist_file)
    # dist_file.write(str(final_utility))
    # dist_file.close()
    #==========================

    # print(len(dist_dict))
    # print(len(state_dict))
    with open("StoredDistances/dist_dict_schema1.pkl", 'rb') as handle:
        data = handle.read()
    dist_dict = pickle.loads(data)

    # return
    
    #Setting initial rewards and utility
    for state in state_dict:
        pos_1=(state[0],state[1])
        pos_2=(state[2],state[3])
        
        if pos_1==pos_2: #agent and prey has same position
            state_dict[state]=[0,0] #minimum possible expected number of steps to prey is 0
        # elif state[0]==state[2]:
        #     state_dict[state]=[math.inf,0] #reaching prey is impossible so a high value
        else:
            # distance_to_prey=len(get_bfs_path(G,state[0],state[1]))
            
            distance=dist_dict[state]
            state_dict[state]=[1]+[distance]
    # print(dist_dict[(0, 0, 0, 1)])
    #=============================================================
    #=========== Value Iteration Algorithm =======================
    #=============================================================
    beta=0.9
    n_iterations=50
    # error_list=[0]*len(state_dict)
    error_list=[]
    for k in range(n_iterations):
        #Running for all states
        error=0
        #For each particular state-We will calculate U* for all possible actions. Then take the min of these values to be the final U for this iteration
        for state in state_dict:
            #Generate action space by getting the neighbors of the current cell of both cells
            pos_1=(state[0],state[1])
            pos_2=(state[2],state[3])
            
            if pos_1==pos_2: #agent and prey has same position
                min_utility=0
                state_dict[state].append(min_utility)
                continue
            #Cell1 is in neighborhood of cell 2
            if dist_dict[state]==1:
                min_utility=1
                state_dict[state].append(min_utility)
                continue
            
            #Now we need to figure out the action space of the 2 cells, which would be mainly 4 actions - UP, DOWN, Left, Right
            
            #Up operation
            r1=state[0]
            c1=state[1]
            r2=state[2]
            c2=state[3]
            action_space=defaultdict()
            
            up_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,up)
            down_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,down)
            left_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,left)
            right_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,right)
            #Initializing utilities
            action_space["Up"]=state_dict[up_state][-1]
            action_space["Down"]=state_dict[down_state][-1]
            action_space["Left"]=state_dict[left_state][-1]
            action_space["Right"]=state_dict[right_state][-1]
            # #Initializing utilities
            # action_space[up_state]=state_dict[up_state][-1]
            # action_space[down_state]=state_dict[up_state][-1]
            # action_space[left_state]=state_dict[up_state][-1]
            # action_space[right_state]=state_dict[up_state][-1]

            # down_state,left_state,right_state]
            # prev_utility=

            reward=state_dict[state][0]
            min_utility=min(action_space.values())
            min_possible_action_list=[key for key in action_space if action_space[key]==min_utility] # getting the minimum action
            min_action=random.choice(min_possible_action_list)
            prev_utility=action_space[min_action]
            
            utility=reward+beta*prev_utility

            state_dict[state].append(utility)


                
            # #Up states for pos 1
            # if r1-1>=0:
            #     if maze[r1-1,c1]!=5:
            #         up_state_1=(r1-1,c1)
            #     else:
            #         up_state_1=(r1,c1)
            # else:
            #     up_state_1=(r1,c1)
            
            # #Up states for pos 1
            # if r2-1>=0:
            #     if maze[r2-1,c1]!=5:
            #         up_state_2=(r2-1,c2)
            #     else:
            #         up_state_2=(r2,c2)
            # else:
            #     up_state_2=(r2,c2)
            
            # up_state=[up_state_1,up_state_2]
            # up_state=sorted(up_state)
            # up_state=(up_state[0][0],up_state[0][1],up_state[1][0],up_state[1][1])
            # print("State->",state)
            # print(up_state)
            
            # continue


            if k>2 :
                error+=state_dict[state][-1]-state_dict[state][-2]
        print("Iteration Done ->",k)
        iteration_error=error/len(state_dict)
        print("Iteration Error = ",iteration_error)
        # if k>5 and abs(iteration_error)<0.001:
        #     break
        error_list.append(iteration_error)
    # print(state_dict)
    value_list=state_dict.values()
    m=-1
    for l in value_list:
        l2=l[2:]
        m_l=max(l)
        if m<m_l and not math.isinf(m_l):
            m=m_l
    
    # #========= Constructing utility dictionary ==========
    for state in final_utility:
        final_utility[state]=state_dict[state][-1]
    # #======== Dumping a dictionary as pickle and then reading it again using loads =====
    final_utility_file = open("StoredUtilities/Schema1.pkl", "wb")
    pickle.dump(final_utility, final_utility_file)
    # final_utility_file.write(str(final_utility))
    final_utility_file.close()
    
    #Whole utility file

   

    end=time()
    file = open("StoredUtilities/Schema1_Result.txt", "w")
    print("Max Utility = ",m)
    file.write('\n Max Utility =  %s'%str(m))
    file.write("\n\nExecution Time = "+str(end-start)+" s\n")

    file.write('\n Iteration Error->')
    for error in error_list:
        file.write('  %s, '%str(error))

    file.write('\n \nState Dictionary->')
    for key, value in state_dict.items(): 
        file.write('    %s  :       %s  \n' % (key, value[30:]))
    print("Done")
    # print("Execution time : "+str(end-start)+" s")
    # print_dict(state_dict)

def get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,dir):
    #Up states for pos 1
    next_r1=r1+dir[0]
    next_c1=c1+dir[1]
    if next_r1>=0 and next_r1<n_row and next_c1>=0 and next_c1<n_col:
        if maze[next_r1,next_c1]!=5:
            dir_state_1=(next_r1,next_c1)
        else:
            dir_state_1=(r1,c1)
    else:
        dir_state_1=(r1,c1)
    
    #Up states for pos 2
    next_r2=r2+dir[0]
    next_c2=c2+dir[1]
    if next_r2>=0 and next_r2<n_row and next_c2>=0 and next_c2<n_col:
        if maze[next_r2,next_c2]!=5:
            dir_state_2=(next_r2,next_c2)
        else:
            dir_state_2=(r2,c2)
    else:
        dir_state_2=(r2,c2)


    # if r2-1>=0:
    #     if maze[r2-1,c1]!=5:
    #         dir_state_2=(r2-1,c2)
    #     else:
    #         dir_state_2=(r2,c2)
    # else:
    #     dir_state_2=(r2,c2)
    
    dir_state=[dir_state_1,dir_state_2]
    dir_state=(dir_state[0][0],dir_state[0][1],dir_state[1][0],dir_state[1][1])
    return dir_state
main()




















