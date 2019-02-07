import sys
import pygame
import random
import string
screen = pygame.display.set_mode((1000, 700))
pygame.init()
pygame.display.set_caption("Function")
black = (0, 0 ,0)
white = (255, 255 ,255)
grey = (125, 125, 125)
red = (255, 0, 0)
font = pygame.font.SysFont("times", 21)
screen.fill(white)


numline0 = font.render(str(-100), 1, black)
screen.blit(numline0, (305, 360))
numline1 = font.render(str(-80), 1, black)
screen.blit(numline1, (375, 360))
numline2 = font.render(str(-60), 1, black)
screen.blit(numline2, (445, 360))
numline3 = font.render(str(-40), 1, black)
screen.blit(numline3, (515, 360))
numline4 = font.render(str(-20), 1, black)
screen.blit(numline4, (585, 360))
numline5 = font.render(str(0), 1, black)
screen.blit(numline5, (655, 360))
numline6 = font.render(str(20), 1, black)
screen.blit(numline6, (725, 360))
numline7 = font.render(str(40), 1, black)
screen.blit(numline7, (795, 360))
numline8 = font.render(str(60), 1, black)
screen.blit(numline8, (865, 360))
numline9 = font.render(str(80), 1, black)
screen.blit(numline9, (935, 360))
numline10 = font.render(str(100), 1, black)
screen.blit(numline10, (1005, 360))



numliney0 = font.render(str(100), 1, black)
screen.blit(numliney0, (655, 0))
numliney0 = font.render(str(100), 1, black)
screen.blit(numliney0, (655, 0))
numliney1 = font.render(str(80), 1, black)
screen.blit(numliney1, (655, 70))
numliney2 = font.render(str(60), 1, black)
screen.blit(numliney2, (655, 140))
numliney3 = font.render(str(40), 1, black)
screen.blit(numliney3, (655, 210))
numliney4 = font.render(str(20), 1, black)
screen.blit(numliney4, (655, 280))
numliney6 = font.render(str(-20), 1, black)
screen.blit(numliney6, (655, 420))
numliney7 = font.render(str(-40), 1, black)
screen.blit(numliney7, (655, 490))
numliney8 = font.render(str(-60), 1, black)
screen.blit(numliney8, (655, 560))
numliney9 = font.render(str(-80), 1, black)
screen.blit(numliney9, (655, 630))
numliney10 = font.render(str(-100), 1, black)
screen.blit(numliney10, (655, 700))




b = 0
a = 0
for a in range (10):
    pygame.draw.line(screen, grey, (300, b ), (1000, b), 1)  # horizontal
    b += 70
a = 0
b = 300
for a in range (10):
    pygame.draw.line(screen, grey, (b, 0), (b, 700), 1)  # vertical

    b += 70


avalues = []
bvalues = []
cvalues = []
yvalues = []
realyvalues = []
realxvalues = []
lettersss= []
lettersss.append(random.choice(string.letters))
yvalue = 0
zero1 = 0
zero2 = 0
zero3 = 0
zero4 = 0
vf = True
count = 0
circley = 20


pygame.display.update()
while vf:
    numberoffunctions = int(input("Number of functions (max 6)"))
    if numberoffunctions <= 6:
        vf = False

print("ax^2+bx+c")
print("This program can only draw constant functions, linear functions and quadratics. ")
for zero1 in range(numberoffunctions):
    avalues.append(int(input("what is the value of a"+ str(zero1)+ " ")))
    bvalues.append(int(input("what is the value of b"+ str(zero1)+ " ")))
    cvalues.append(int(input("what is the value of c"+ str(zero1)+ " ")))
zero1 = -100
zero2 = 0
zero3 = 0
zero4 = 0
for zero2 in range(numberoffunctions):
    zero3 = -100
    zero1 = 0
    for zero1 in range(201):
        yvalue = (avalues[zero2]) * zero3 * zero3 + bvalues[zero2] * zero3 + cvalues[zero2]
        yvalues.append(yvalue)
        zero3 += 1
zero2 = 0
zero3 = 0
zero4= 0
zero5= 0
functiony = 10
vf = True
for zero2 in range(numberoffunctions-1):
    newletter = random.choice(string.letters)
    while vf:
        if lettersss[zero5] == newletter:
            newletter = random.choice(string.letters)
            count = 0
            zero5 = -1

        if (lettersss[zero5]) != (newletter):
            count += 1
        if count == len(lettersss):
            lettersss.append(newletter)
            newletter = random.choice(string.letters)
            count = 0
            zero5 = -1
        if len(lettersss) == numberoffunctions:
            vf = False

        zero5 += 1
    zero5 = 0
    count = 0

    vf = True




for zero2 in range(numberoffunctions):
    zero1 = 0
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))



    if avalues[zero2]!= 0 and bvalues[zero2]!= 0 and cvalues[zero2]!= 0:
        numline = font.render((lettersss[zero2]+ "(x) = " + str(avalues[zero2])+ "x^2 + " + str(bvalues[zero2]) + "x + "+ str(cvalues[zero2])), 1, black)
    if avalues[zero2]== 0 and bvalues[zero2]!= 0 and cvalues[zero2]!= 0:
        numline = font.render((lettersss[zero2]+ "(x) = " + str(bvalues[zero2]) + "x + "+ str(cvalues[zero2])), 1, black)
    if avalues[zero2]!= 0 and bvalues[zero2]== 0 and cvalues[zero2]!= 0:
        numline = font.render((lettersss[zero2]+ "(x) = " + str(avalues[zero2])+ "x^2 + " + str(cvalues[zero2])), 1, black)
    if avalues[zero2]!= 0 and bvalues[zero2]!= 0 and cvalues[zero2]== 0:
        numline = font.render((lettersss[zero2]+ "(x) = " + str(avalues[zero2]+ "x^2 + " + str(bvalues[zero2]) + "x")), 1, black)
    if avalues[zero2] == 0 and bvalues[zero2] == 0 and cvalues[zero2] != 0:
        numline = font.render((lettersss[zero2] + "(x) = " + str(cvalues[zero2])), 1, black)
    if avalues[zero2] == 0 and bvalues[zero2] != 0 and cvalues[zero2] == 0:
        numline = font.render((lettersss[zero2]+ "(x) =" + str(bvalues[zero2]) + "x" ), 1, black)
    if avalues[zero2] != 0 and bvalues[zero2] == 0 and cvalues[zero2] == 0:
        numline = font.render((lettersss[zero2]+ "(x) =" + str(avalues[zero2]) + "x^2 "), 1, black)




    pygame.draw.circle(screen, color, (250,circley),10)

    screen.blit(numline, (10, functiony))
    functiony += 100
    circley += 98





    for zero1 in range(201):
        if yvalues[zero4] < 0:
            realyvalues.append(350 + yvalues[zero4] * -3.5)
        if yvalues[zero4] > 0:
            realyvalues.append(350 - yvalues[zero4] * 3.5)
        if yvalues[zero4] == 0:
            realyvalues.append(350)
        if zero1 < 100:
            realxvalues.append(650 - (zero1-100) * -3.5)
        if zero1 > 100:
            realxvalues.append(650 + (zero1-100) * 3.5)
        if zero1 == 100:
            realxvalues.append(650)
        if zero3 > 0:
            pygame.draw.line(screen, color, (realxvalues[zero3-1], realyvalues[zero3-1]), (realxvalues[zero3], realyvalues[zero3]), 3)
            pygame.display.update()
        zero3+= 1
        zero4+=1





pygame.display.update()




while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()