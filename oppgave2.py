import random
import math


#Class for organizing our representation
#line tells what line the pin is on, if the pin breaks the line with its next step, its wound up.
class Pin:
    def __init__(self, l, w, n, i):
        self.line = l
        self.wind = w
        self.ne = n
        self.ident = i
        
#Makes the default board for each puzzle, an array of pins
def make_board(N,M, start, end):
    board = []
    row = M*[0]
    for i in range(N):
        board.append(list(row))
    for i in range(N):
        for j in range(M):
            board[i][j] = Pin("na",0,"na","")
    board[start[0]][start[1]] = Pin("na",1,"na","start") 
    board[end[0]][end[1]] = Pin("na",0,"na","end") 
    return board

#Finds a neighboor close in the searchspace, ether 1 step further, or backtracks one step, if the randomized action is illegal
def finn_nabo(board, start):
    random.seed()
    head_x = start[0]
    head_y = start[1]
    #To localize the head of our current solution.
    while board[head_x][head_y].ne != "na":
        if board[head_x][head_y].ne == "N":
            head_y +=1
        elif board[head_x][head_y].ne == "S":
            head_y -= 1
        elif board[head_x][head_y].ne == "E":
            head_x += 1
        elif board[head_x][head_y].ne == "W":
            head_x -= 1
        else:
            print("dude wtf!! feil i data: ",board[head_x][head_y].ne)
            return board

    rand = random.randrange(4)
    dir_x = 0
    dir_y = 0
    error = 0

    #You are not allowed to move further from the pin if it is the end pin.
    if board[head_x][head_y].ident == "end":
        error = 1

    elif rand == 0:
        dir_x = 1
        if head_x + dir_x >= len(board):
            error = 1
        elif board[head_x+dir_x][head_y+dir_y].ne != "na":
            error = 1
        else:
            if board[head_x][head_y].line != "E":
                board[head_x][head_y].wind = 1
            else:
                board[head_x][head_y].wind = 0
            board[head_x][head_y].ne = "E"
            board[head_x+dir_x][head_y+dir_y].line = "E"
            return board
        
    elif rand == 1:
        dir_x = -1
        if head_x + dir_x <0:
            error = 1
        elif board[head_x+dir_x][head_y+dir_y].ne != "na":
            error = 1
        else:
            if board[head_x][head_y].line != "W":
                board[head_x][head_y].wind = 1
            else:
                board[head_x][head_y].wind = 0
            board[head_x][head_y].ne = "W"
            board[head_x+dir_x][head_y+dir_y].line = "W"
            return board

    elif rand == 2:
        dir_y = 1
        if head_y + dir_y >= len(board[0]):
            error = 1
        elif board[head_x+dir_x][head_y+dir_y].ne != "na":
            error = 1
        else:
            if board[head_x][head_y].line != "N":
                board[head_x][head_y].wind = 1
            else:
                board[head_x][head_y].wind = 0
            board[head_x][head_y].ne = "N"
            board[head_x+dir_x][head_y+dir_y].line = "N"
            return board

    elif rand == 3:
        dir_y = -1
        if head_y + dir_y < 0:
            error = 1
        elif board[head_x+dir_x][head_y+dir_y].ne != "na":
            error = 1
        else:
            if board[head_x][head_y].line != "S":
                board[head_x][head_y].wind = 1
            else:
                board[head_x][head_y].wind = 0
            board[head_x][head_y].ne = "S"
            board[head_x+dir_x][head_y+dir_y].line = "S"
            return board
    else:
        print("FO REAL!?!?!?! random funksjonen er feil?")
        error = 1
    
    if error == 1:
        if board[head_x][head_y].line == "N":
            board[head_x][head_y-1].ne = "na"
        elif board[head_x][head_y].line == "S":
            board[head_x][head_y+1].ne = "na"
        elif board[head_x][head_y].line == "E":
            board[head_x-1][head_y].ne = "na"
        elif board[head_x][head_y].line == "W":
            board[head_x+1][head_y].ne = "na"
        board[head_x][head_y].line = "na"
        return board
    print("error doesnt work")
        

#Objective function, counts how many pins are connected, subtracts all winds and gives a slight bonus if the end has been reached. 
def objective_function(board, W, D):
    total_cost = 0
    points = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].wind == 1:
                total_cost += W
            if board[i][j].ne != "na":
                points += W+1
            if board[i][j].ident == "end" and board[i][j].line != "na":
                points += W+1 
    points -= total_cost
    dim = len(board)
    two_dim = dim*2
    print((float(points))/(len(board)*len(board)*W))
    if ((float(points))/(len(board)*len(board)*W))<0:
        return 0.0
    return ((float(points))/(len(board)*len(board)*W))







def simulated_annealing(n,m,w,d,start, end):
    neighbors_gen = 10
    temperature = 0.05    
    dtemp = 0.000003        


    #Start point
    brett = make_board(n,m,start,end)
    value = objective_function(brett, w,d)

    while True:
        #print "while loop"

        if objective_function(brett, w,d) >= 1:
            print "Found solution"
            return brett

        neighbors = []
        value_list = []
        max_index = 0

        for i in range(neighbors_gen):

            neighbors.append(finn_nabo(brett,start))
            value_list.append(objective_function(neighbors[i],w,d))

            if value_list[i] >  value_list[max_index]:
                max_index = i


        if (value > 0 ):
            q = math.fabs((value_list[max_index] - value)/value)
        else:
            q = value_list[max_index]/0.001
        print "q = %f"%q
        print "temperature = %f" %temperature

        if temperature >0:
            z = min(1,math.exp(-q/temperature))
        else:
            z = min(1,math.exp(-q/0.00001))
         

        print "z = %f" %(z)


        if (random.random() > z):
            print "Exploiting"
            brett = neighbors[max_index]
        else:
            print "exploring"
            brett = neighbors[random.randrange(neighbors_gen)]

        temperature -= dtemp

    return brett



print "finished"
simulated_annealing(4,4,3,2, [0,0],[3,3])





# brett = make_board(4,4,[0,0],[3,3])
# losning = list(10*[0])
# losning[0] = finn_nabo(brett, [0,0])
# for i in range(9):
#     objective_function(losning[i], 2,2)
#     losning[i+1] = finn_nabo(losning[i],[0,0])



