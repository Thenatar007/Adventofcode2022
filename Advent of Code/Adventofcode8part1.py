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
    #start from the edge, if each num is less than the one before go to next, if it gets to the 
    visible = True 
    orig = twodarray[y][x]
    changed = False
    tallest = twodarray[y][x]
    for y in range (y):
      current = twodarray[y][x]
      #print(current)
      if  twodarray[y][x] >= tallest:
          tallest = twodarray[y][x]
          visible = False
          changed = True
    if orig == tallest and changed == False:
         visible = True  
    return visible

def checksouth(x, y):
    visible = True
    orig = twodarray[y][x]
    tallest = twodarray[y][x]
    changed = False
    counters = y+1
    while counters < len(twodarray):
        current = twodarray[counters][x]
        #print(current)
        if twodarray[counters][x] >= tallest:
          tallest = twodarray[counters][x]
          visible = False
          changed = True
          counters += 1
        else: counters +=1
    if orig == tallest and changed == False:
         visible = True   
    return visible

def checkeast(x, y):
    visible = True
    orig = twodarray[y][x]
    changed = False
    tallest = twodarray[y][x]
    for x in range (x):
      current = twodarray[y][x]
      #print(current)
      if  twodarray[y][x] >= tallest:
          tallest = twodarray[y][x]
          visible = False
          changed = True
    if orig == tallest and changed == False:
         visible = True
    return visible

def checkwest(x,y):
    visible = True
    counters = x+1
    changed = False
    orig = twodarray[y][x]
    tallest = twodarray[y][x]
    while counters <len(twodarray):
        current = twodarray[y][counters]
        #print(current)
        if twodarray[y][counters] >= tallest:
          tallest = twodarray[y][counters]
          visible = False
          changed = True
          counters +=1
        else: counters +=1
    if orig == tallest and changed == False:
         visible = True    
    return visible

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

for i in range (len(twodarray)):
    for j in range(len(twodarray[0])):
        if (i == 0) or (i == len(twodarray)-1) or (j == 0 ) or j == (len(twodarray[0])-1):
            counter += 1
        elif checknorth(j,i) == True or checkeast(j,i) == True or checksouth(j,i) == True or checkwest(j,i) == True:
           counter +=1

end = time.time()

print(end-start)
print(counter)
'''
put all chars into 2d array
for each char in the array

if it is at x = 0 or y = 0 or y = len-1 or x = len -1
add to counter

if not check if all numbers above are lower( all y less than the current y)
if number above higher, check left (all x less than current x)
if left higher, check right,(all x more than current x)
if right higher check down ( all y more than current y)
if up left right or down lower, add to counter
'''
