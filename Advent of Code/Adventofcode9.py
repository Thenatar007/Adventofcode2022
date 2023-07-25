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
    if ((tail[0] == head[0]+1 and tail[1]==head[1]) or (tail[0]+1 == head[0] and tail[1]==(head[1]+1)) or (tail[0] == head[0]+1 and tail[1]==(head[1]-1))):
        tailnearhead = 1
    if ((tail[0] == head[0]-1 and tail[1]==head[1]) or (tail[0] == head[0]-1 and tail[1]==(head[1]+1)) or (tail[0] == head[0]-1 and tail[1]==(head[1]-1))):
        tailnearhead = 1
    return tailnearhead

def update(tail):
    name = str(tail[0]) + 'x' +str(tail[1])
    dict[name] = 1

file_input.close()
head = [0 , 0]
tail = [0, 0]
for move in array:
    move.replace("\n", "")
    move = move.split(" ")
    direction = move[0]
    distance =int( move[1])
    if (direction == 'R'):
        while distance > 0:
            head[0] += 1
            if tailcheck(head, tail) == 0:
                tail[0] = head[0]
                tail[1] = head[1]
                tail[0] -=1
                update(tail)
            distance -= 1

    elif (direction == 'L'):
        while distance > 0:
            head[0] -= 1
            if tailcheck(head, tail) == 0:
                tail[0] = head[0]
                tail[1] = head[1]
                tail[0] -=1
                update(tail)
            distance -= 1
    elif (direction == 'U'):
        while distance > 0:
            head[1] += 1
            if tailcheck(head, tail) == 0:
                tail[0] = head[0]
                tail[1] = head[1]
                tail[1] -=1
                update(tail)
            distance -= 1
    elif (direction == 'D'):
        while distance > 0:
            head[1] -= 1
            if tailcheck(head, tail) == 0:
                tail[0] = head[0]
                tail[1] = head[1]
                tail[1] +=1
                update(tail)
            distance -= 1
total = 0
for entry in dict:
    total += 1

print(total)
