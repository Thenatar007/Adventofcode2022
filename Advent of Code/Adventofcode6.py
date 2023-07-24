import fileinput
array = []
array2=[]
points= 0
counter = 0
var1 = 0
var2 = 1
var3 = 2
var4 = 3
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\Adventinput6.txt")
for line in file_input:
    for char in line:
        array.append(char)
file_input.close()
'''
def comparechars(a, b, c, d):
    if a == b or a == c or a == d:
        return False
    elif b == c or b == d:
        return False
    elif c == d:
        return False
    else:
        return True
    
#check four characters at a time for repeats, abcd then shift input by 1 so bcde etc until 4 characters are different
charbool = False
while counter < len(array) and charbool == False:
    char1 = array[counter]
    char2 = array[counter+1]
    char3 = array[counter+2]
    char4 = array[counter+3]
    charbool = comparechars(char1, char2, char3, char4)
    counter +=1

print(counter+3)
'''
def comparechars2(array):
    i = 0
    j = 0
    ret = True
    #while i < 14
    #check i against all other variables where you start checking at i+1 until len of array
    while i<14:
        chari = array[i]
        j = i + 1
        while j < 14:
            charj = array[j]
            if chari == charj:
                ret = False
            j+=1
        i+=1
    return ret
#check four characters at a time for repeats, abcd then shift input by 1 so bcde etc until 4 characters are different
counter = 0
charbool = False
while counter < len(array) and charbool == False:
    i = 0
    while i < 14 and (counter+i) < len(array):
        array2.append(array[counter+i])
        i+=1
    print(array2)
    charbool = comparechars2(array2)
    counter +=1
    array2 = []
print(counter+13)
