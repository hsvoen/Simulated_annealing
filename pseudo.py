import random 

class Basket:
   N = 0
   M = 0
   eggs = []   
   def __init__(self, n,m):
      row = [0]*n
      q = []
      for i in range(m):
         self.N = n
         self.M = m
         q.append(row)
         self.eggs = q
   def set_eggs(self, table):
      self.eggs = table


def objective_function(basket, K):
   points = 0
   M = len(basket.eggs)
   for i in range(len(basket.eggs)):
      nr_of_eggs = 0   
      for space in basket.eggs[i]:
         if space == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:         
               points -= 1
   for j in range(len(basket.eggs[0])):
      nr_of_eggs = 0                      #Sjekke diagonaler mangler
      for row in basket.eggs:
         if row[j] == 1:
            nr_of_eggs += 1
            if nr_of_eggs > K:         
               points -= 1
         
   for row in basket.eggs:
      for j in range(len(basket.eggs[0])):
         if row[j] == 1:
            points += 1                       # maks (N+M)*2   
   if points < 0:
      return 0   
   return float(points)/(M*K) 


 
def find_nabo(basket):      
      random.seed()                       # Maa ha krav til godkjent endring. 
      nabo = Basket(basket.N,basket.M)
      nabo.eggs = basket.eggs
      x = random.randrange(len(basket.eggs))
      y = random.randrange(len(basket.eggs[0]))
      if basket.eggs[x][y] == 1:
         nabo.eggs[x][y] = 0
      else:
         nabo.eggs[x][y] = 1
      return nabo

P = Basket(3,3)
q = []
q.append([1,0,1])
q.append([0,1,0])
q.append([1,0,0])
P.set_eggs(q)

print "P before new neighbor"
print  P.eggs
print objective_function(P,1)


