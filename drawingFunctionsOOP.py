import sys
import pygame
import random
import string


class Screen:         # Class to set up display
    def __init__(self):
        #color
        self.white = (255, 255, 255)

        # Display screen in 1000x700px and
        pygame.init ()
        self.screen = pygame.display.set_mode ((1000, 700))
        pygame.display.set_caption ("Function") #name display as Functions
        self.screen.fill (self.white) #background set to white



class Field(Screen):  # Class to set up xy coordinate system
    def __init__(self, Screen_Class): # Takes screen class as input
        #colors
        self.grey = (125, 125, 125)
        self.black = (0, 0, 0)

        self.screen = Screen_Class.screen # gets screen variable from Screen class

        self.num_array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.font = pygame.font.SysFont ("times", 21)


        #calls functions
        self.Write_Horizontal()
        self.Write_Vertical()
        self.Draw_Horizontal()
        self.Draw_Vertical()



    def Write_Horizontal(self):
        for zero1 in self.num_array:   # from -5 to 5,   writes all numbers on horizontal axis
            line_num = self.font.render (str (20 * zero1), 1, self.black) # sets text color and text that will be written
            self.screen.blit (line_num, (305 + (70 * (zero1 + 5)), 360)) # Displays the text at given loaction

    def Write_Vertical(self):
        for zero1 in self.num_array: # from -5 to 5,   writes all numbers on vertical axis
            if zero1 != 0: # at origin there is already a 0 written from Write_Horizontal function
                line_num = self.font.render (str (-20 * zero1), 1, self.black) # sets text color and text that will be written
                self.screen.blit (line_num, (655, (70 * (zero1 + 5)))) # Displays the text at given loaction

    def Draw_Vertical(self):
        x_position = 0
        for zero1 in range (10):
            pygame.draw.line (self.screen, self.grey, (300, x_position), (1000, x_position), 1)  # draws vertical lines on coordinate system at given position
            x_position += 70

    def Draw_Horizontal(self):
        y_position = 300
        for zero1 in range (10):
            pygame.draw.line(self.screen, self.grey, (y_position, 0), (y_position, 700), 1)  # draws horizontal lines on coordinate system at given position
            y_position += 70


class Functions(Screen, Field):
    def __init__(self, Screen_Class, Field_Class):

        self.avalues = []
        self.bvalues = []
        self.cvalues = []
        self.yvalues = [] #values according to real coordinate system
        self.realyvalues = [] #values according to pygame coordinate system
        self.realxvalues = [] #values according to pygame coordinate system
        self.lettersss= [] #name of the functions represented by letters
        self.lettersss.append(random.choice(string.letters))
        self.circley = 20 #color indicators radius next to the function name on the screen
        self.zero4 = 0
        self.zero3 = 0

        self.screen = Screen_Class.screen # gets screen variable from Screen class
        self.font = Field_Class.font # gets font variable from Field class
        self.black = Field_Class.black # gets black variable from Field class

        #calls functions
        self.Get_Number_Of_Functions()
        self.Get_Function_constants()
        self.Get_Points_Function()
        self.Function_Names()
        self.Write_Function_Name()



    def Get_Number_Of_Functions(self): #gets number of functions that is wanted to be draw
        vf = True
        while vf:
            self.numberoffunctions = int(input("Number of functions (max 6)"))
            if self.numberoffunctions <= 6 and self.numberoffunctions > 0:  #asks for input again if the number is higher than six or lower than 0
                vf = False
        print("ax^2+bx+c")
        print("This program can only draw constant functions, linear functions and quadratics. ")

    def Get_Function_constants(self): #gets constants for all values
        for zero1 in range(self.numberoffunctions): #runs number of times as functions to be drawn
            self.avalues.append(int(input("what is the value of a"+ str(zero1)+ " ")))  #asks for input and adds to avalues because it is a constant of a
            self.bvalues.append(int(input("what is the value of b"+ str(zero1)+ " ")))  #asks for input and adds to bvalues because it is a constant of b
            self.cvalues.append(int(input("what is the value of c"+ str(zero1)+ " ")))  #asks for input and adds to cvalues because it is a constant of c

    def Get_Points_Function(self):  #finds points on xy coordinate system, each point is found for x eual to -100 to 100 and x increases by 1, there is no need to store x values because
        # its values are know ( -100 to 100 )
        for zero2 in range(self.numberoffunctions): #makes this process for each function
            zero3 = -100 #start number of x
            zero1 = 0
            for zero1 in range(201):
                self.yvalue = (self.avalues[zero2]) * zero3 * zero3 + self.bvalues[zero2] * zero3 + self.cvalues[zero2] #finds the y value by putting x's value in x which is zero3
                # in this case and multiplys by its constants gathered from the user
                self.yvalues.append(self.yvalue) #adds the value found to the list
                zero3 += 1 #x increases by 1 each time

    def Function_Names(self):
        count = 0
        zero1= 0
        self.functiony = 10
        vf = True
        newletter = random.choice(string.letters)   #generate a letter
        while vf: #makes this process for each function -1 because first letter was found in init function, runs until it is known that new letter found is not same with another one
            if len(self.lettersss) == self.numberoffunctions:   #makes vf False because there is no need to find any more letters
                vf = False

            if self.lettersss[zero1] == newletter: # if new letter is same as a previously found letter then generates once again
                newletter = random.choice(string.letters)
                count = 0 #equal count ot 0 to start the comparing process again
                zero1 = -1

            if (self.lettersss[zero1]) != (newletter): # if letter is not same as the previously find letter at spesified index then adds count 1
                count += 1

            if count == len(self.lettersss): #if all letter previously found is compared to new letter and it is not same as any, then adds to list
                self.lettersss.append(newletter)
                newletter = random.choice(string.letters)
                count = 0
                zero1 = -1

            zero1 += 1


    def Write_Function_Name(self):

        for zero2 in range(self.numberoffunctions):  #runs number of times as functions to be drawn
            zero1 = 0
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))  #generates a random color


            #all of these if satets are written to write the function in correct syntax (by wrong syntax I mean 0x^2 + 0x +2)
            if self.avalues[zero2]!= 0 and self.bvalues[zero2]!= 0 and self.cvalues[zero2]!= 0: #if function is a quadratic such as 2x^2 + 2x +2
                numline = self.font.render((self.lettersss[zero2]+ "(x) = " + str(self.avalues[zero2])+ "x^2 + " + str(self.bvalues[zero2]) + "x + "+ str(self.cvalues[zero2])), 1,
                                           self.black)
            if self.avalues[zero2]== 0 and self.bvalues[zero2]!= 0 and self.cvalues[zero2]!= 0:    #if function is linear such as 2x +2
                numline = self.font.render((self.lettersss[zero2]+ "(x) = " + str(self.bvalues[zero2]) + "x + "+ str(self.cvalues[zero2])), 1, self.black)
            if self.avalues[zero2]!= 0 and self.bvalues[zero2]== 0 and self.cvalues[zero2]!= 0:     #if function is a quadratic such as 2x^2 +2
                numline = self.font.render((self.lettersss[zero2]+ "(x) = " + str(self.avalues[zero2])+ "x^2 + " + str(self.cvalues[zero2])), 1, self.black)
            if self.avalues[zero2]!= 0 and self.bvalues[zero2]!= 0 and self.cvalues[zero2]== 0:     #if function is a quadratic such as 2x^2 + 2x
                numline = self.font.render((self.lettersss[zero2]+ "(x) = " + str(self.avalues[zero2]+ "x^2 + " + str(self.bvalues[zero2]) + "x")), 1, self.black)
            if self.avalues[zero2] == 0 and self.bvalues[zero2] == 0: #if function is constant such as 2
                numline = self.font.render((self.lettersss[zero2] + "(x) = " + str(self.cvalues[zero2])), 1, self.black)
            if self.avalues[zero2] == 0 and self.bvalues[zero2] != 0 and self.cvalues[zero2] == 0:      #if function is a linear such as 2x
                numline = self.font.render((self.lettersss[zero2]+ "(x) =" + str(self.bvalues[zero2]) + "x" ), 1, self.black)
            if self.avalues[zero2] != 0 and self.bvalues[zero2] == 0 and self.cvalues[zero2] == 0:  #if function is a quadratic such as 2x^2
                numline = self.font.render((self.lettersss[zero2]+ "(x) =" + str(self.avalues[zero2]) + "x^2 "), 1, self.black)

            pygame.draw.circle(self.screen, self.color, (250, self.circley),10) #draws a circle next to the function name in order to indicate functions by color
            self.screen.blit(numline, (10, self.functiony)) #writes the function name found in previous if statements
            self.functiony += 100       #increases y value to not draw on the same line on pygame
            self.circley += 98      #increases y value to not draw on the same line on pygame
            self.Draw_Function()


    def Draw_Function(self):        #converts previously found xy coordiante system y values to pygaem also converts x too
        zero2 = 0
        for zero1 in range(201):        #for loop for all 201 point, 100 from left 100 from right and 0
            self.realyvalues.append(350 - self.yvalues[self.zero4] * 3.5)  #if yvalue is negative then muliplys the y value by 3.5, 3.5 is the distance between x =1 and x =2, if y
            # value is negative it must be  under x axis however on to go under x axis in pygame you must increase y value, thats why 3.5 is negative, becaue -*- is positive adds it to
            # 350 and finds the point likewise if it is positive +*- is negative and on pygaem axis it will go upper, also at y = 0 it will be 350
            self.realxvalues.append(650 + (zero1-100) * 3.5)    #if zero1 (x)(x starts from -100 increases until 100) at x =0 (zero1 = 100) x will be 650. 650 is the x vlaue of origin in
            # terms of pygame coordinate system, as x increases pygame x increases and as x decreases pygame x decreases too.  thats why this function is consistant with the coordiante
            # system
            if zero2 > 0: #if this statement wasnt here then pgame would try to draw a line however on the first rub there would be only one x and y point so there wont be an endpoint as
                # a result program would crash
                pygame.draw.line(self.screen, self.color, (self.realxvalues[self.zero3-1], self.realyvalues[self.zero3-1]), (self.realxvalues[self.zero3], self.realyvalues[self.zero3]), 3)
            self.zero3+= 1
            zero2 += 1
            self.zero4+=1


screen = Screen()   #call Screen class and name it as screen
Coordinate_system = Field(screen) #give screen as input to Filed Class and name the object as Coordiante_system
func = Functions(screen, Coordinate_system) #give screen and Coordiante_system as input to Functions class and name the object as func

pygame.display.update ()    #displays everything drawn on screen

while True:
    #this code runs to keep the screen alive and when an user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()