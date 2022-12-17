import numpy as np
import matplotlib.pyplot as plt

def generate_maze():
    
    schematic_file=open('Schematics/Schema_1.txt', 'r')
    schema_data=schematic_file.readlines()
    print(type(schema_data))
    n_row=len(schema_data)
    n_col=len(schema_data[0].strip())
    maze=np.zeros([n_row,n_col])
    
    for row in range(len(schema_data)):
        line=schema_data[row].strip()

        for col in range(len(line)):
            if line[col]=='X':
                maze[row][col]=5
    
    # print(maze)
    # plot_maze(maze)
    return maze
def plot_maze(maze):
    # print(maze)
    plt.imshow(maze, "Dark2")
    plt.show()
# generate_maze()