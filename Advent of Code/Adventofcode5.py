import fileinput
array = []
points= 0
counter = 0
numofmoves = 0
removestack = 0
placestack = 0
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Adventinput5.txt")
for line in file_input:
    array.append(line)
   # print(line)
file_input.close()
print("closed file \n")
counter=0
arrayofstacks = []
stack =['F', 'd', 'b', 'z', 't', 'j' , 'r', 'n']
arrayofstacks.append(stack)
stack =['r', 's', 'n', 'j', 'h']
arrayofstacks.append(stack)
stack =['c', 'r', 'n', 'j', 'g', 'z' , 'f', 'q']
arrayofstacks.append(stack)
stack =['f', 'v', 'n', 'g', 'r', 't' , 'q']
arrayofstacks.append(stack)
stack =['l', 't', 'q', 'f']
arrayofstacks.append(stack)
stack =['q', 'c', 'w', 'z', 'b', 'r' , 'g', 'n']
arrayofstacks.append(stack)
stack =['f', 'c', 'l', 's', 'n', 'h' , 'm']
arrayofstacks.append(stack)
stack =['d', 'n', 'q', 'm', 't', 'j' ]
arrayofstacks.append(stack)
stack =['p', 'g', 's']
arrayofstacks.append(stack)
#for each line do the move requested, then display the entire stack
for moves in array:
    move = moves.split("\n")
    move = move[0].split(" ")
    numofmoves = move[0]
    removestack = move[1]
    placestack = move[2]
    i = 0
    tempstack1 = arrayofstacks[int(removestack)-1]
    tempstack2= arrayofstacks[int(placestack)-1]
    print("number of moves " + numofmoves)
    print ("before " )
    print(tempstack1)
    print ("before " )
    print(tempstack2)
    while i < int(numofmoves):
        
        tempstack2.append(tempstack1.pop())

        i+=1
    arrayofstacks[int(removestack)-1] = tempstack1
    arrayofstacks[int(placestack)-1] = tempstack2
    print ("after ")
    print(tempstack1)
    print ("after ")
    print(tempstack2)
for x in arrayofstacks:
    print(x.pop())




array = []
points= 0
counter = 0
numofmoves = 0
removestack = 0
placestack = 0
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Adventinput5.txt")
for line in file_input:
    array.append(line)
   # print(line)
file_input.close()
print("closed file \n")
counter=0
arrayofstacks = []
stack =['F', 'd', 'b', 'z', 't', 'j' , 'r', 'n']
arrayofstacks.append(stack)
stack =['r', 's', 'n', 'j', 'h']
arrayofstacks.append(stack)
stack =['c', 'r', 'n', 'j', 'g', 'z' , 'f', 'q']
arrayofstacks.append(stack)
stack =['f', 'v', 'n', 'g', 'r', 't' , 'q']
arrayofstacks.append(stack)
stack =['l', 't', 'q', 'f']
arrayofstacks.append(stack)
stack =['q', 'c', 'w', 'z', 'b', 'r' , 'g', 'n']
arrayofstacks.append(stack)
stack =['f', 'c', 'l', 's', 'n', 'h' , 'm']
arrayofstacks.append(stack)
stack =['d', 'n', 'q', 'm', 't', 'j' ]
arrayofstacks.append(stack)
stack =['p', 'g', 's']
arrayofstacks.append(stack)
#pt 2
for moves in array:
    move = moves.split("\n")
    move = move[0].split(" ")
    numofmoves = move[0]
    removestack = move[1]
    placestack = move[2]
    i = 0
    tempstack1 = arrayofstacks[int(removestack)-1]
    tempstack2= arrayofstacks[int(placestack)-1]
    tempstack3 =[]
    print("number of moves " + numofmoves)
    print ("before " )
    print(tempstack1)
    print ("before " )
    print(tempstack2)
    while i < int(numofmoves):

        tempstack3.append(tempstack1.pop())

        i+=1
    print("temp stack 3")
    print(tempstack3)
    i = 0
    while not len(tempstack3) == 0:
        tempstack2.append(tempstack3.pop())
    arrayofstacks[int(removestack)-1] = tempstack1
    arrayofstacks[int(placestack)-1] = tempstack2
    print(tempstack3)
    print ("after ")
    print(tempstack1)
    print ("after ")
    print(tempstack2)
for x in arrayofstacks:
    print(x.pop())
