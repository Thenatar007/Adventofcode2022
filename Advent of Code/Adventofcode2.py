import fileinput
array = []
arrayline = []
points= 0
counter = 0
string1 = ""
string2 = ""
temp = ""
a = 1
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Advent input3.txt")
for line in file_input:
    array.append(line)
   
file_input.close()
print("closed file \n")
counter=0
def compare(a,b):
    for x in a:
        for y in b:
            if x==y:
                return x
    
while counter <= len(array):
    temp = array[counter]
    comp = ""
    counter = counter + 1
    string1 = temp[0:len(temp)//2]
    string2 = temp[len(temp) //2 if len(temp)% 2 == 0 else ((len(temp)//2)+1): ]
    comp = compare(string1, string2)
    if comp != "":
        points = comp
