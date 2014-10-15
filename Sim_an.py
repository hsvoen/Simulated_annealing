import random 
import math

class Basket:
   N = 0
   M = 0
   K = 0
   #eggs = []   
   def __init__(self, n,m, k):
      self.M = m
      self.N = n
      self.K = k
      self.eggs = []
      self.value = float(0)         

   def set_eggs(self, table):
      self.eggs = table

   def init_start_eggs(self):
      row = [0]*self.N
      for i in range(self.M):
         
         self.eggs.append(list(row))


def objective_function(basket, K):
   points = 0.0
   M = len(basket.eggs)
   for i in range(len(basket.eggs)): #checks columns
      nr_of_eggs = 0   
      for space in basket.eggs[i]:
         if space == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:         
               points -= 1
              # print("minus from columns")
   for j in range(len(basket.eggs[0])): #checks rows
      nr_of_eggs = 0                      
      for row in basket.eggs:
         if row[j] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:         
               points -= 1
               #print("minus from rows")
   if abs(points) > M*2:
      for row in basket.eggs:       #1 point per egg in the basket
         for j in range(len(basket.eggs[0])):
            if row[j] == 1:
               points += 1
      return float(points)/(M*K)
   
   for j in range(basket.M):     #checks diagonals
      nr_of_eggs = 0
      nr_of_eggs1 = 0 
      for i in range(j+1):
         if basket.eggs[i][j-i] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:
               points -= 0.5
         if basket.eggs[(basket.N-1)-i][j-i] == 1:
            nr_of_eggs1 +=1
            if nr_of_eggs1 > K:
               points -= 0.5
      nr_of_eggs1 = 0
      nr_of_eggs = 0
      for i in range(basket.M-j):
         if basket.eggs[i][j+i] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:
               points -= 0.5
         if basket.eggs[(basket.N-1)-i][j+i] == 1:
            #print(j, nr_of_eggs1)
            nr_of_eggs1 += 1
            #print(j, nr_of_eggs1)
            if nr_of_eggs1 > K:
               points -= 0.5

   for row in basket.eggs:       #1 point per egg in the basket
      for j in range(len(basket.eggs[0])):
         if row[j] == 1:
            points += 1
   #print(points)
   if points < 0:                #no point returning a negative answer. 
      return 0   
   return float(points)/(M*K) #N = M i alle oppgavene







   # points = 0.0
   # M = len(basket.eggs)
   # for i in range(len(basket.eggs)): #checks columns
   #    nr_of_eggs = 0   
   #    for space in basket.eggs[i]:
   #       if space == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:         
   #             points -= 1
   #            # print("minus from columns")
   # for j in range(len(basket.eggs[0])): #checks rows
   #    nr_of_eggs = 0                      
   #    for row in basket.eggs:
   #       if row[j] == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:         
   #             points -= 1
   #             #print("minus from rows")

   # for j in range(basket.M):     #checks diagonals
   #    nr_of_eggs = 0
   #    nr_of_eggs1 = 0 
   #    for i in range(j+1):
   #       if basket.eggs[i][j-i] == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:
   #             points -= 0.5
   #       if basket.eggs[(basket.N-1)-i][j-i] == 1:
   #          nr_of_eggs1 +=1
   #          if nr_of_eggs1 > K:
   #             points -= 0.5
   #    nr_of_eggs1 = 0
   #    nr_of_eggs = 0
   #    for i in range(basket.M-j):
   #       if basket.eggs[i][j+i] == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:
   #             points -= 0.5
   #       if basket.eggs[(basket.N-1)-i][j+i] == 1:
   #          #print(j, nr_of_eggs1)
   #          nr_of_eggs1 += 1
   #          #print(j, nr_of_eggs1)
   #          if nr_of_eggs1 > K:
   #             points -= 0.5

   # for row in basket.eggs:       #1 point per egg in the basket
   #    for j in range(len(basket.eggs[0])):
   #       if row[j] == 1:
   #          points += 1
   # #print(points)
   # if points < 0:                #no point returning a negative answer. 
   #    return 0   
   # return float(points)/(M*K) #N = M i alle oppgavene





   # points = 0
   # M = len(basket.eggs)
   # for i in range(len(basket.eggs)):
   #    nr_of_eggs = 0   
   #    for space in basket.eggs[i]:
   #       if space == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:         
   #             points -= 1
   # for j in range(len(basket.eggs[0])):
   #    nr_of_eggs = 0                      #Sjekke diagonaler mangler
   #    for row in basket.eggs:
   #       if row[j] == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:         
   #             points -= 1
         
   # for row in basket.eggs:
   #    for j in range(len(basket.eggs[0])):
   #       if row[j] == 1:
   #          points += 1                        
   # if points < 0:
   #    return 0   
   # return float(points)/(M*K) #N = M i alle oppgavene

def print_solution(solution):
   x = ""
   for i in solution:

      x = x + "".join(str(i)) + "\n"
   print x

def find_nabo(basket):      
      #print "Find nabo called"
      random.seed()                       # Maa ha krav til godkjent endring. 
      
      #print "input argument"
      #print basket.eggs

      nabo = Basket(basket.N,basket.M, basket.K)

      for egg in basket.eggs:

         nabo.eggs.append(list(egg))
      x = random.randrange(len(basket.eggs))
      y = random.randrange(len(basket.eggs[0]))    # forslag 1: ikke lov aa plassere egg som bryter regler. 
      if nabo.eggs[x][y] == 1:                   # 2: skjekk om obj funksjon ooker: hvis ja: Coolio, hvis nei, sjanse for aa ikke akseptere og proove paa nytt. 
         nabo.eggs[x][y] = 0                       # 3: Legge inn for at egg flyttes fremfor aa fjaernes? slik at de kun fjaernes om det ikke finnes lovlige flytt. (egget som "bryter" flest regler? ) 
      else:                                       # 4: mulig med en funskjon som finner lovelige plasseringer?
         nabo.eggs[x][y] = 1    
      return nabo

def simulated_annealing(n,m,k):
   neighbors_gen = 10

   #Start point
   p = Basket(n,m,k)
   p.init_start_eggs()
   p.value = objective_function(p, k)
   for i in range(p.N):
      for j in range(p.M):
         p.eggs[i][j] = random.randrange(2)

   temperature = 1000 #Not sure what a good value is.
   dtemp = 5         #Not sure what a good standard difference is.

   while True:
      #print "while loop"

      if objective_function(p, k) >= 1:
         print "Found solution"
         return p

      neighbors = []
      max_index = 0

      #print "generating neighbors"
      for i in range(neighbors_gen):
         new_neighbor = find_nabo(p)
         new_neighbor.value = objective_function(new_neighbor, k)
         neighbors.append(new_neighbor)

         if neighbors[i].value >  neighbors[max_index].value:
            max_index = i

      print "p value = %f"%p.value
      if (p.value > 0 ):
         q = (neighbors[max_index].value - p.value)/p.value
      else:
         q = neighbors[max_index].value

      if temperature >0:
         z = min(1,math.exp(-q/temperature))
      else:
         z = 0
      x = random.random()

      print "z = %f, x = %f" %(z,x)


      if (x > z):
         print "Exploiting"
         p = neighbors[max_index]
      else:
         print "exploring"
         p = neighbors[random.randrange(neighbors_gen)]

      temperature -= dtemp

   return p














   


solution = simulated_annealing(10,10,1)
print_solution(solution.eggs)
print "finished"
# print "P before new neighbor"
# print  p.eggs
# P1 = find_nabo(p)
# print "P1:"
# print P1.eggs
# print "P after new neighbor"
# print p.eggs

# print objective_function(p,1)


