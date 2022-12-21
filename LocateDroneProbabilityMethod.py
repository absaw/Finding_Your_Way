from Maze import *
from BFS import *
from Way import *
from Utility import *
import random

def locate_Drone():

    # file_path='Schematics/Schema_1.txt'
    file_path='Schematics/Schema_1.txt'
    way=Way(file_path)
    maze=way.maze
    n_row=way.n_row
    n_col=way.n_col
    steps=(n_row-1)*3
    #We have the utility of all cells in the maze, now we need to merge cells with max utility
    with open("StoredDistances/dist_dict_schema1.pkl", 'rb') as handle:
            data = handle.read()
    dist_dict = pickle.loads(data)


    for k in range(steps):
        # max_list=way.get_max_list()
        # print("\n\n Step Number ->",k)
        if k<way.n_row-1:
            way.left_step()
        elif k<2*(way.n_col-1):
            way.up_step()
        elif k<3*(way.n_col-1):
            way.right_step()
        # elif k<4*way.n_col-1:
        #     way.left_step()
        # elif k<5*way.n_col-1:
        #     way.right_step()
        
        # way.plot_maze(way.maze)
        # way.print_state()
        # way.plot_maze(way.p_now)

    #Now we will try to merge the cells with non_zero probability

    # way.print_state()
    # print("\nSummary ========\n")
    # way.print_state()
    # print("Max Prob Value = ",way.get_max_list())
    # non_zero_list=way.get_non_zero_list()
    # print("Non Zero Prob list = ",non_zero_list)
    # print("Drone at -> ",way.drone)
    # if way.drone in non_zero_list:
    #     print("Drone in Drone list")
    #     print("prob = ",way.p_now[way.drone[0],way.drone[1]])
    # else:
    #     print("No")
    # return





    #Merge 2 points with max prob of having drone
    with open("StoredUtilities/Schema1.pkl", 'rb') as handle:
        data = handle.read()
    util_dict = pickle.loads(data)
    
    right=[0, 1]
    left=[0, -1]
    down=[1, 0]
    up=[-1, 0]
    non_zero_list=way.get_non_zero_list()
    non_zeros=np.count_nonzero(way.p_now)
    util_neighbors=defaultdict()
    
    #============================
    #Generate sorted utility list Method
    # sorted_util_dict=defaultdict()

    # for cell_1 in range(len(non_zero_list)):
    #     for cell_2 in range(cell_1,len(non_zero_list)):
    #         #Calculate utility for each non zero cell. Then sort the dictionary in non decreasing order
    #         if cell_1!=cell_2:
    #             state=(non_zero_list[cell_1][0],non_zero_list[cell_1][1],non_zero_list[cell_2][0],non_zero_list[cell_2][1])
    #             sorted_util_dict[state]=util_dict[state]
    # print(sorted_util_dict)
    # sorted_util_dict=dict(sorted(sorted_util_dict.items(), key=lambda item: item[1]))
    # non_zero_list=list(sorted_util_dict.keys())
    #============================
    # print(len(non_zero_list))
    # return
    while non_zeros>1:
        p1=non_zero_list.pop(0)
        p2=non_zero_list.pop(0)

        #Merge only 2 points for now, while ignoring rest.
        #Create new maze containing only p1 and p2' probability values
        #Move both points towards each other using their utility values
    

        while p1!=p2:

            r1=p1[0]
            c1=p1[1]
            r2=p2[0]
            c2=p2[1]

            up_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,up) #State = next(r1,c1,r2,c2)
            down_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,down)
            left_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,left)
            right_state=get_dir_state(n_row,n_col,maze,r1,c1,r2,c2,right)


            util_neighbors["Up"]=util_dict[up_state]
            util_neighbors["Down"]=util_dict[down_state]
            util_neighbors["Left"]=util_dict[left_state]
            util_neighbors["Right"]=util_dict[right_state]
        
            min_utility=min(util_neighbors.values())
            min_possible_action_list=[key for key in util_neighbors if util_neighbors[key]==min_utility] # getting the minimum action
            min_action=random.choice(min_possible_action_list) # Up or down or right or left
            #Take action to make them meet
            if min_action =="Up":
                way.up_step()
                p1=(up_state[0],up_state[1])
                p2=(up_state[2],up_state[3])
                
            elif min_action=="Down":
                way.down_step()
                p1=(down_state[0],down_state[1])
                p2=(down_state[2],down_state[3])
            elif min_action=="Right":
                way.right_step()
                p1=(right_state[0],right_state[1])
                p2=(right_state[2],right_state[3])
            elif min_action=="Left":
                way.left_step()
                p1=(left_state[0],left_state[1])
                p2=(left_state[2],left_state[3])
            
            # print("Point 1 : ",p1)
            # print("Point 2 : ",p2)
            # print("Distance:",dist_dict[(p1[0],p1[1],p2[0],p2[1])])


        
        # way.print_state()
        non_zero_list=way.get_non_zero_list()
        non_zeros=np.count_nonzero(way.p_now)
        print("Non Zeros :",non_zeros)
        print("No. of steps : ",len(way.move_list))
    


    # way.print_state()
    # way.plot_maze(way.p_now)
    print("\nSummary ========\n")
    way.print_state()
    print("Max Prob Value = ",way.get_max_list())
    non_zero_list=way.get_non_zero_list()
    print("Non Zero Prob list = ",non_zero_list)
    print("Drone at -> ",way.drone)
    if way.drone in non_zero_list:
        print("Drone in Drone list")
        print("prob = ",way.p_now[way.drone[0],way.drone[1]])
    else:
        print("No")
locate_Drone()