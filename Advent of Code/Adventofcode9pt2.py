array = []
dict = {}

file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Adventinput9.txt")
for line in file_input:
    array.append(line)
   # print(line)
def tailcheck(head, tail):
    tailnearhead = 0
    if ((tail[0] == head[0] and tail[1]==head[1]) or (tail[0] == head[0] and tail[1]==(head[1]+1)) or (tail[0] == head[0] and tail[1]==(head[1]-1))):
        tailnearhead = 1
    if ((tail[0] == head[0]+1 and tail[1]==head[1]) or (tail[0] == head[0]+1 and tail[1]==(head[1]+1)) or (tail[0] == head[0]+1 and tail[1]==(head[1]-1))):
        tailnearhead = 1
    if ((tail[0] == head[0]-1 and tail[1]==head[1]) or (tail[0] == head[0]-1 and tail[1]==(head[1]+1)) or (tail[0] == head[0]-1 and tail[1]==(head[1]-1))):
        tailnearhead = 1
    return tailnearhead

def update(tail):
    name = str(tail[0]) + 'x' +str(tail[1])
    dict[name] = 1

file_input.close()
head = [0 , 0]
knot1 = [0 , 0]
knot2= [0 , 0]
knot3= [0 , 0]
knot4= [0 , 0]
knot5= [0 , 0]
knot6= [0 , 0]
knot7= [0 , 0]
knot8= [0 , 0]
tail = [0, 0]

def checkropel():
    if tailcheck(head, knot1) == 1:
        knot1[0] = head[0]
        knot1[1] = head[1]
        knot1[0] -=1
        if tailcheck(knot1, knot2) == 1:
            knot2[0] = knot1[0]
            knot2[1] = knot1[1]
            knot2[0] -=1 
            if tailcheck(knot2, knot3) == 1:
                knot3[0] = knot2[0]
                knot3[1] = knot2[1]
                knot3[0] -=1
                if tailcheck(knot3, knot4) == 1:
                    knot4[0] = knot3[0]
                    knot4[1] = knot3[1]
                    knot4[0] -=1
                    if tailcheck(knot4, knot5) == 1:
                        knot5[0] = knot4[0]
                        knot5[1] = knot4[1]
                        knot5[0] -=1 
                        if tailcheck(knot5, knot6) == 1:
                            knot6[0] = knot5[0]
                            knot6[1] = knot5[1]
                            knot6[0] -=1
                            if tailcheck(knot6, knot7) == 1:
                                knot7[0] = knot6[0]
                                knot7[1] = knot6[1]
                                knot7[0] -=1
                                if tailcheck(knot7, knot8) == 1:
                                    knot8[0] = knot7[0]
                                    knot8[1] = knot7[1]
                                    knot8[0] -=1 
                                    if tailcheck(knot8, tail) == 1:
                                        tail[0] = knot8[0]
                                        tail[1] = knot8[1]
                                        tail[0] -=1
                                        update(tail)
                            
for move in array:
    move.replace("\n", "")
    move = move.split(" ")
    direction = move[0]
    distance =int( move[1])
    if (direction == 'R'):
        while distance > 0:
            head[0] += 1
            #for each knot, do a tail check
            '''
            basically
            
            if head, 1
                if 1, 2
                etc until
                    if 8,9
                    update(tail)
            
            '''
            checkropel()
            distance -= 1

    elif (direction == 'L'):
        while distance > 0:
            head[0] -= 1
            
            checkropel()
            distance -= 1
    elif (direction == 'U'):
        while distance > 0:
            head[1] += 1
            checkropel()
            distance -= 1
    elif (direction == 'D'):
        while distance > 0:
            head[1] -= 1
            checkropel()
            distance -= 1
total = 0
for entry in dict:
    total += 1

print(total)