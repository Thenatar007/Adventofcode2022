array = []
line1 = [None]*40
line2 = [None]*40
line3 = [None]*40
line4 = [None]*40
line5 = [None]*40
line6 = [None]*40

global yreg
yreg = 1
global operationcount
operationcount= 1
global sumoffrequencies
sumoffrequencies = 0
global pixelcount
pixelcount = 0
def checkcounter():
    global sumoffrequencies
    global yreg
    if operationcount == 20:
        sumoffrequencies += 20*yreg
        print(20*yreg)
    elif operationcount == 60:
        sumoffrequencies += 60*yreg
        print(60*yreg)
    elif operationcount == 100:
        sumoffrequencies += 100*yreg
        print(100*yreg)
    elif operationcount == 140:
        sumoffrequencies += 140*yreg
        print(140*yreg)
    elif operationcount == 180:
        sumoffrequencies += 180*yreg
        print(180*yreg)
    elif operationcount == 220:
        sumoffrequencies += 220*yreg
        print(220*yreg)
def addx(num):
    global operationcount
    global yreg
    drawpixel()
    operationcount +=1
    checkcounter()
    drawpixel()
    operationcount +=1
    yreg += num
    checkcounter()
    
    
def drawpixel():
    global pixelcount
    global yreg
    
    if pixelcount <40:
        if (yreg -1 == pixelcount) or (yreg == pixelcount) or (yreg +1 == pixelcount):
            line1[pixelcount] = "#"
        else:
            line1[pixelcount] = "."
    if pixelcount >= 40 and pixelcount <80:
        if (yreg -1 == pixelcount-40) or (yreg == pixelcount-40) or (yreg +1 == pixelcount-40):
            line2[pixelcount-40] = "#"
        else:
            line2[pixelcount-40] = "."
    if pixelcount >= 80 and pixelcount <120:
        if (yreg -1 == pixelcount-80) or (yreg == pixelcount-80) or (yreg +1 == pixelcount-80):
            line3[pixelcount-80] = "#"
        else:
            line3[pixelcount-80] = "."
    if pixelcount >=120 and pixelcount <160:
        if (yreg -1 == pixelcount-120) or (yreg == pixelcount-120) or (yreg +1 == pixelcount-120):
            line4[pixelcount-120] = "#"
        else:
            line4[pixelcount-120] = "."
    if pixelcount >=160 and pixelcount <200:
        if (yreg -1 == pixelcount-160) or (yreg == pixelcount-160) or (yreg +1 == pixelcount-160):
            line5[pixelcount-160] = "#"
        else:
            line5[pixelcount-160] = "."
    if pixelcount >= 200 and pixelcount <240:
        if (yreg -1 == pixelcount-200) or (yreg == pixelcount-200) or (yreg +1 == pixelcount-200):
            line6[pixelcount-200] = "#"
        else:
            line6[pixelcount-200] = "."
    pixelcount += 1
    
    
    
    
    
    
file_input = open("C:\\Users\E1416669\Desktop\Advent of code\AdventInput10.txt")
for line in file_input:
    array.append(line)
   
file_input.close()



for command in array:
    
    if command.find("noop") >= 0:
        drawpixel()
        operationcount += 1
        checkcounter()
        
        continue
    elif command.find("addx") >=0:
        command = command.split(' ')
        number = int(command[1])
        addx(number)
        
print(sumoffrequencies)
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)


#basically
#sprite starts at 012
#pixel 0 is a # op1 start add

#if add, Pixel 1 is a # op2
#if add pixel 2 is a . as add has ended and the sprite has moved.
#everywhere there is a check counter, add a draw pixel