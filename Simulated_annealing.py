import random 
import math



class Basket:
   N = 0
   M = 0
   K = 0

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
   diag_penalty = 0.4
   norm_penalty = 0.55


   M = len(basket.eggs)
   for i in range(len(basket.eggs)): #checks columns
      nr_of_eggs = 0   
      for space in basket.eggs[i]:
         if space == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:         
               points -= norm_penalty
              # print("minus from columns")
   for j in range(len(basket.eggs[0])): #checks rows
      nr_of_eggs = 0                      
      for row in basket.eggs:
         if row[j] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:         
               points -= norm_penalty
               #print("minus from rows")
   
   # if abs(points) > M*2 and K==1:
   #    for row in basket.eggs:       #1 point per egg in the basket
   #       for j in range(len(basket.eggs[0])):
   #          if row[j] == 1:
   #             points += 1
   #    if points < 0:                #no point returning a negative answer. 
   #       return 0.0001 
   #    return float(points)/(M*K)
   
   for j in range(basket.M):     #checks diagonals
      nr_of_eggs = 0
      nr_of_eggs1 = 0 
      for i in range(j+1):
         if basket.eggs[i][j-i] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:
               points -= diag_penalty
         if basket.eggs[(basket.N-1)-i][j-i] == 1:
            nr_of_eggs1 +=1
            if nr_of_eggs1 > K:
               points -= diag_penalty
      nr_of_eggs1 = 0
      nr_of_eggs = 0
      for i in range(basket.M-j):
         if basket.eggs[i][j+i] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:
               points -= diag_penalty
         if basket.eggs[(basket.N-1)-i][j+i] == 1:
            #print(j, nr_of_eggs1)
            nr_of_eggs1 += 1
            #print(j, nr_of_eggs1)
            if nr_of_eggs1 > K:
               points -= diag_penalty


   for row in basket.eggs:       #1 point per egg in the basket
      for j in range(len(basket.eggs[0])):
         if row[j] == 1:
            points += 1

   #print(points)
   if points < 0:                #no point returning a negative answer. 
      return 0.0001   
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


   # for j in range(len(basket.eggs[0])): #checks rows
   #    nr_of_eggs = 0                      
   #    for row in basket.eggs:
   #       if row[j] == 1:
   #          nr_of_eggs += 1
   #          if nr_of_eggs > K:         
   #             points -= 1


   # if abs(points) > M*2 and K==1:
   #    for row in basket.eggs:       #1 point per egg in the basket
   #       for j in range(len(basket.eggs[0])):
   #          if row[j] == 1:
   #             points += 1
   #    return float(points)/(M*K)
   

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
   #          nr_of_eggs1 += 1
   #          if nr_of_eggs1 > K:
   #             points -= 0.5

   # for row in basket.eggs:       #1 point per egg in the basket
   #    for j in range(len(basket.eggs[0])):
   #       if row[j] == 1:
   #          points += 1
   # if points < 0:                #no point returning a negative answer. 
   #    return 0.001   
   # return float(points)/(M*K) #N = M i alle oppgavene






def print_solution(solution):
   x = ""
   for i in solution:

      x = x + "".join(str(i)) + "\n"
   print x




def find_nabo(basket):      
      random.seed()                       
      
      nabo = Basket(basket.N,basket.M, basket.K)

      for egg in basket.eggs:

         nabo.eggs.append(list(egg))
      x = random.randrange(len(basket.eggs))
      y = random.randrange(len(basket.eggs[0]))    
      if nabo.eggs[x][y] == 1:                   
         nabo.eggs[x][y] = 0                       
      else:                                     
         nabo.eggs[x][y] = 1    
      return nabo





def simulated_annealing(n,m,k):
   neighbors_gen = 10
   temperature = 0.05    
   dtemp = 0.000003        


   #Start point
   p = Basket(n,m,k)
   p.init_start_eggs()
   p.value = objective_function(p, k)
   for i in range(p.N):
      for j in range(p.M):
         p.eggs[i][j] = random.randrange(2)

   p.value = objective_function(p, k)
   print p.value


   while True:
      #print "while loop"

      if objective_function(p, k) >= 1:
         print "Found solution"
         return p

      neighbors = []
      max_index = 0

      for i in range(neighbors_gen):
         new_neighbor = find_nabo(p)
         new_neighbor.value = objective_function(new_neighbor, k)
         neighbors.append(new_neighbor)

         if neighbors[i].value >  neighbors[max_index].value:
            max_index = i

      print "p value = %f, best neighbor value= %f"%(p.value, neighbors[max_index].value)

      if (p.value > 0 ):
         q = math.fabs((neighbors[max_index].value - p.value)/p.value)
      else:
         q = neighbors[max_index].value/0.001
      print "q = %f"%q
      print "temperature = %f" %temperature

      if temperature >0:
         z = min(1,math.exp(-q/temperature))
      else:
         z = min(1,math.exp(-q/0.00001))
     

      print "z = %f" %(z)


      if (random.random() > z):
         print "Exploiting"
         p = neighbors[max_index]
      else:
         print "exploring"
         p = neighbors[random.randrange(neighbors_gen)]

      temperature -= dtemp

   return p














   


solution = simulated_annealing(10,10,3)

print_solution(solution.eggs)
print "finished"



