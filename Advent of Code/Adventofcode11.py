import math
global onecount
onecount = 0
global twocount
twocount = 0
global threecount
threecount = 0
global zerocount
zerocount = 0
global fourcount
fourcount = 0
global fivecount
fivecount = 0
global sixcount
sixcount = 0
global sevencount
sevencount = 0
monkey0 = [56, 56, 92, 65, 71, 61, 79]
monkey1 = [61, 85]
monkey2 = [54, 96, 82, 78, 69]
monkey3 = [57, 59, 65, 95]
monkey4 = [62, 67, 80]
monkey5 = [91]
monkey6 = [79, 83, 64, 52, 77, 56, 63, 92]
monkey7 = [50, 97, 76, 96, 80, 56]
product = 3 * 11 * 7* 19* 5* 17 * 13
def monkey0function():
    global zerocount
    while len(monkey0) > 0:
        
        item = monkey0.pop(0)
        item = item * 7
       
        if item % product == 0:
            monkey3.append(item)
        else:
            monkey7.append(item)
        zerocount += 1
            
def monkey1function():
    global onecount
    while len(monkey1) > 0:
        item = monkey1.pop(0)
        item = item + 5
        
        if item % product == 0:
            monkey6.append(item)
        else:
            monkey4.append(item)
        onecount += 1
        
def monkey2function():
    global twocount
    while len(monkey2) > 0:
        item = monkey2.pop(0)
        item = item * item
        
        if item % product == 0:
            monkey0.append(item)
        else:
            monkey7.append(item)
        twocount += 1   
            
def monkey3function():
    global threecount
    while len(monkey3) > 0:
        item = monkey3.pop(0)
        item = item + 4
        
        if item % product == 0:
            monkey5.append(item)
        else:
            monkey1.append(item)
        threecount+= 1

def monkey4function():
    global fourcount
    while len(monkey4) > 0:
        
        item = monkey4.pop(0)
        item = item * 17
        
        if item % product == 0:
            monkey2.append(item)
        else:
            monkey6.append(item)
        fourcount += 1
            
def monkey5function():
    global fivecount
    while len(monkey5) > 0:
        item = monkey5.pop(0)
        item = item + 7
        
        if item % product == 0:
            monkey1.append(item)
        else:
            monkey4.append(item)
        fivecount += 1
        
def monkey6function():
    global sixcount
    while len(monkey6) > 0:
        item = monkey6.pop(0)
        item = item + 6
        
        if item % product == 0:
            monkey2.append(item)
        else:
            monkey0.append(item)
        sixcount += 1   
            
def monkey7function():
    global sevencount
    while len(monkey7) > 0:
        item = monkey7.pop(0)
        item = item + 3
        
        if item % product == 0:
            monkey3.append(item)
        else:
            monkey5.append(item)
        sevencount+= 1
for y in range (10000):
    for x in range(20):
        monkey0function()
        monkey1function()
        monkey2function()
        monkey3function()
        monkey4function()
        monkey5function()
        monkey6function()
        monkey7function()

print('zero')    
print(zerocount)
print('one')    
print(onecount)
print('two')    
print(twocount)
print('three')    
print(threecount)
print('four')    
print(fourcount)
print('five')    
print(fivecount)
print('six')    
print(sixcount)
print('seven')    
print(sevencount)