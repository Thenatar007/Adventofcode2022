import fileinput
array = []
elfcal= []
counter = 0
temp = 0
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Advent Input.txt")
for line in file_input:
    array.append(line)
    counter = counter + 1
file_input.close()
print("closed file \n")
counter=0

while counter < len(array)-1:
    print(counter)
    
    if array[counter] != '\n':
        temp = temp +int (array[counter])
        print(temp)
        counter = counter + 1
    if array[counter] == '\n':
        elfcal.append(temp)
        temp = 0
        counter = counter + 1 
        print("added number to elfcal \n")

elfcal.sort()
print ("this is the highest amount of calories :")
print (elfcal[len(elfcal)-1])

temp = 0
temp = elfcal[len(elfcal)-1] + elfcal[len(elfcal)-2] + elfcal[len(elfcal)-3]
print(temp) 
