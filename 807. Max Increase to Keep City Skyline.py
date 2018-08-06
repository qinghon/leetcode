import random


#grid=[]

def get_guid(x,y):
    guid=[]
    for a in range(y):
        grid[a]=[random.randint(0,100) for b in range(x)] 

def get_max_l(grid):
    x_max=[]
    y_max=[]
    temp=[]

    if len(grid)==0:
        return 0,0
    y_l=len(grid)
    x_l=len(grid[0])

    for y in range(x_l):
        x_max.append(max(grid[y]))
        
    for x in range(x_l):
        y_max.append(max([grid[y][x] for y in range(y_l)]))
            
    return x_max,y_max

def out_max_l(x_max,y_max):
    gridNew=[]
    for x in range(len(x_max)):
        gridNew.append([])
        for y in range(len(y_max)):
            gridNew[x].append(min([y_max[y],x_max[x]]))
        
    return gridNew
grid = get_guid(20,20)
x_max,y_max=get_max_l(grid)
if x_max!=0 and y_max!=0:
    
    print(out_max_l(x_max,y_max))
else :
    print(0)


    