import fileinput
array = []
points= 0
counter = 0
temp = ""
firsthalf =""
secondhalf = ""
firststring = ""
secondstring = ""
thirdstring = ""
retval = ""
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Advent input3.txt")
for line in file_input:
    array.append(line)
   
file_input.close()
print("closed file \n")
counter=0
def compare (firststring, secondstring) :
     for element in range(0,len(firststring)):
        for element2 in range(0,len(secondstring)):
            if firststring[element] == secondstring[element2]:
                return firststring[element]

def compare3 (firststring, secondstring, thirdstring) :
     for element in range(0,len(firststring)):
        for element2 in range(0,len(secondstring)):
            for element3 in range (0,len(thirdstring)):
                if firststring[element] == secondstring[element2]== thirdstring[element3]:
                    return firststring[element]

            
while counter < (len(array)):
    temp = array[counter]
    stringlen= len(temp)
    counter = counter + 1
    firsthalf = slice (0, stringlen//2)
    secondhalf = slice (stringlen//2, stringlen)
    firststring = temp[firsthalf]
    secondstring = temp[secondhalf]
    retval = compare(firststring, secondstring)

    if retval == "a":
        points = points + 1
    elif retval == "b":
        points = points + 2
    elif retval == "c":
        points = points + 3

    elif retval == "d":
        points = points + 4
    elif retval == "e":
        points = points + 5
    elif retval == "f":
        points = points + 6
    elif retval == "g":
        points = points + 7
    elif retval == "h":
        points = points + 8
    elif retval == "i":
        points = points + 9
    elif retval == "j":
        points = points + 10
    elif retval == "k":
        points = points + 11
    elif retval == "l":
        points = points + 12
    elif retval == "m":
        points = points + 13
    elif retval == "n":
        points = points + 14
    elif retval == "o":
        points = points + 15
    elif retval == "p":
        points = points + 16
    elif retval == "q":
        points = points + 17
    elif retval == "r":
        points = points + 18
    elif retval == "s":
        points = points + 19
    elif retval == "t":
        points = points + 20
    elif retval == "u":
        points = points + 21
    elif retval == "v":
        points = points + 22
    elif retval == "w":
        points = points + 23
    elif retval == "x":
        points = points + 24
    elif retval == "y":
        points = points + 25
    elif retval == "z":
        points = points + 26
    elif retval == "A":
        points = points + 1 + 26
    elif retval == "B":
        points = points + 2 + 26
    elif retval == "C":
        points = points + 3 + 26

    elif retval == "D":
        points = points + 4+ 26
    elif retval == "E":
        points = points + 5+ 26
    elif retval == "F":
        points = points + 6+ 26
    elif retval == "G":
        points = points + 7+ 26
    elif retval == "H":
        points = points + 8+ 26
    elif retval == "I":
        points = points + 9+ 26
    elif retval == "J":
        points = points + 10+ 26
    elif retval == "K":
        points = points + 11+ 26
    elif retval == "L":
        points = points + 12+ 26
    elif retval == "M":
        points = points + 13+ 26
    elif retval == "N":
        points = points + 14+ 26
    elif retval == "O":
        points = points + 15+ 26
    elif retval == "P":
        points = points + 16+ 26
    elif retval == "Q":
        points = points + 17+ 26
    elif retval == "R":
        points = points + 18+ 26
    elif retval == "S":
        points = points + 19+ 26
    elif retval == "T":
        points = points + 20+ 26
    elif retval == "U":
        points = points + 21+ 26
    elif retval == "V":
        points = points + 22+ 26
    elif retval == "W":
        points = points + 23+ 26
    elif retval == "X":
        points = points + 24+ 26
    elif retval == "Y":
        points = points + 25+ 26
    elif retval == "Z":
        points = points + 26+ 26
     
print(points)

points = 0
counter = 0

while counter < (len(array)):
    temp = array[counter]
    temp2= array[counter+1]
    temp3 = array[counter+2]
    counter = counter + 3
    print(temp )
    print(temp2)
    print(temp3)
    retval= compare3 (temp, temp2, temp3)


    if retval == "a":
        points = points + 1
    elif retval == "b":
        points = points + 2
    elif retval == "c":
        points = points + 3

    elif retval == "d":
        points = points + 4
    elif retval == "e":
        points = points + 5
    elif retval == "f":
        points = points + 6
    elif retval == "g":
        points = points + 7
    elif retval == "h":
        points = points + 8
    elif retval == "i":
        points = points + 9
    elif retval == "j":
        points = points + 10
    elif retval == "k":
        points = points + 11
    elif retval == "l":
        points = points + 12
    elif retval == "m":
        points = points + 13
    elif retval == "n":
        points = points + 14
    elif retval == "o":
        points = points + 15
    elif retval == "p":
        points = points + 16
    elif retval == "q":
        points = points + 17
    elif retval == "r":
        points = points + 18
    elif retval == "s":
        points = points + 19
    elif retval == "t":
        points = points + 20
    elif retval == "u":
        points = points + 21
    elif retval == "v":
        points = points + 22
    elif retval == "w":
        points = points + 23
    elif retval == "x":
        points = points + 24
    elif retval == "y":
        points = points + 25
    elif retval == "z":
        points = points + 26
    elif retval == "A":
        points = points + 1 + 26
    elif retval == "B":
        points = points + 2 + 26
    elif retval == "C":
        points = points + 3 + 26

    elif retval == "D":
        points = points + 4+ 26
    elif retval == "E":
        points = points + 5+ 26
    elif retval == "F":
        points = points + 6+ 26
    elif retval == "G":
        points = points + 7+ 26
    elif retval == "H":
        points = points + 8+ 26
    elif retval == "I":
        points = points + 9+ 26
    elif retval == "J":
        points = points + 10+ 26
    elif retval == "K":
        points = points + 11+ 26
    elif retval == "L":
        points = points + 12+ 26
    elif retval == "M":
        points = points + 13+ 26
    elif retval == "N":
        points = points + 14+ 26
    elif retval == "O":
        points = points + 15+ 26
    elif retval == "P":
        points = points + 16+ 26
    elif retval == "Q":
        points = points + 17+ 26
    elif retval == "R":
        points = points + 18+ 26
    elif retval == "S":
        points = points + 19+ 26
    elif retval == "T":
        points = points + 20+ 26
    elif retval == "U":
        points = points + 21+ 26
    elif retval == "V":
        points = points + 22+ 26
    elif retval == "W":
        points = points + 23+ 26
    elif retval == "X":
        points = points + 24+ 26
    elif retval == "Y":
        points = points + 25+ 26
    elif retval == "Z":
        points = points + 26+ 26
print(points)
