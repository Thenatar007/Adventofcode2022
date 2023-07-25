import fileinput
import time

start = time.time()
array = []
array2=[]
twodarray = []
points= 0
counter = 0
var1 = 0
var2 = 1
var3 = 2
var4 = 3

def checknorth(x,y):
    scenic = 0
    foundtaller =0
    treeheight = twodarray[y][x]
    for z in range (y+1):
      #print(current)
      if (y - z) == y:
          continue
      if  twodarray[y-z][x] < treeheight and foundtaller == 0:
          scenic += 1
      elif twodarray[y-z][x] == treeheight and foundtaller == 0 :
        scenic += 1
        foundtaller = 1
      else:
          if foundtaller == 0:
             scenic += 1
          foundtaller = 1   
          
          
    return scenic      
    
    

def checksouth(x, y):
    scenic = 0
    foundtaller =0
    treeheight = twodarray[y][x]
    for z in range (len(twodarray)- y):
      #print(current)
      if (y + z) == y:
          continue
      if  twodarray[y+z][x] < treeheight and foundtaller == 0:
          scenic += 1
      elif twodarray[y+z][x] == treeheight and foundtaller == 0 :
        scenic += 1
        foundtaller = 1
      else:
          if foundtaller == 0:
             scenic += 1
          foundtaller = 1
          
          
    return scenic   

def checkeast(x, y):
    scenic = 0
    foundtaller =0
    treeheight = twodarray[y][x]
    for z in range (len(twodarray[y]) - x):
      #print(current)
      if (x + z) == x:
          continue
      if  twodarray[y][(x+z)] < treeheight and foundtaller == 0:
          scenic += 1
      elif twodarray[y][(x+z)] == treeheight and foundtaller == 0 :
        scenic += 1
        foundtaller = 1
      else: 
          if foundtaller == 0:
             scenic += 1
          foundtaller =1  
          
           
          
    return scenic      

def checkwest(x,y):
    scenic = 0
    foundtaller =0
    treeheight = twodarray[y][x]
    for z in range (x+1):
      #print(current)
      if (x - z) == x:
          continue
      if  twodarray[y][x-(z)] < treeheight and foundtaller == 0:
          scenic += 1
      elif twodarray[y][x-(z)] == treeheight and foundtaller == 0 :
        scenic += 1
        foundtaller = 1
      else: 
          if foundtaller == 0:
             scenic += 1   
          foundtaller = 1
      
    return scenic      
    

file_input = open("Advent of code\Adventinput8.txt")
for line in file_input:
    array.append(line)
   # print(line)
file_input.close()

for line in array:
    array2 = []
    line = line.split("\n")
    line = line[0]
    for char in line:
        array2.append(char)
    twodarray.append(array2)
highscore = 0
for i in range (len(twodarray)):
    for j in range(len(twodarray[0])):
        current = twodarray[i][j]
        tempscore = (checkeast(j,i) * checkwest(j,i) * checknorth(j,i) * checksouth(j,i) )
        if tempscore > highscore:
            highscore = tempscore

end = time.time()

print(end-start)
print(highscore)

