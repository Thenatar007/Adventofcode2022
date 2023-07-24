import fileinput
import re
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
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Adventinput4.txt")
for line in file_input:
    array.append(line)
   
file_input.close()
print("closed file \n")
counter=0

def are_pairs_containing(pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    min1, max1 = pair1
    print(pair1,pair2)
    min2, max2 = pair2
    return (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2)




while counter < (len(array)):
    temp = array[counter]
    #print(temp)
    temp = array[counter].split("\n")
    #print(temp)
    temp = temp[0]
    temp = temp.split(",")
    firsthalf=temp[0]

    secondhalf = temp[1]

    firststring = firsthalf.split("-")
   # print(firststring)
    secondstring = secondhalf.split("-")
   # print(secondstring)
    counter += 1
    if (are_pairs_containing(firststring, secondstring)):
        
     points +=1
print ("these are the points:")
print(points)
