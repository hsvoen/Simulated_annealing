import random 

class Basket:
   N = 0
   M = 0
   #eggs = []   
   def __init__(self, n,m):
      self.M = m
      self.N = n
      self.eggs = []      

   def set_eggs(self, table):
      self.eggs = table

   def init_start_eggs(self):
      row = [0]*self.N
      for i in range(self.M):
         
         self.eggs.append(list(row))


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
            points += 1                        
   if points < 0:
      return 0   
   return float(points)/(M*K) #N = M i alle oppgavene


 
def find_nabo(basket):      
      print "Find nabo called"
      random.seed()                       # Maa ha krav til godkjent endring. 
      
      print "input argument"
      print basket.eggs

      nabo = Basket(basket.N,basket.M)

      for egg in basket.eggs:

         nabo.eggs.append(list(egg))
      x = random.randrange(len(basket.eggs))
      y = random.randrange(len(basket.eggs[0]))    # forslag 1: ikke lov aa plassere egg som bryter regler. 
      if nabo.eggs[x][y] == 1:                   # 2: skjekk om obj funksjon ooker: hvis ja: Coolio, hvis nei, sjanse for aa ikke akseptere og proove paa nytt. 
         nabo.eggs[x][y] = 0                       # 3: Legge inn for at egg flyttes fremfor aa fjaernes? slik at de kun fjaernes om det ikke finnes lovlige flytt. (egget som "bryter" flest regler? ) 
      else:                                       # 4: mulig med en funskjon som finner lovelige plasseringer?
         nabo.eggs[x][y] = 1    
      return nabo


   


p = Basket(3,3)
p.init_start_eggs()
for i in range(p.N):
   for j in range(p.M):
      p.eggs[i][j] = random.randrange(2)


print "P before new neighbor"
print  p.eggs
P1 = find_nabo(p)
print "P1:"
print P1.eggs
print "P after new neighbor"
print p.eggs


print objective_function(p,1)


