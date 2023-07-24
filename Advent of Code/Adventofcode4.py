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
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Adventinput4.txt")
for line in file_input:
    array.append(line)
   
file_input.close()
print("closed file \n")
counter=0




while counter < (len(array)):
    temp = array[counter]
    temp = array[counter].split("\n")
    temp = temp[0]
    temp = temp.split(",")
    firsthalf=temp[0]
    secondhalf = temp[1]
    print(secondhalf)
    firststring = firsthalf.split("-")
    print(firststring)
    secondstring = secondhalf.split("-")
   # print(secondstring)
    counter = counter +1
   # print("Points before")
   # print(points)
    min1,max1 = firststring
    min2,max2 = secondstring
    if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
        points = points+1
    else:
        points = points
   # print("points after")
   # print(points)
print ("these are the points:")
print(points)
'''
counter = 0
points = 0
while counter < (len(array)):
    temp = array[counter]
    temp = array[counter].split("\n")
    temp = temp[0]
    temp = temp.split(",")
    firsthalf=temp[0]
    secondhalf = temp[1]
    firststring = firsthalf.split("-")
   # print(firststring)
    secondstring = secondhalf.split("-")
   # print(secondstring)
    counter = counter +1
   # print("Points before")
   # print(points)
    min1,max1 = firststring
    min2,max2 = secondstring
    if( min1<= min2 <= max1 or min2<= min1 <= max2):
        points = points + 1
    print(points)
'''
