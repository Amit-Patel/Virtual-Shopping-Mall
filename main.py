
import pygame
import math,decimal


BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
BLUE   = (   0,   0, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
PURPLE = ( 255,   0, 255)
WANT   = ( 250,  20,  20)
GOLD   = ( 255, 165,   0)
SKY    = (   0, 153, 153)
GREY   = ( 135, 135, 135)

global pos_x,pos_y
global accno,input1,Mmoney,money
global count,l,b,z
global score
global staytime

staytime="0"


def startup():
    global money
    print
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    print"-*-              Welcome  to   Elite  Mall                     -*-"
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"                                                            
    print
    print
    import turtle as t
    import random

    n=raw_input("Enter your Name:")
    gender=raw_input("Enter Your Gender:")
    contactno=raw_input("Enter your Contact number please:")
    h=len(contactno)
    leno=23-h
    if gender=="Male" or gender=="male":
        q="Mr."
        print
        print "Welcome",q,n,"!"
    if gender=="Female" or gender=="female":
        print
        q="Ms."
        print "Welcome",q,n,"!"
    loop=1
    choice=0
    x=0
    money=0
    def refill():
        global money
        print "-"*80
        print "Welcome to the credit top-up counter!"
        print ""
        print "-"*80
        print ""
        new=input("Please enter your shopping card number:")
        print "-"*80
        if new==111297:
            print ""
            print "-"*80
            bank=raw_input("Enter your bank card number:")
            if bank==accno:
                print "-"*80
                print "Card number authorized."
                print
                pass1=input("Enter your bank account password:")
                if pass1==305:
                    print ""
                    print "The information you provided seems correct."
                    print "-"*80
    
                    enter=input("Enter the amount you want to top-up:")
                    if enter>Mmoney:
                        print "Sorry! You do not have that much balance in your Mastercard."
                        print
                    else:
                        money=money+enter
                        print "Thankyou! Qr.",enter,"has been credited to your shopping card!"
                        print "-"*80
            else:
                print "Card number unauthorized."
                block=1
                print "-"*80
            
            
        else:
            print "This card number doesn't exist."
            block=1
            print "-"*80
        
        
    print "-"*80
    print "You will have to pay a money of Qr.1500 from your credit card to avail our shopping card and to explore the mall."
    print "-"*80
    print " "
    print "-"*80
    print "We accept the following cards:"
    print "1. Mastercard"
    print "2. Visa"
    print "3. Maestro"
    print "4. Paypal"
    print "-"*80
    print
    block=0
    input1=raw_input("Enter your card type:")

    if input1=="Mastercard" or input1=="Visa" or input1=="Maestro" or input1=="Paypal":
        Mmoney=5000
        print "-"*80
        new=0
        while new==0:
            accno=raw_input("Enter the account number (10 digits):")
            length=len(accno)
            if length==10:
                new=1
            else:
                print "Sorry! Your bank account number is incorrect! It should be of 10 digits!"
                new=0
        
        pswrd=raw_input("Enter your password:")
        print "-"*80
        if pswrd=="305":
        
            print "Account login successful!"
            print " "
            print "Your current",input1,"card balance in Qr.3000."
            print "-"*80
            tagin=raw_input("Do you agree to transfer Qr.1500 for your shopping card? (Y/N)")
            if tagin=="Y":
                Mmoney=Mmoney-1500
                print "-"*80
                print "Qr.1500 has been transferred from your",input1,"card to your shopping card."
                print
                print "Thankyou for starting up! Enjoy your time here at The Elite Mall."
                print "-"*80
                print
                money=money+1500
                press1=input("Press 1 to get your shopping card:")
                if press1==1:
                    pass
            else:
                print "Thankyou anyways!"
                print "-"*80
            
        
        else:
            print " "
            print "Wrong Password!"
            print "-"*80
            print
        
        

    

    print "Here's your shopping card:"
    print
    print
    print
    if gender=="Male" or gender=="male":
        z=len(n)
        b=29-z
        print
        print "-"*43
        print "|                                         |"
        print "|    ELITE MALL SHOPPING CREDIT CARD      |"
        print "|                                         |"
        print "|   Name :",n," "*b,"|"
        print "|   Gender : Male                         |"
        print "|   Contact No :",contactno," "*leno,"|"
        print "|   Cash Balance : Qr.",money,"              |"
        print "|   Card Number : 111297                  |"
        print "|                                         |"
        print "-"*43
        print " "

    if gender=="Female" or gender=="female":
        z=len(n)
        b=29-z
        print
        print "-"*43
        print "|                                         |"
        print "|    ELITE MALL SHOPPING CREDIT CARD      |"
        print "|                                         |"
        print "|   Name :",n," "*b,"|"               
        print "|   Gender : Female                       |"
        print "|   Contact No :",contactno," "*leno,"|"
        print "|   Cash Balance : Qr.",money,"              |"
        print "|   Card Number : 111297                  |"
        print "|                                         |"
        print "-"*43
        print " "

    
    print "You have a money of Qr.",money," for spending."
    print "Each zone has an entry fee of Qr.100."
    print
    print

#startup()


hello = pygame.display.set_mode([800,600])
hi=pygame.image.load("mario.png")

########################################################

def mario(hi,pos_x, pos_y):
   
    hello.blit(hi,[pos_x,pos_y])


groceryplayer=pygame.image.load("grocerystoremario.png")

#########################################################

def grocerymario(hi,pos_x, pos_y):
    hello.blit(groceryplayer,[pos_x,pos_y])

#########################################################

tata=pygame.image.load("goldenmario.png")

def fifacornermario(tata,pos_x,pos_y):
    hello.blit(tata,[pos_x,pos_y])

#########################################################


    

pygame.display.set_caption("-----------------------------------------------------------------------------------------")


global pos_x,pos_y
pos_x = 320
pos_y = 540
x1=10
y1=10

def guessinggame():
    import random,turtle
    print ""
    print "-"*80
    print "                        Welcome to the The Guessing game"
    print "-"*80
    print ""
    print "Rule 1: Guess the number from 1 to 20 to win a megaprize!"
    print " "
    x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a=random.choice(x)
    count=0
    for i in range(1,6):
        print "-"*80
        s=input("Guess my number:")
        print "-"*80
        if (a==s):
            if count==1:
                print "You've got the correct answer in",count,"tries!"
                print
                print "CONGRATULATIONS! YOU HAVE WON THE MEGAPRIZE!"
                print "YOU GET A MERCEDES BENZ A SERIES"
                print "-"*80
                claim=input("Press 1 to claim the car:")
                if claim==1:
                    turtle.title("CONGRATULATIONS ON YOUR WIN! (click on the window to close it)")
                    turtle.bgpic("merc.gif")
                    turtle.pencolor("white")
                    turtle.pencolor("black")
                    turtle.exitonclick()
                    print "It's not over yet! You also get a prize money of Qr.500 for your personal credit card!"
                    print "-"*80
                    claim2=input("Press 2 to claim it:")
                    if claim2==2:
                        Mmoney=Mmoney+500
                        print "Qr.500 has been credit to your card."
                        print "-"*80
                    
                        break
                    else:
                        print "You've got the correct answer in",count,"tries!"
                        print
                        print "CONGRATULATIONS! YOU HAVE WON!"
                        print "YOU GET A TATA NANO!"
                        print "-"*80
                        claim=input("Press 1 to claim the car:")
                        if claim==1:
                            turtle.pencolor("violet")
                            turtle.title("CONGRATULATIONS ON YOUR WIN! (click on the window to close it)")
                            turtle.bgpic("nano.gif")
                            turtle.pencolor("white")
                            turtle.exitonclick()
                        
                            break
                            
                          
                      
        else:
            count=count+1
            print "HARD LUCK!"
            print "You have another",5-i,"tries left!"
            if (5-i)>=1:
                if a-2<s and s<a+2:
                    print "You're in the hot zone!"
                    print "You have another",5-i,"tries left!"
            if 5-i==0:
                print " "
                print "POOOOOOR!!! The number I was guessing was :",a
            
###############################################################################





################################################################################

def foodcourt():
    
    global staytime    
    global pos_x,pos_y
    pos_x=350
    pos_y=400
    pygame.init()
    global money
    global b
    b=0
    global z
    z={}
    global l
    l={}
   
    def McDonalds():
        global z
        global money
        import turtle as t

        print " "
        print "        Welcome to McDonald's!"
        print "-"*80
        print
        print "We have the following items on the menu:"
        print ""
        print "-"*80
        print "     ITEM NAME                    PRICE "
        print "-"*80
        print "1. Big Mac                        Qr.15"
        print "2. McChicken                      Qr.20"
        print "3. Chicken McNuggets              Qr.30"
        print "4. McCafe Mango                   Qr.40"
        print "5. McFlurry                       Qr.10"
        print "6. Hot cakes                      Qr.25"
        print "7. World Famous Fries             Qr.5"
        print "8. Premium Southwest Salad        Qr.7"

        print "-"*80
        print
        print "Press 9 to have a look at the items on the menu "
        print "Press 10 to display your items and get your bill"
        print
        print "-"*80
        print          
        global b

        
        x=input("Select the item you want to buy:")
        
        if x==1:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+15*g
                z["Big Mac"]=g
                print
                print "This item has been added to your bucket."
                
            if a=="no":
                print "Thank you anyways!"

            print
            
                
            
        if x==2:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+20*g
                z["McChicken"]=g
                print
                print "This item has been added to your bucket."


            if a=="no":
                print "Thank you anyways!"

            print
            
                            
        if x==3:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+30*g
                z["Chicken McNuggets"]=g
                print
                print "This item has been added to your bucket."

                
            if a=="no":
                print "Thank you anyways!"

            print
           

        if x==4:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+40*g
                z["McCafe Mango"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"

            print
            



        if x==5:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+10*g
                z["McFlurry"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"

            print
            
                
        if x==6:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+25*g
                z["Hot Cakes"]=g
                print
                print "This item has been added to your bucket."

                
            if a=="no":
                print "Thank you anyways!"

            print
            
                

        if x==7:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+5*g
                l["World Famous Fries"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"

            print
            

        if x==8:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no')"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+7*g
                z["Premium Southwest Salad"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"
            print
            
                
        if x==9:
            loopo=0
            print "-"*80
            print "Please note: After you are done looking at the items, press 0 to exit"
            print "-"*80

            while loopo==0:
                y=input("Enter your choice :")
                if y==1:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("1.gif")
                    t.exitonclick()
                    

                if y==2:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("2.gif")
                    t.exitonclick()


                if y==3:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("3.gif")
                    t.exitonclick()

                if y==4:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("4.gif")
                    t.exitonclick()


                if y==5:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("5.gif")
                    t.exitonclick()


                if y==6:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("6.gif")
                    t.exitonclick()


                if y==7:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("7.gif")
                    t.exitonclick()


                if y==8:
                    t.setup(width=2000,height=2000,startx=0,starty=0)
                    t.bgpic("8.gif")
                    t.exitonclick()


                if y==0:
                    loopo=1
                    break
                

        if x==10:
            if b>0:
                print
                print "Your bucket items are:"
                print " "
                print "-"*80
                print "Item","\t","   Quantity"
                print "-"*80
                for i in z:
                    print i,'\t',z[i]
                    print "-"*80
                    print "Your total bill is Qr.",b
                    print "-"*80
                    print "Do we confirm your purchase ?"
                    d=raw_input("")
                    if d=="yes":
                        print "-"*80
                        print "Thank you for the purchase!","Qr.",b,"has been deducted from your credit card."
                        money=money-b
                        print "Your current balance is: Qr.",money
                        print " "
                        z={}
                        e=raw_input("Do you want to exit?")
                        if e=="yes":
                            ping=1
                            break
                        else:
                            continue

                    if d=="no":
                        print "Thank you anyways!"
                        print " "
                        e=raw_input("Do you want to exit?")
                        if e=="yes":
                            ping=1
                            break
                        else:
                            pass
                        print "-"*80
                        ping=1
                        break
            else:
                print
                print "-"*80
                print "Thank you for visiting!"
                print "-"*80
                
                




    def KFC():
        global l
        global money
    
        print " "
        print "                       Welcome to KFC!"
        print
        print "SPECIAL 25% DISCOUNT ON PURCHASES WORTH MORE THAN Qr.200! HURRY!"
        print " "
        print "We have the following items on the menu:"
        print ""
        print "-"*80
        print "     ITEM NAME                    PRICE "
        print "-"*80
        print "1. Fun Do Dipping Box               Qr.20"
        print "2. Chicken For Me                   Qr.50"
        print "3. Family Meal                      Qr.70"
        print "4. Value Menu                       Qr.40"
        print "5. Krushers                         Qr.20"
        print "6. Beverages                        Variable"
        print "7. Grilled Sandwich                 Qr.5"
        print "-"*80
        print " "
        print "Press 8 to proceed to the billing counter."
        print "Press 9 to Exit."
        print
        global b
        
        x=input("Select the item you want to buy:")

        if x==1:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")
            
            if a=="yes":
                b=b+20*g
                l["Fun Do Dipping Box"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"
            print
            
                


        if x==2:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")

            if a=="yes":
                b=b+50*g
                l["Chicken For Me"]=g
                print
                print "This item has been added to your bucket."


            if a=="no":
                print "Thank you anyways!"
            print
            


        if x==3:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")

            if a=="yes":
                b=b+70*g
                l["Family Meal"]=g
                print
                print "This item has been added to your bucket."
                
            if a=="no":
                print "Thank you anyways!"
            print
            

        if x==4:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")
        
            if a=="yes":
                b=b+40*g
                l["Value Menu"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"
            print
            



        if x==5:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")
            if a=="yes":
                b=b+20*g
                l["Krushers"]=g
                print
                print "This item has been added to your bucket."

            if a=="no":
                print "Thank you anyways!"
            print
                         


        if x==6:
            print "We have the following beverages:"
            print "-"*80
            print "   BEVERAGE                PRICE"
            print
            print " - Pepsi                    Qr.5"
            print " - 7up                      Qr.5"
            print " - Mountain Dew             Qr.5"
            print " - Sprite                   Qr.5"
            print " - Coke                     Qr.5"
            print
            print "-"*80
            print " "
            f=raw_input("Enter the name of your drink:")
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            s=f.lower()
            if s=="pepsi" or s=="7up" or s=="mountain dew" or s=="sprite" or s=="coke":
                print
                print s,"has been added to your bucket list."
                b=b+5*g
                l[s]=g

            print
            
                

        if x==7:
            print "-"*80
            g=input("Enter quantity:")
            print "-"*80
            print "Can we confirm your order? (Reply with 'yes' for approval otherwise 'no'"
            print "-"*80
            a=raw_input("")
            
            if a=="yes":
                b=b+5*g
                l["Grilled Sandwich"]=g
                print
                print "This item has been added to your bucket."
                
            if a=="no":
                print "Thank you anyways!"
            print
           

        if x==8:
            print
            print
            print
            print 
            print "Your bucket items are:"
            print " "
            print "-"*80
            print "Item","\t","    Quantity"
            print "-"*80
            for i in l:
                print i,'\t',l[i]
                print "-"*80
                print "Your total bill is Qr.",b
                print
                print "Do we confirm your purchase ?"
                d=raw_input("")

                
                if d=="yes":
                    z={}
                    if b>200:
                        b=b-(0.25*b)
                        print "Thank you for the purchase!","Qr.",b,"has been deducted from your credit card after offering you a special discount!"
                    else:
                        print "Thank you for the purchase!","Qr.",b,"has been deducted from your credit card."
                        money-=b
                        print "Your current balance is: Qr.",money
                        print " "
                    print
                    print"-"*80
                    e=raw_input("Do you want to exit?")
                    if e=="yes":
                        pass
                    else:
                        continue

                if d=="no":
                    print "Thank you anyways!"
                    print " "

            
        if x==9:
            print
            print "-"*80
            print "Thank you for choosing KFC. See you next time!"
            print "-"*80


    GAMELOOP = False

    clock = pygame.time.Clock()

    x_speed = 0
    y_speed = 0

    KFC1=pygame.image.load("kfcee.png")
    Phut=pygame.image.load("mcdon1.png")
    title=pygame.image.load("foodcourt.png")
    FLOOR=pygame.image.load("floor.png")
    



    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0

        
        
        if ((pos_x)>350) and ((pos_x)<420) and (pos_y>500) and (pos_y<580):
            pos_x=700
            pos_y=275
            thebase()

        if pos_x>450 and pos_x<520 and pos_y>200 and pos_y<280:
            McDonalds()
            

        if pos_x>150 and pos_x<250 and pos_y>200 and pos_y<280:
            KFC()
            pos_x=200
            pos_y=300
    


    
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed


        hello.fill(WHITE)
       # hello.blit(FLOOR,[0,0])
        hello.blit(KFC1,[30,400])
        hello.blit(Phut,[430,280])
        hello.blit(title,[250,40])
    
        

        
    
        pygame.draw.rect(hello,PURPLE,(20,20,760,540),2)
        pygame.draw.rect(hello,PURPLE,(350,460,80,100),2)

        Hi2=pygame.font.SysFont("monospace",20)
        doorfont=Hi2.render("  EXIT ",True,GREEN)
        Hier=doorfont.get_rect()
        Hier.center=(380,500)
        hello.blit(doorfont,Hier)
        
        
    
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        

        mario(hi, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



def grocery():

    global staytime
    global money
    global pos_x,pos_y
    
    pos_x=20
    pos_y=400
    global count,count1,count2,count3,count4,cost
    
    cost=0
    count=0
    count1,count2,count3,count4=0,0,0,0
    global listbought
    listbought=[]

    def otherwise(x,y):
        
        global money
        global count,count1,count2,count3
        global cost
        global place1
        global place2
        global place3
        global place4
        
        if x>0:
            pass
        
        print "-"*80
        print "You have the following items on your list:"
        print "-"*80
        print
        for i in range(len(listbought)):
            print "   ",i+1,". ",listbought[i]
        print
        theloop=0
        while theloop==0:
                
            print "-"*80
            print "Do you want to add or remove any item? (press A/R to Add or Remove) "
            print
            
            answer=raw_input("Enter (A/R):")
            print "-"*80
            if answer=="R":
                a=input("Enter the number of items you want to remove:")
                for i in range(a):
                    removeitem=raw_input("Enter the name of the item:")
                    a=removeitem.capitalize()
                    if a in listbought:
                        cost=cost-50
                        listbought.remove(a)
                        
                        
            elif answer=="A":
                if y==1:
                    count=0
                    Produce()
                if y==2:
                    count1=0
                    Meat()
                if y==3:
                    count2=0
                    Dairy()
                if y==4:
                    count3=0
                    seafood()

                
                
            print "-"*80

            print "You now have the following items:"
            print "-"*80
            for i in range(len(listbought)):
                print "   ",i+1,". ",listbought[i]
            print
            print "-"*80
            ask=raw_input("Do you want to leave? (Y/N)")
            if ask=="N":
                theloop=0
            if ask=="Y":
                print
                print "Thank you!"
                theloop=1
            
    
    
    def Produce():
        global money
        global count
        global cost
        global place1

        place1=1
       
        listitems=["","Carrots","Lettuce","Cucumbers","Tomatoes","Onions","Red peppers"]
        produceloop=0
        
        if count==0:
            pass
        else:
            otherwise(count,place1)
            count=count+1
            produceloop=1
          
        while produceloop==0:

            print " "
            print "-"*80
            print "We have the following items:"
            print "-"*80
            print "    ITEM            COST"
            
            print "1. Carrots          QR.10/kg"
            print "2. Lettuce          QR.10/kg"
            print "3. Cucumbers        QR.10/kg"
            print "4. Tomatoes         QR.10/kg"
            print "5. Onions           QR.10/kg"
            print "6. Red peppers      QR.10/kg"
            print
            print "-"*80
            print "   Press 7 to Leave!"
            print
        
            
            
            choice=input("Enter choice:")
            if choice==1 or choice==2 or choice==3 or choice==4 or choice==5 or choice==6:
                if listitems[choice] not in listbought:
                    listbought.append(listitems[choice])
                    cost=cost+10
                    print
                    print listitems[choice],"has been added to your grocery bucket."
                else:
                    print
                    print "This item already exists."
            
            if choice==7:
                print ""
                print "-"*80
                print "You now have the following items:"
                print "-"*80
                print "Thank you!"
                print " "
                count=count+1
                produceloop=1
                
    ################################################################################################
    def Meat():
        
        global count1
        global cost
        global money
        global place2

        place2=2
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
                
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        
        listitems=["","Chicken","Beef","Mutton","Pork"]
        produceloop=0
        
        if count1==0:
            pass
        else:
            otherwise(count1,place2)
            count1=count1+1
            produceloop=1
          
        while produceloop==0:

            print " "
            print "-"*80
            print "We have the following items:"
            print "-"*80
            print "    ITEM           COST"
            print "1. Chicken          QR.13/kg"
            print "2. Beef             QR.17/kg"
            print "3. Mutton           QR.12/kg"
            print "4. Pork             QR.15/kg"
            print 
            print "5.  Press 5 to Leave!"
            print
        
            
            
            choice=input("Enter choice:")
            if choice==1 or choice==2 or choice==3 or choice==4:
                if listitems[choice] not in listbought:
                    listbought.append(listitems[choice])
                    cost=cost+50
                    print
                    print listitems[choice],"has been added to your grocery bucket."
                else:
                    print "This item already exists."
            
            if choice==5:
                print ""
                print "-"*80
                print
                print "Thank you!"
                print " "
                count1=count1+1
                produceloop=1
    
    def Dairy():
        global count2
        global cost
        global money
        global place3

        place3=3
                
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
        
        listitems=["","Eggs","Butter","Milk","Yogurt"]
        produceloop=0
        
        if count2==0:
            pass
        else:
            otherwise(count2,place3)
            count2=count2+1
            produceloop=1
          
        while produceloop==0:

            print " "
            print "-"*80
            print "We have the following items:"
            print "-"*80
            print "    ITEM           COST"
            print "1. Eggs           QR.10/6 Eggs"
            print "2. Butter         QR.7/kg"
            print "3. Milk           QR.7/L"
            print "4. Yogurt         QR.15/6 Cups"
            print 
            print "5. Press 5 to Leave!"
            print
        
            
            
            choice=input("Enter choice:")
            if choice==1 or choice==2 or choice==3 or choice==4: 
                if listitems[choice] not in listbought:
                    listbought.append(listitems[choice])
                    cost=cost+50
                    print
                    print listitems[choice],"has been added to your grocery bucket."
                else:
                    print "This item already exists."
            
            if choice==5:
                print ""
                print "-"*80
                print "Thank you!"
                print " "
                count2=count2+1
                produceloop=1
    def seafood():
        
        global count3
        global cost
        global money
        global place4
                
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        place4=4
        
        listitems=["","Shrimps","Salmon","Piranha","Prawns"]
        produceloop=0
        
        if count3==0:
            pass
        else:
            otherwise(count3,place4)
            count3=count3+1
            produceloop=1
          
        while produceloop==0:

            print " "
            print "-"*80
            print "We have the following items:"
            print "-"*80
            print "    ITEM           COST"
            print "1. Shrimps        QR.50/kg"
            print "2. Salmon         QR.50/kg"
            print "3. Piranha        QR.50/kg"
            print "4. Prawns         QR.50/kg"
            print 
            print "   Press 7 to Leave!"
            print
        
            
            
            choice=input("Enter choice:")
            if choice==1 or choice==2 or choice==3 or choice==4 or choice==5 or choice==6:
                if listitems[choice] not in listbought:
                    listbought.append(listitems[choice])
                    cost=cost+50
                    print
                    print listitems[choice],"has been added to your grocery bucket."
                else:
                    print "This item already exists."
            
            if choice==7:
                print ""
                print "-"*80
                print "You now have the following items:"
                print "-"*80
                print "Thank you!"
                print " "
                count3=count3+1
                produceloop=1
        ############################################################################################

    def guestservice():
        global cost
        global listbought
        global money
        
        print ""
        print "Hello! You have the following items in your bucket:"
        print
        print "-"*80
        for i in range(len(listbought)):
            print "   ",i+1,". ",listbought[i]
        print
        print "That costs Qr.",cost
        print " "
        askagain=raw_input("Do you want to purchase them?")
        if askagain=="Y":
            listbought=[]
            money=money-cost
            print "Your balance is now QR.",money
            print "Thank you, please visit again!"
        else:
            print "Thank you! Come again!"
        
        
    
            
                        
    pygame.init()

    


    GAMELOOP = False

    clock = pygame.time.Clock()

    x_speed = 0
    y_speed = 0

    lulu=pygame.image.load("lulumap.png")
    
    
    



    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0

        
        
        if ((pos_x)>260 and pos_x<350 and (pos_y>560) and (pos_y<600)):
            pos_x=720
            pos_y=150
            thebase()
            
        if pos_x>200 and pos_x<240 and pos_y<220 and pos_y>200:
            Produce()
            pos_x=250
            pos_y=225

        if pos_x>200 and pos_x<280 and pos_y<80 and pos_y>60:
            seafood()
            pos_x=250
            pos_y=100

        if pos_x>200 and pos_x<240 and pos_y<560 and pos_y>520:
            guestservice()
            pos_x=260
            pos_y=540

        if pos_x>700 and pos_x<740 and pos_y<400 and pos_y>280:
            Dairy()
            pos_x=700
            pos_y=350

        if pos_x>600 and pos_x<740 and pos_y<80 and pos_y>50:
            Meat()
            pos_x=650
            pos_y=60
            
     
    
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed


        hello.fill(WHITE)
        hello.blit(lulu,[60,40])

        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("         EXIT HERE!",True,GREEN)
        Exiter=exitfont.get_rect()
        Exiter.center=(300,580)
        hello.blit(exitfont,Exiter)
        
        

        
    
        pygame.draw.rect(hello,WANT,(60,40,684,520),2)
        pygame.draw.rect(hello,WANT,(260,560,150,80),2)
        

        
        
    
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))

        grocerymario(hi, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



#######################################################################################################



#################################################################################################"""


    
################################################################################
def ATM2():
    global money
    
    
    print
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    print"-*-                Welcome to Trida ATM                        -*-"
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    print
    print"-"*80
    print"The  following cards are accepted:"
    print"-"*80
    print "1. Mastercard"
    print "2. Visa"
    print "3. Maestro"
    print "4. Paypal"
    print "-"*80
    print
    block=0
    input1=raw_input("Enter your card type:")
    if input1=="Mastercard" or input1=="Visa" or input1=="Maestro" or input1=="Paypal":
        
        
        print "-"*80
        new=0
        while new==0:
            accno=raw_input("Enter the account number (10 digits):")
            length=len(accno)
            if length==10:
                new=1
            else:
                print "Sorry! Your bank account number is incorrect! It should be of 10 digits!"
                break

            pswrd=raw_input("Enter your password:")
            print "-"*80
            if pswrd=="305":
                print "Account login successful!"
                print " "
                print "Your current",input1,"card balance is Qr.",money
                continue
  

      
      
            else:
                "Incorrect Password"
                break
    loop=1
    choice=0
    while loop==1:
        print
        print"-"*80
        print"1)Deposit Cash"
        print"2)Withdraw Cash"
        print"3)Check Balance"
        print"4)Exit ATM"
        print"-"*80
        print
        choice=input("Enter your choice :")
        if choice==1:
            print"How much cash would you like to deposit ? "
            dep=input("Enter amount:")
            if dep>5000:
                print"You can only deposit an amount of upto Qr.5000"
            else:

                print"You have succesfully deposited Qr.",dep
                money+=dep
        if choice==2:
            print"How much cash would you like to withdraw ?"
            wdr=input("Enter amount:")
            if wdr>money:
                print"You cannot withdraw amount as it is more than your account balance"
            else:
                print"You have succesfully withdrawn Qr.",wdr
                money-=wdr                  

                 
        if choice==3:
            print"Your current balance is:",money
        if choice==4:
            print "Thank you for using Trida ATM! Wishing you good health and wealth!"
            print "-"*80
            loop=0
            break

################################################################################

def FIFACORNER():
    import turtle
    print
    print
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    print"-*-                Welcome to World Cup Corner                 -*-"
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    print " "
    print "-"*80
    print
    print "              WELCOME TO THE FIFA WORLDCUP 2014 CORNER!"
    print ""
    print "-"*80
    print "Participate in the various activities and win amazing prizes!"
    print
    print "We have the following activities:"
    print "-"*80
    print
    print "1.World Cup 2014 Quiz"
    print "2.Guess the player!"
    print
      
    pick=0
    like=input("Enter your choice:")
    if like==1:
        score=0
        print
        print "Thankyou for selecting World Cup 2014 Quiz!"
        print
        print "So here are some simple rules before we jump to the quiz:"
        print "- The quiz consists of 10 questions."
        print "- Each correct answer fetches 5 points."
        print "- Each incorrect answer costs 5 points as well."
        print ""
        print "Aim for the highest!"
        print " "
        print "-"*80
        print
        print "Are you ready? (Y/N)"
        ready=raw_input()
        if ready=="Y":
            pass
        else:
            print "Don't be lazy! Play the game."
            pass
        
        print " "
        print "1. How many times have Germany won the World Cup including this win? "
        print "-"*80
        print "Your options are:"
        print
        print "a.2"
        print "b.3"
        print "c.8"
        print "d.4"
        a1=raw_input("Enter your answer:")
        if a1=="d":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "2. Who won the award for the Golden Boot? "
        print "-"*80
        print "Your options are:"
        print
        print "a.Messi"
        print "b.Neuer"
        print "c.James Rodriguez"
        print "d.Paul Rodriguez"
        b1=raw_input("Enter your answer:")
        if b1=="c":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "3. Who is the all time World Cup top scorer and with how many goals? "
        print "-"*80
        print "Your options are:"
        print
        print "a. Ronaldo - 17 goals"
        print "b. Muller - 15 goals"
        print "c. Ronaldo - 16 goals"
        print "d. Klose - 16 goals"
        c1=raw_input("Enter your answer:")
        if c1=="d":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "4. Who did Netherlands play against in the Quarter Finals? "
        print "-"*80
        print "Your options are:"
        print
        print "a. Croatia"
        print "b. Costa Rica"
        print "c. Columbia"
        print "d. Argentina"
        d1=raw_input("Enter your answer:")
        if d1=="b":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "5. In total how many stadiums hosted the World Cup 2014 matches? "
        print "-"*80
        print "Your options are:"
        print
        print "a. 10"
        print "b. 11"
        print "c. 12"
        print "d. 8"
        e1=raw_input("Enter your answer:")
        if e1=="c":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "6. What is the name of the player whom Luis Suarez bit during a World Cup match? "
        print "-"*80
        print "Your options are:"
        print
        print "a. Chiellini"
        print "b. Chellaini"
        print "c. Fellaini"
        print "d. Chicken Nuggets"
        f1=raw_input("Enter your answer:")
        if f1=="a":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "7. In which minute did Mario Gotze scored the World Cup winning goal?"
        print "-"*80
        print "Your options are:"
        print
        print "a. 117"
        print "b. 113"
        print "c. 109"
        print "d. 114"
        print
        g1=raw_input("Enter your answer:")
        print
        if g1=="b":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "8. What is the name of the eldest player to have played in all of the World Cups?"
        print "-"*80
        print "Your options are:"
        print
        print "a. Pele"
        print "b. Mondragon"
        print "c. Casillas"
        print "d. Di Stefano"
        g1=raw_input("Enter your answer:")
        if g1=="b":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "9. Which was the first World Cup 2014 game to have ended in a draw?"
        print "-"*80
        print "Your options are:"
        print
        print "a. Brazil vs Mexico"
        print "b. Japan vs Greece"
        print "c. Iran vs Nigeria"
        print "d. Russia vs Korea"
        g1=raw_input("Enter your answer:")
        if g1=="c":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print " "
        print " "
        print "10. Which player has a tatto on his torso that reads 'Only God Can Judge Me'?"
        print "-"*80
        print "Your options are:"
        print
        print "a. Ronaldo"
        print "b. Marcelo"
        print "c. Neymar"
        print "d. Ibrahimovic"
        g1=raw_input("Enter your answer:")
        if g1=="d":
            score=score+5
            print "You got the answer correct!"
        else:
            print "Oops! That was an incorrect answer."
            score=score-5
        print "-"*80
        print "With that we come to the end of the quiz."
        print ""
        print "Your total score is:",score
        print "-"*80
        if score>=45:
            print " "
            print "Congratulations! You have won Qr.50 worth credit for your shopping card!"
            money=money+50
            print "-"*80
        else:
            print " "
            print "Try next time!"
            print " "
            cont=raw_input("press E to exit:")
            if cont=="E":
                pick=1

    if like==2:
        import turtle
        score1=0
        print " "
        print "Thank you for selecting Guess the Player game!"
        print " "
        print "The rule is simple : Give the name of the play shown in the picture and earn 10 points for each correct answer"
        print "Be careful about your punctuation!"
        print " "
        begin=raw_input("Shall we begin? (Y/N)")
        if begin=="Y":
            pass
        else:
            pass
        print ""
        print "Here we go!"
        print " "
        print "-"*80
        print "Number 1: "
        print "-"*80
        print
        a=input("Press 1 to view the player's image:")
        if a==1:
            
            turtle.delay(150)
            turtle.bgpic("dempsey.gif")
            
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Dempsey":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print
        print "-"*80
        print "Number 2: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Fred.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Fred":
                  score1=score1+10
                  print " "
                  print "Your answer was correct!"
                  print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 3: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Gotze.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Gotze" or name=="Goetze":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 4: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Tim Howard.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Tim Howard":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 5: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Huntelaar.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Huntelaar":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 6: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Schurrle.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Schurrle":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 7: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.delay(150)
            turtle.bgpic("Varane.gif")
            
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Varane":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 8: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Ronaldo.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Ronaldo":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 9: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.bgpic("Ochoa.gif")
            turtle.delay(150)
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Ochoa":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print "-"*80
        print "-"*80
        print "Number 10: "
        print "-"*80
        a=input("Press 1 to view the player's image:")
        if a==1:
            turtle.delay(150)
            turtle.bgpic("Hazard.gif")
            
            turtle.hideturtle()
            turtle.forward(100)
            
            
            turtle.bye()
            
            print " "
            name=raw_input("Enter the player's name:")
            if name=="Hazard":
                score1=score1+10
                print " "
                print "Your answer was correct!"
                print
            else:
                score1=score1-5
                print "Oops!"
        print ""
        print "-"*80
        print "Your total score is:",score1
         
        print "-"*80
        if score1>=80:
            print " "
            print "Congratulations! You have won Qr.100 worth credit for your shopping card!"
            money=money+100
            print "-"*80
        else:
            print " "
            print "Try next time!"
        print " "
        cont=raw_input("press E to exit:")
        if cont=="E":
            pass

################################################################################

def FIFA():

    global staytime
    global pos_x,pos_y
    pygame.init()

    pos_x = 80
    pos_y = 120

    


    GAMELOOP = False

    clock = pygame.time.Clock()
    wallpaper=pygame.image.load("fifa.gif")

    x_speed = 0
    y_speed = 0

    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            if event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0
        if (pos_x)<70 and (pos_y<60):
            pos_x=700
            pos_y=520
            thebase()
            
        if pos_x<70 and pos_y>520:
            FIFACORNER()
            pos_x=80
            pos_y=500

       
            
        
        
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed

        hello.fill(BLACK)
        hello.blit(wallpaper,[50,170,800,230])
        pygame.draw.rect(hello,GOLD,(10,10,780,580),2)
        pygame.draw.rect(hello,GOLD,(10,10,80,100),2)
        pygame.draw.rect(hello,GOLD,(710,10,80,100),2)
        pygame.draw.rect(hello,GOLD,(10,10,700,100),2)
        pygame.draw.rect(hello,GOLD,(10,490,80,100),2)

        

        Hi2=pygame.font.SysFont("showcard gothic",40)
        doorfont=Hi2.render("  FIFA WORLD CUP 2014 ",True,GOLD)
        Hier=doorfont.get_rect()
        Hier.center=(400,60)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("calibri",20)
        doorfont=Hi2.render("   EXIT",True,GOLD)
        Hier=doorfont.get_rect()
        Hier.center=(40,60)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("calibri",20)
        doorfont=Hi2.render("    GAMES",True,GOLD)
        Hier=doorfont.get_rect()
        Hier.center=(40,540)
        hello.blit(doorfont,Hier)
        
        
        
        
        
        
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
    
            
        

        fifacornermario(tata, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

###############################################################################

def XNO():
    print " "
    print "-"*80
    print "WELCOME TO X AND O"
    a1,a2,a3,b1,b2,b3,c1,c2,c3=" "," "," "," "," "," "," "," "," "
    l=["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
    print "-"*80
    print
    print "",a1," | ",a2,"| ",a3,"               a1 | a2 | a3  "
    print " ___|____|___                ___|____|___"
    print "",b1," | ",b2,"| ",b3,"               b1 | b2 | b3  "
    print " ___|____|___                ___|____|___"
    print "",c1," | ",c2,"| ",c3,"               c1 | c2 | c3  "
    print "    |    |                      |    |   "
    print " "
    gamelist=["X","O"]
    def matrix():
        print "-"*80
        print
        print "",a1," | ",a2,"| ",a3
        print " ___|____|___  "
        print "",b1," | ",b2,"| ",b3
        print " ___|____|___  "
        print "",c1," | ",c2,"| ",c3
        print "    |    |            "
        print " "
    p1=raw_input("Are you ready player 1? (Y/N)")
    if p1=="Y":
        x="X"
    p2=raw_input(" Are you ready player 2? (Y/N)")
    if p2=="Y":
        x1="O"
    for i in range(9):
        if i%2==0:
            if x=="X":
                print "It's player 1's turn!"
                a=raw_input("Enter which position:")
                if a=="a1":
                    a1=x
                if a=="a2":
                    a2=x
                if a=="a3":
                    a3=x
                if a=="b1":
                    b1=x
                if a=="b2":
                    b2=x
                if a=="b3":
                    b3=x
                if a=="c1":
                    c1=x
                if a=="c2":
                    c2=x
                if a=="c3":
                    c3=x
                matrix()
                if (a1==a2 and a1==a3 and a1=="X") or (a1==b1 and b1==c1 and a1=="X") or (a1==b2 and b2==c3 and a1=="X") or (a3==b2 and b2==c1 and a3=="X") or (b1==b2 and b2==b3 and b1=="X") or (c1==c2 and c2==c3 and c1=="X") or (a1==b2 and b2==c2 and a1=="X") or (a3==b3 and b3==c3 and a3=="X"):
                    print "Congratulations! You have won player 1!"
                    break
                if (a1==a2 and a1==a3 and a1=="O") or (a1==b1 and b1==c1 and a1=="O") or (a1==b2 and b2==c3 and a1=="O") or (a3==b2 and b2==c1 and a3=="O") or (b1==b2 and b2==b3 and b1=="O") or (c1==c2 and c2==c3 and c1=="O") or (a1==b2 and b2==c2 and a1=="O") or (a3==b3 and b3==c3 and a3=="O"):
                    print "Congratulations! You have won player 2!"
                    break
        if i%2!=0:
            loopa=0
            while loopa==0:
                a=raw_input("Enter which position:")
                if a=="a1":
                    a1=x1
                    loopa=1
                if a=="a2":
                    a2=x1
                    loopa=1
                if a=="a3":
                    a3=x1
                    loopa=1
                if a=="b1":
                    b1=x1
                    loopa=1
                if a=="b2":
                    b2=x1
                    loopa=1
                if a=="b3":
                    b3=x1
                    loopa=1
                if a=="c1":
                    c1=x1
                    loopa=1
                if a=="c2":
                    c2=x1
                    loopa=1
                if a=="c3":
                    c3=x1
                    loopa=1
                matrix()
                if (a1==a2 and a1==a3 and a1=="X") or (a1==b1 and b1==c1 and a1=="X") or (a1==b2 and b2==c3 and a1=="X") or (a3==b2 and b2==c1 and a3=="X") or (b1==b2 and b2==b3 and b1=="X") or (c1==c2 and c2==c3 and c1=="X") or (a1==b2 and b2==c2 and a1=="X") or (a3==b3 and b3==c3 and a3=="X"):
                    print "Congratulations! You have won player 1!"
                    break
                if (a1==a2 and a1==a3 and a1=="O") or (a1==b1 and b1==c1 and a1=="O") or (a1==b2 and b2==c3 and a1=="O") or (a3==b2 and b2==c1 and a3=="O") or (b1==b2 and b2==b3 and b1=="O") or (c1==c2 and c2==c3 and c1=="O") or (a1==b2 and b2==c2 and a1=="O") or (a3==b3 and b3==c3 and a3=="O"):
                    print "Congratulations! You have won player 2!"
                    break

###############################################################################

def KONEKT():
    from itertools import groupby, chain
    global pos_x,pos_y
    loop2=0 
    Positon= '|_'
    Player1= 'P1'
    Player2= 'P2'
    print"-"*80
    print" "*20,"Welcome to Konekt"
    print"-"*80
    print
    def DiagonalsPositive (matrix, cols, rows):
        for di in([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
            yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]
    def DiagonalsNegative (matrix, cols, rows):
        for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
            yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

    class Game:
        def __init__(self,cols=7,rows=6,requiredtoWin=4):
            self.cols=cols
            self.rows=rows
            self.win=requiredtoWin
            self.board=[[Positon]*rows for i in range(cols)]

        def insert (self,column,player):
            c=self.board[column]
            if c[0]!=Positon:
                print
                print "Column is full !!"
                global loop2
                loop2=0
            i=-1
            while c[i]!=Positon:
                i=i-1
            c[i]=player

            self.checkforWin()

        def checkforWin(self):
            w=self.getWinner()
            if w:
                self.printBoard()
                print
                print"-"*80
                print"Congratulations !!"
                print w,"Won!!"
                print"-"*80
                global loop2
                pos_x=650
                pos_y=100
                
                loop2=5
        

        def getWinner(self):
            lines=( self.board,
                    zip(*self.board),
                    DiagonalsPositive(self.board, self.cols, self.rows),
                    DiagonalsNegative(self.board, self.cols, self.rows) )
            for line in chain(*lines):
                for player,group in groupby(line):
                    if player!=Positon and len(list(group))>=self.win:
                        return player

        def printBoard(self):
            print
            print
            print "                    ",("     ".join(map(str,range(self.cols))))
            for y in range(self.rows):
                print "                   ",("    ".join(str(self.board[x][y]) for x in range(self.cols)))
        

    while loop2==0:
        g=Game()
        turn=Player1
        while loop2==0:
            print
            g.printBoard()
            print
            print
            row=input('{}\'s turn: '.format("Player1" if turn==Player1 else "Player2"))
            g.insert(int(row),turn)
            if turn==Player1:
                turn=Player2
            else:
                turn=Player1
            
            
###############################################################################
def Gamezone():
    
    global pos_x,pos_y
    global enemyX,enemyY
    global staytime
    
    pygame.init()

    pos_x = 80
    pos_y = 120

    


    GAMELOOP = False

    clock = pygame.time.Clock()
    wallpaper=pygame.image.load("gamezone.png")

    x_speed = 0
    y_speed = 0

    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            if event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0

        if (pos_x)<70 and (pos_y<80):
            pos_x=30
            pos_y=275
            thebase()
            #left second
        if (pos_x)<-15 and (pos_y<200):
            pass
            #left first
        if (pos_x)<300 and (pos_x)>200 and (pos_y>200 and pos_y<300):
            XNO()
            pos_x=350
            pos_y=400
                    
               
                    
                
        if (pos_x>570) and (pos_x<630) and (pos_y>200 and pos_y<300):
            guessinggame()
            pos_x=570
            pos_y=350
            #right second
        if (pos_x)>460 and (pos_x<510) and (pos_y>200 and pos_y<300):
               
            import kiddygame
            #right third
        if (pos_x)>120 and (pos_x<180) and (pos_y>200 and pos_y<300):
            game()

        if (pos_x)>720 and (pos_x<800) and (pos_y>20 and pos_y<100):
            pos_x=650
            pos_y=100
            KONEKT()
            

        
            
            
        

    
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed


        hello.fill(BLACK)
        hello.blit(wallpaper,[100,350,800,230])
        
    

        Hi=pygame.font.SysFont("monospace",20)
        doorfont=Hi.render("   A-MAZE",True,RED)
        Hier=doorfont.get_rect()
        Hier.center=(120,280)
        hello.blit(doorfont,Hier)

        

        Hi=pygame.font.SysFont("monospace",20)
        doorfont=Hi.render("    X N O",True,RED)
        Hier=doorfont.get_rect()
        Hier.center=(290,280)
        hello.blit(doorfont,Hier)

        Hi1=pygame.font.SysFont("monospace",20)
        doorfont=Hi1.render("    LUCK ",True,RED)
        Hier=doorfont.get_rect()
        Hier.center=(460,280)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("monospace",20)
        doorfont=Hi2.render("        GUESSING  ",True,RED)
        Hier=doorfont.get_rect()
        Hier.center=(620,250)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("monospace",20)
        doorfont=Hi2.render("        GAME  ",True,RED)
        Hier=doorfont.get_rect()
        Hier.center=(620,300)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("monospace",20)
        doorfont=Hi2.render("  EXIT ",True,WHITE)
        Hier=doorfont.get_rect()
        Hier.center=(40,60)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("monospace",20)
        doorfont=Hi2.render("   MORE ",True,WHITE)
        Hier=doorfont.get_rect()
        Hier.center=(740,60)
        hello.blit(doorfont,Hier)
            
    
        pygame.draw.rect(hello,RED,(10,10,780,580),5)
        
        pygame.draw.rect(hello,GREY,(70,200,150,150),2)
        pygame.draw.rect(hello,GREY,(240,200,150,150),2)
        pygame.draw.rect(hello,GREY,(410,200,150,150),2)
        pygame.draw.rect(hello,GREY,(580,200,150,150),2)
        pygame.draw.rect(hello,GREY,(10,10,70,100),2)
        pygame.draw.rect(hello,GREY,(720,10,70,100),2)        
   
    
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))

        mario(hi, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
def COMSERV():
    
    global pos_x,pos_y
    global staytime
    
    pos_x=380
    pos_y=520
    pygame.init()



    def csv():

        global staytime
        

        pygame.init()
  

        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
            

        pygame.quit()
    


    GAMELOOP = False

    clock = pygame.time.Clock()

    x_speed = 0
    y_speed = 0

    import random

    a=["green2.png"]
    x=random.choice(a)
    if x=="green2.png":
        position=[80,0]
    
    

    bg=pygame.image.load(x)
    
       

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0
                    
        if ((pos_x)>350) and ((pos_x)<420) and (pos_y>570) and (pos_y<590):
            pos_x=120
            pos_y=530
            thebase()
        if pos_x>300 and pos_x<450 and pos_y<150:
            customerservice()
            
            pos_x=400
            pos_y=45
    
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed
 
        comservsprite=pygame.image.load("comservsprite.png")
        swirl=pygame.image.load("swirl.png")
   
        hello.fill(BLACK)
        hello.blit(bg,position)
        hello.blit(comservsprite,[340,20])
        hello.blit(swirl,[-50,0])
        hello.blit(swirl,[595,0])        
        hello.blit(swirl,[-50,255])
        hello.blit(swirl,[595,255])
        hello.blit(swirl,[-50,510])
        hello.blit(swirl,[595,510]) 
        
        pygame.draw.rect(hello,BLACK,(250,150,310,40),5)
        pygame.draw.rect(hello,BLACK,(350,550,90,60),5)

        Hi2=pygame.font.SysFont("Arial Black",25)
        doorfont=Hi2.render("  CUSTOMER SERVICE ",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(400,170)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("Arial Black",20)
        doorfont=Hi2.render("  EXIT ",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(390,575)
        hello.blit(doorfont,Hier)

        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
 

        mario(hi, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

######################################################################################################################################################################
def customerservice():
    import sys
    print
    print
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    print"-*-                Welcome to Customer Service                  -*-"
    print"-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-*-*-"
    d={}
    print
    print"Welcome to Customer Service!"
    print
    #Print Name of customer
    print"My Name is Bob. How can I be of Service to you today? "#Name
    
    loopalpha=1
    choicealpha=0
    while loopalpha==1:
        print "-"*80
        print
        print"1)Offers"
        print"2)Raffle Draws"
        print"3)Feedback"
        print"4)Complaints"
        print"5)Do you want to Leave?"
        print
        print "-"*80
        print

        choicealpha=input("Which of the following would you like to know about:")
        if choicealpha==1:
            print
            print"We have a variety of offers at the following stores:"
            print
            loopaaalpha=1
            choicealpha=0
            while loopalpha==1:
                print "-"*80
                print
                print"1)Gaming Zone"
                print"2)Clothes"
                print"3)Movies"
                print"4)Food"
                print"5)Saloon"
                print"6)Quit"
                print
                print "-"*80
                print
                choicebeta=input("Which shop would you like to know about?:")
                if choicebeta==1:
                    print"We currently have offers in the try your luck game where you can win bonus prizes!"
                if choicebeta==2:
                    print""
                if choicebeta==3:
                    print"#"
                if choicebeta==4:
                    print"In the food section, we have a special offer in KFC!"
                    ask=raw_input("Would you like to know more about it? (Y/N)")
                    if ask=="Y":
                        print ""
                        print "KFC offers a special discount of 25% on purchases worth Qr.200 or more!"
                        print " "
                        print "Thank you!"
                        print "-"*80
                    if ask!="N":
                        print "Thank you anyways!"
                        print
                if choicebeta==5:
                    print"#"
                if choicebeta==6:
                    break
         
        if choicealpha==2:
            print"We have raffle draws at the following Stores:"
            print"#"
        if choicealpha==3:
            print"To provide your feedback please enter your name and phone number and then proceed to write your feedback"
            print "-"*80
            name=raw_input("Enter name:")
            print "-"*80
            phone=input("Enter phone no:")
            print "-"*80
            d[name]=phone
            feedback=""
            feedback=raw_input("You may now proceed to write your feedback:")
            print "-"*80
            str=feedback
            print "-"*80
            print"Thank you for your feedback!"
        if choicealpha==4:
            print "-"*80
            print"To provide your complaint please enter your name and phone number and then proceed to write your complaint"
            print "-"*80
            name=raw_input("Enter name:")
            print "-"*80
            phone=input("Enter phone no:")
            print "-"*80
            subject=""
            subject=raw_input("Enter the subject of your complaint:")
            print "-"*80
            d[name]=phone
            complaint=""
            complaint=raw_input("You may now proceed to file your Complaint")
            print "-"*80
            str=complaint
            print "-"*80
            print"Thank you! We will look into the matter as soon as possible!"
        
        if choicealpha==5:
            break
            print"Thank you for visiting Verdant Mall Customer Service. Please visit us again if you have any further queries."
            print "-"*80
           

###############################################################################

def MOVIEZONE():
    
    global pos_x,pos_y
    global staytime
    
    pos_x=380
    pos_y=520
    pygame.init()

    def DOPOA():

        global staytime
        
    
        pygame.init()
        pygame.mixer.quit()
        movie=pygame.movie.Movie("DOPOA.mpg")
        if movie.has_video():
            
            hello=pygame.display.set_mode([800,600])
            movie_length=movie.get_length()
            movie.set_volume(0.99)
            movie.set_display(hello)
            movie.play()
            
            
        
        playing=True
        while playing:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    movie.stop()
                    playing=False
            key=pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                movie.stop()
                
                MOVIEZONE()


            staytime=float(staytime)+0.2
            staytime=str(round(staytime,1))
            

        pygame.quit()
        
    def HERCULES():

        global staytime
        

        pygame.init()
        pygame.mixer.quit()
        movie=pygame.movie.Movie("Hercules.mpg")
        if movie.has_video():
            
            hello=pygame.display.set_mode([800,600])
            movie_length=movie.get_length()
            movie.set_volume(0.99)
            movie.set_display(hello)
            movie.play()
            
        
        playing=True
        while playing:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    movie.stop()
                    playing=False
            key=pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                movie.stop()
                
                MOVIEZONE()
            

            staytime=float(staytime)+0.2
            staytime=str(round(staytime,1))
            

        pygame.quit()

    def GOTG():

        global staytime
        

        pygame.init()
        pygame.mixer.quit()
        movie=pygame.movie.Movie("GOTG.mpg")
        if movie.has_video():
            
            hello=pygame.display.set_mode([800,600])
            movie_length=movie.get_length()
            movie.set_volume(0.99)
            movie.set_display(hello)
            movie.play()
            
        
        playing=True
        while playing:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    movie.stop()
                    playing=False
            key=pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                movie.stop()
                
                MOVIEZONE()
            

            staytime=float(staytime)+0.2
            staytime=str(round(staytime,1))
            

        pygame.quit()
    


    GAMELOOP = False

    clock = pygame.time.Clock()

    x_speed = 0
    y_speed = 0

    import random

    a=["scientists.png"]
    x=random.choice(a)
    if x=="scientists.png":
        position=[0,0]

    

    bg=pygame.image.load(x)
    
    



    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0
                    
        if ((pos_x)>350) and ((pos_x)<420) and (pos_y>570) and (pos_y<590):
            pos_x=20
            pos_y=180
            thebase()
        if pos_x>350 and pos_x<450 and pos_y<15:
            CINEMA()
            
            pos_x=400
            pos_y=45
        if pos_x>130 and pos_x<200 and pos_y>570:
            
            DOPOA()
            pos_x=150
            pos_y=400

        if pos_x>230 and pos_x<300 and pos_y>570:
            pygame.mixer.pause()
            HERCULES()
            pos_x=250
            pos_y=400

        if pos_x>330 and pos_x<400 and pos_y>570:
            pygame.mixer.pause()
            GOTG()
            pos_x=250
            pos_y=400

    
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed


        hello.fill(BLACK)
        hello.blit(bg,position)
        

        
        pygame.draw.rect(hello,BLACK,(300,5,200,40),4)
        pygame.draw.rect(hello,BLACK,(5,5,790,585),4)
        pygame.draw.rect(hello,BLACK,(350,550,80,40),4)
        pygame.draw.rect(hello,BLACK,(250,550,80,40),4)
        pygame.draw.rect(hello,BLACK,(150,550,80,40),4)
        pygame.draw.rect(hello,BLACK,(450,550,80,40),4)
        pygame.draw.rect(hello,BLACK,(550,550,80,40),4)
        pygame.draw.rect(hello,BLACK,(50,550,80,40),4)
        pygame.draw.rect(hello,BLACK,(650,550,80,40),4)

        Hi2=pygame.font.SysFont("Arial Bold",25)
        doorfont=Hi2.render("  EXIT ",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(390,575)
        hello.blit(doorfont,Hier)

        doorfont=Hi2.render("3",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(290,575)
        hello.blit(doorfont,Hier)

        doorfont=Hi2.render("2",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(190,575)
        hello.blit(doorfont,Hier)

        doorfont=Hi2.render("1",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(90,575)
        hello.blit(doorfont,Hier)

        doorfont=Hi2.render("4",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(490,575)
        hello.blit(doorfont,Hier)

        doorfont=Hi2.render("5",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(590,575)
        hello.blit(doorfont,Hier)

        doorfont=Hi2.render("6",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(690,575)
        hello.blit(doorfont,Hier)

        Hi2=pygame.font.SysFont("Arial Bold",25)
        doorfont=Hi2.render("  CINEMA RECEPTION ",True,BLACK)
        Hier=doorfont.get_rect()
        Hier.center=(400,25)
        hello.blit(doorfont,Hier)

        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
 

        mario(hi, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

#################################################################################

def CINEMA():

    print
    print"-"*80
    print"1)Movie Information"
    print"2)Ticket Counter"
    print"3)Snack Counter"
    print"4)Exit"
    print"-"*80

    choicealpha=input("Where would you like to go ? ")    
    print""
    if choicealpha==1:
        print"Welcome to Movie Information"
        print""
        loopalpha=1
        choicealpha=0
        while loopalpha==1:
            print"-"*80
            print"1)Opening This Week"
            print"2)Out Now"
            print"3)Coming Soon"
            print"4)Exit"
            print"-"*80
            print""
            choicebeta=input("Enter which section you would like to know about ? ")
            if choicebeta==1:
                print
                print"Opening This Week"
                loopaaalpha=1
                choicealpha=0
                while loopaaalpha==1:
                    print"-"*80
                    print"1)Teenage Mutant Ninja Turtles"
                    print"2)The Hundred-Foot Journey"
                    print"3)Into The Storm"
                    print"4)Step Up All In"
                    print"5)What If"
                    print"6)Go Back"
                    print"-"*80
                    choicegamma=input("Enter which section you would like to know about ? ")
                    if choicegamma==1:
                        print
                        print
                        print"-"*80
                        print"Teenage Mutant Ninja Turtles"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Darkness has settled over New York City as Shredder and his evil
Foot Clan have an iron grip on everything from the police to the politicians.                                               
The future is grim until four unlikely outcast brothers rise from the sewers
and discover their destiny as Teenage Mutant Ninja Turtles. The Turtles must
work with fearless reporter April O'Neil and her cameraman Vern Fenwick to save
the city and unravel Shredder's diabolical plan."""
                        print"-"*80
                        print
                        print
                    if choicegamma==2:
                        print
                        print
                        print"-"*80
                        print"The Hundred-Foot Journey"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""The Kadam family clashes with Madame Mallory, proprietress of a celebrated
French restaurant,after they open their own nearby eatery, until undeniable chemistry
causes the Madame to take gifted young chef Hassan under her wing."""
                        print"-"*80
                        print
                        print
                    if choicegamma==3:
                        print
                        print                        
                        print"-"*80
                        print"Into The Storm"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Storm trackers, thrill-seekers, and everyday townspeople document an unprecedented
onslaught of tornadoes touching down in the town of Silverton."""
                        print"-"*80
                        print
                        print
                    if choicegamma==4:
                        print
                        print
                        print"-"*80
                        print"Step Up All In"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""All-stars from the previous Step Up installments come together in glittering Las Vegas,
battling for a victory that could define their dreams and their careers."""
                        print"-"*80
                        print
                        print
                    if choicegamma==5:
                        print
                        print
                        print"-"*80
                        print"What If"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Wallace, who is burned out from a string of failed relationships, forms an instant bond with Chantry,
who lives with her longtime boyfriend. Together, they puzzle out what it means if your best friend is also the
love of your life."""
                        print"-"*80
                        print
                        print
                    if choicegamma==6:
                        break
                    
            if choicebeta==2:
                print
                print"Out Now"
                loopalpha=1
                choicealpha=0
                while loopalpha==1:
                    print"-"*80
                    print"1)Guardians Of The Galaxy"
                    print"2)Dawn of the Planet of the Apes"
                    print"3)Get on Up"
                    print"4)Hercules"
                    print"5)Horns"
                    print"6)Go Back"
                    print"-"*80
                    choicegamma=input("Enter which section you would like to know about ? ")
                    if choicegamma==1:
                        print
                        print
                        print"-"*80
                        print"Guardians Of The Galaxy"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Light years from Earth, 26 years after being abducted Peter Quill finds himself the prime target of
a manhunt after discovering an orb wanted by Ronan the Accuser."""
                        print"-"*80
                        print
                        print
                    if choicegamma==2:
                        print
                        print
                        print"-"*80
                        print"Dawn of the Planet of the Apes"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""In the wake of a disaster that changed the world, the growing and genetically evolving apes find
themselves at a critical point with the human race."""
                        print"-"*80
                        print
                        print
                    if choicegamma==3:
                        print
                        print
                        print"-"*80
                        print"Get On Up"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""A chronicle of James Brown's rise from extreme poverty to become one of the most influential musicians in history"""
                        print"-"*80
                        print
                        print
                    if choicegamma==4:
                        print
                        print
                        print"-"*80
                        print"Hercules"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Having endured his legendary twelve labors, Hercules, the Greek demigod,
has his life as a sword-for-hire tested when the King of Thrace and his daughter seek his aid in defeating
a tyrannical warlord.."""
                        print"-"*80
                        print
                        print
                    if choicegamma==5:
                        print
                        print
                        print"-"*80
                        print"Horns"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""In the aftermath of his girlfriend's mysterious death, a young man awakens to strange horns sprouting from his temples."""
                        print"-"*80
                        print
                        print
                    if choicegamma==6:
                        break
                    
            if choicebeta==3:
                print
                print"Coming Soon"
                loopalpha=1
                choicealpha=0
                while loopalpha==1:
                    print"-"*80
                    print"1)The Expendables 3"
                    print"2)If I Stay"
                    print"3)The Maze Runner"
                    print"4)The Boxtrolls"
                    print"5)Book Of Life"
                    print"6)Go Back"
                    print"-"*80
                    choicegamma=input("Enter which section you would like to know about ? ")
                    if choicegamma==1:
                        print
                        print
                        print"-"*80
                        print"The Expendables 3"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Barney and his team, known as "The Expendables", come into conflict with ruthless arms dealer Conrad Stonebanks,
the Expendables' co-founder, who is determined to destroy the team."""
                        print"-"*80
                        print
                        print
                    if choicegamma==2:
                        print"-"*80
                        print"If I Stay"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Life changes in an instant for young Mia Hall after a car accident puts her in a coma. During an out-of-body experience,
she must decide whether to wake up and live a life far different than she had imagined."""
                        print"-"*80
                        print
                        print
                    if choicegamma==3:
                        print
                        print
                        print"-"*80
                        print"The Maze Runner"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Thomas is deposited in a community of boys after his memory is erased, soon learning they're all trapped in a maze
that will require him to join forces with fellow "runners" for a shot at escape."""
                        print"-"*80
                        print
                        print
                    if choicegamma==4:
                        print
                        print
                        print"-"*80
                        print"The Boxtrolls"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""A young orphaned boy raised by underground cave-dwelling trash collectors tries to save his
friends from an evil exterminator. Based on the children's novel 'Here Be Monsters' by Alan Snow."""
                        print"-"*80
                        print
                        print
                    if choicegamma==5:
                        print
                        print
                        print"-"*80
                        print"Book of Life"
                        print"-"*80
                        print
                        print"Plot Moneymary"
                        print
                        print"-"*80
                        print"""Manolo, a young man who is torn between fulfilling the expectations of his family and following his heart,
embarks on an adventure that spans three fantastical worlds where he must face his greatest fears."""
                        print"-"*80
                        print
                        print
                    if choicegamma==6:
                        break

            if choicebeta==4:
                break         
    if choicealpha==2:
        print"Welcome to the Ticket Counter"
        loopalpha=1
        choicealpha=0
        while loopalpha==1:
            print"-"*80
            print"1)Guardians Of The Galaxy"
            print"2)Dawn of the Planet of the Apes"
            print"3)Get on Up"
            print"4)Hercules"
            print"5)Horns"
            print"6)Go Back"
            print"-"*80

            choicebeta=input("Whcih movie would you like to watch ? ")
            if choicebeta==1:
               
                print"A fee of Qr.50 has been subtracted from your account"
                #Subtraction of Money from account
                #money=money=50
                print"Please proceed to Theatre 1"
                print"Thanks for Watching.Please come again."
            if choicebeta==2:
                
                print"A fee of Qr.50 has been subtracted from your account"
                #Subtraction of Money from account
                #money=money=50
                print"Please proceed to Theatre 2"
                print"Thanks for Watching.Please come again."
            if choicebeta==3:
               
                print"A fee of Qr.50 has been subtracted from your account"
                #Subtraction of Money from account
                #money=money=50
                print"Please proceed to Theatre 3"
                print"Thanks for Watching.Please come again."
            if choicebeta==4:
                
                print"A fee of Qr.50 has been subtracted from your account"
                #Subtraction of Money from account
                #money=money=50
                print"Please proceed to Theatre 4"
                print"Thanks for Watching.Please come again."
            if choicebeta==5:
                print"A fee of Qr.50 has been subtracted from your account"
                #Subtraction of Money from account
                
                #money=money=50
                print"Please proceed to Theatre 5"
                print"Thanks for Watching.Please come again."
            if choicebeta==6:
                break

    if choicealpha==3:
        print"Welcome to the Snack Counter"
        loopalpha=1
        choicealpha=0
        while loopalpha==1:
            print"-"*80
            print"We have the following items on the Menu"
            print"-"*80
            print" ITEM NAME                      PRICE "
            print"1)Popcorn                       Qr.15"
            print"2)French Fries                  Qr.10"
            print"3)Chicken Burger                Qr.25"
            print"4)Veggie Burger                 Qr.20"
            print"5)Drinks                        Qr.5"
        
            print"-"*80
            print"6)Go Back"
            print"-"*80
            print
            choicebeta=input("What would you like to buy ? ")
            if choicebeta==1:
                print"A fee of Qr.15 has been subtracted from your account"
                #Subtraction of Money from account
                print
            if choicebeta==2:
                print"A fee of Qr.10 has been subtracted from your account"
                #Subtraction of Money from account
                print
            if choicebeta==3:
                print"A fee of Qr.25 has been subtracted from your account"
                #Subtraction of Money from account
                print
            if choicebeta==4:
                print"A fee of Qr.20 has been subtracted from your account"
                #Subtraction of Money from account
                print
            if choicebeta==5:
                print"A fee of Qr.5 has been subtracted from your account"
                #Subtraction of Money from account
                print
            if choicebeta==6:
                print"Enjoy the Movie.Please visit us again."
                print
                loopalpha=0
    if choicealpha==4:
        print"Thanks for coming"
        print"Please visit us again.Goodbye"
        
################################################################################

def game():
    
    global pos_x,pos_y
    global enemyX,enemyY
    global score
    global staytime

    pygame.mixer.init()
    pygame.mixer.music.load("Mario.mp3")
    pygame.mixer.music.play(-1,0.0)

    
    class player(object):
   
        def __init__(self):
      
            self.rect = pygame.Rect(32, 32, 20, 20)

        def move(self,X,Y):

            if X!=0:
                self.move_single_axis(X,0)
                
                
            if Y!=0:
                self.move_single_axis(0,Y)
               

        def move_single_axis(self,X,Y):

            self.rect.x+=X
            self.rect.y+=Y

            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if X>0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if X<0:   
                     # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        
                    if Y > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        
                    if Y < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect):
                    if X>0:
                        self.rect.right = enemy.rect.left
                    if X<0:
                        self.rect.left = enemy.rect.left
                    if Y > 0:
                        self.rect.bottom = enemy.rect.top
                    if Y < 0:
                        self.rect.top = enemy.rect.bottom
                        
    X1=250
    Y1=250
    
    class enemyplayer(object):
   
        def __init__(self,enemyX,enemyY):
      
            self.rect = pygame.Rect(enemyX,enemyY,20,20)

        def moveenemy(self,X1,Y1):

            if X1!=0:
                self.killed(X1,0)
                
            if Y1!=0:

                self.killed(0,Y1)

            

        def killed(self,X1,Y1):

            self.rect.x+=X1
            self.rect.y+=Y1

            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if X1>0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if X1<0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    if Y1 > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    if Y1 < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom

            for play in playerlist:
                if self.rect.colliderect(play.rect):
                    if X1>0:
                        self.rect.right = play.rect.left
                    if X1<0:
                        self.rect.left = play.rect.left
                    if Y1 > 0:
                        self.rect.bottom = play.rect.top
                    if Y1 < 0:
                        self.rect.top = play.rect.bottom
                        


    class Wall(object):
    
        def __init__(self,w,x,y,z):
            walls.append(self)
            self.rect = pygame.Rect(w,x,y,z)

    class Enemy(object):
    
        def __init__(self,w,x,y,z):
            enemies.append(self)
            self.rect = pygame.Rect(w,x,y,z)
    

    walls=[]


    Wall(0, 0, 20, 250)
    Wall(0, 350, 20, 250)
    Wall(780, 0, 20, 600)
    Wall(20, 0, 760, 20)
    Wall(20, 580, 760, 20)
    Wall(250,230,300,10)
    Wall(500,280,10,200)
    Wall(550,230,10,200)
    Wall(250,230,10,250)
    Wall(250,480,350,10)
    Wall(600,180,10,310)
    Wall(200,180,10,300)
    Wall(200,180,400,10)
    Wall(0,410,20,100)
    Wall(300,280,200,10)
    Wall(300,280,10,100)
    Wall(300,430,10,50)
    Wall(350,330,10,150)
    Wall(350,330,100,10)
    Wall(450,330,10,100)
    Wall(350,430,40,10)
    Wall(430,430,30,10)
    Wall(150,130,500,10)
    Wall(150,130,10,400)
    Wall(150,530,500,10)
    Wall(650,130,10,200)
    Wall(650,380,10,160)


    pos_x=0
    pos_y=0

    
    
    pygame.init()
    GAMELOOP = False

    clock = pygame.time.Clock()
    playerlist=[]
    PLAYER=player()
    playerlist.append(PLAYER)
    enemies=[]
    
    ENEMY1=enemyplayer(220,500)
    ENEMY2=enemyplayer(610,210)
    ENEMY3=enemyplayer(310,450)
    ENEMY4=enemyplayer(530,340)
    
    enemies.append(ENEMY1)
    enemies.append(ENEMY2)
    enemies.append(ENEMY3)
    enemies.append(ENEMY4)
    
    score=0
    timer="0"
    
    while not GAMELOOP:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True

        key = pygame.key.get_pressed()
        
        

        if key[pygame.K_LEFT]:
            PLAYER.move(-5, 0)
        if key[pygame.K_RIGHT]:
            PLAYER.move(5, 0)
        if key[pygame.K_UP]:
            PLAYER.move(0, -5)
        if key[pygame.K_DOWN]:
            PLAYER.move(0, 5)

        if key[pygame.K_a]:
            ENEMY1.moveenemy(-7, 0)
        if key[pygame.K_d]:
            ENEMY1.moveenemy(7, 0)
        if key[pygame.K_w]:
            ENEMY1.moveenemy(0, -7)
        if key[pygame.K_s]:
            ENEMY1.moveenemy(0, 7)

        if PLAYER.rect.x>400 and PLAYER.rect.y>380 and PLAYER.rect.x<430 and PLAYER.rect.y<400:
            pos_x=120
            pos_y=320
            score=score+int(timer)
            Game2()

        if PLAYER.rect.x>620 and PLAYER.rect.x<640 and PLAYER.rect.y>210 and PLAYER.rect.y<230:
            if ENEMY2 in enemies:
                score=score-100
                enemies.remove(ENEMY2)
        if PLAYER.rect.x>320 and PLAYER.rect.x<340 and PLAYER.rect.y>450 and PLAYER.rect.y<470:
            if ENEMY3 in enemies:
                score=score-100
                enemies.remove(ENEMY3)
        if PLAYER.rect.x>500 and PLAYER.rect.x<560 and PLAYER.rect.y>300 and PLAYER.rect.y<360:
            if ENEMY4 in enemies:
                score=score-100
                enemies.remove(ENEMY4)


        hello.fill(BLACK)

        
        for wall in walls:
            pygame.draw.rect(hello,SKY,wall.rect)
        for play in playerlist:
            pygame.draw.rect(hello,GOLD,PLAYER.rect)
       
        for enemy in enemies:
            pygame.draw.rect(hello,GREY,enemy.rect)
        pygame.draw.rect(hello,RED,ENEMY1.rect)
        

        Exit=pygame.font.SysFont("castellar",20)
        exitfont=Exit.render("SCORE :",True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(360,50)
        hello.blit(exitfont,Exiter)
        

        Exit=pygame.font.SysFont("castellar",20)
        exitfont=Exit.render(timer,True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(460,50)
        hello.blit(exitfont,Exiter)
        
        
        
        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("HERE!",True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(400,400)
        hello.blit(exitfont,Exiter)

        exitfont=Exit.render("GET THE GREY ONES AND IMPROVE YOUR SCORE !",True,GOLD)
        Exiter=exitfont.get_rect()
        Exiter.center=(400,110)
        
        hello.blit(exitfont,Exiter)
        
        timer=str(int(timer)+1)
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    
###############################################################################

def Game2():
    
    global pos_x,pos_y
    global score
    global staytime

    
    class player(object):
   
        def __init__(self):
      
            self.rect = pygame.Rect(32, 32, 20, 20)

        def move(self,X,Y):

            if X!=0:
                self.move_single_axis(X,0)
                
                
            if Y!=0:
                self.move_single_axis(0,Y)
               

        def move_single_axis(self,X,Y):

            self.rect.x+=X
            self.rect.y+=Y

            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if X>0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if X<0:   
                     # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        
                    if Y > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        
                    if Y < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom

            for block in blocks:
                if self.rect.colliderect(block.rect):
                    if X>0: # Moving right; Hit the left side of the wall
                        self.rect.right = block.rect.left
                    if X<0:   
                     # Moving left; Hit the right side of the wall
                        self.rect.left = block.rect.right
                        
                    if Y > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = block.rect.top
                        
                    if Y < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = block.rect.bottom

            for enemy in enemies:
                if self.rect.colliderect(enemy.rect):
                    
                        
                    if Y < 0: # Moving up; Hit the bottom side of the wall
                        displayscore("YOU GOT SHOT!","Better luck next time",40)
    class enemyplayerbullet(object):
   
        def __init__(self,enemyX,enemyY):
      
            self.rect = pygame.Rect(enemyX,enemyY,20,20)

        def moveenemybullet(self,X11,Y11):

            if X11!=0:
                self.killed(X11,0)
                
            if Y11!=0:

                self.killed(0,Y11)

            

        def killed(self,X11,Y11):

            self.rect.x+=X11
            self.rect.y+=Y11

            for player in playerlist:
                if self.rect.colliderect(player.rect):
                    
                        
                    if Y11 < 0: # Moving up; Hit the bottom side of the wall
                        displayscore("YOU GOT SHOT!","Better luck next time",40)

         
                        
    class enemyplayer(object):
   
        def __init__(self,enemyX,enemyY):
      
            self.rect = pygame.Rect(enemyX,enemyY,20,20)

        def moveenemy(self,X1,Y1):

            if X1!=0:
                self.killed(X1,0)
                
            if Y1!=0:

                self.killed(0,Y1)

            

        def killed(self,X1,Y1):

            self.rect.x+=X1
            self.rect.y+=Y1
            
    class Wall(object):
    
        def __init__(self,x,y):
            walls.append(self)
            self.rect = pygame.Rect(x,y,20,20)

    class Block(object):
    
        def __init__(self,x,y):
            blocks.append(self)
            self.rect = pygame.Rect(x,y,20,20)
    class Enemy(object):
    
        def __init__(self,w,x,y,z):
            enemies.append(self)
            self.rect = pygame.Rect(w,x,y,z)

    
    walls=[]
    blocks=[]
    enemies=[]
    bullets=[]
    ENEMY1=enemyplayer(220,550)
    enemies.append(ENEMY1)
    BULLET1=enemyplayerbullet(220,550)
    BULLET2=enemyplayerbullet(220,550)
    BULLET3=enemyplayerbullet(220,550)
    BULLET4=enemyplayerbullet(220,550)
    BULLET5=enemyplayerbullet(220,550)
    BULLET6=enemyplayerbullet(220,550)
    BULLET7=enemyplayerbullet(220,550)
    BULLET8=enemyplayerbullet(220,550)
    BULLET9=enemyplayerbullet(220,550)
    BULLET10=enemyplayerbullet(220,550)
    BULLET11=enemyplayerbullet(220,550)
    bullets.append(BULLET1)
    maze=[
    "M  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
    "M  M                                  MM",
    "M  M  MMMMM  MM  MMMMMMMMMMMMMMMMMMMMMMM",
    "M     MM     MM                       MM",
    "M     MM  MMMMMMMMMM   MMMMMMMM  MM   MMM",
    "M  MMMMM  MMMMMMMMMM   MMMMMMMM  MM   MMM",
    "M  MM     MM                 MM  MM   MMM",
    "M  MMMMMMMMM   MMMMMMMMMMM   MMMMMM   MMM",
    "MMMMMMMMMMMM            MM   MM       MMM", 
    "MMMMMMM   MM   MMMMMMMMMMM   MM   MMMMMMM",
    "M         MM   MM            MM       MMM",
    "MMMMMMM   MM   MM   MMMMMM   MM  MM   MMM",
    "M    MM   MM   MMMMMMMMMMM   MM  MM   MMM",
    "M    MM   MM                 MMMMMM   MMM",
    "M   MMM   MMMMMMMMM   MMMMMMMMMM      MMM",
    "M         MMMMMMMMM   MMMMMMM      MMMMMM",
    "MMMMMMMMMMMM          MMMMMMM   MMMMMMMMM   ",
    "MMMMMMMMMMMMMMMMMMMMMMMM        MMMM  MMM",
    "M                     MMMMMMMWWWMMMM  MMM",
    "M    MMMMMMMMMMMMMM   MM   MM   MMMM  MMM",
    "M    MMMMMMMMMMMMMM        MM         MMM",
    "M                               MMMMMMMMM",
    "M    MMMMMMMMMMMMMMMMMMMMMMMM         MMM",
    "M    MMMMMMMMMMMMMMMMMMMMMMMMMMMM   MMMMM",
    "M  MMMMMMMMMMMMM              MMM   MMMMM",
    "M  MMMMMMMMMMMMM   MMMMM   MMMMMM   MMMMM",
    "M                  MMMMM   MMMMMM   MMMMM",
    "MNMMMMMMMMMMMMMM   MMMMM       MMMMMMMMMM",
    "MMMMMMMMMMMMMMMM   MMMMMMMMM   MMMMMMMMMM",
    "MMMMMMMMMMMMMMMMMMMMMMMMMMMM   MMMMMMMMMM"
    ]

    x,y=0,0
    
    for row in maze:
        for col in row:
            if col=="M":
                Wall(x,y)
            if col=="W":
                Block(x,y)
            x+=20
        y+=20
        x=0
    

    pos_x=0
    pos_y=0

    
    slow=0
    pygame.init()
    
    GAMELOOP = False

    clock = pygame.time.Clock()
    playerlist=[]
    PLAYER=player()
    playerlist.append(PLAYER)
    timer=str(score)

    def displayscore(message,x,size):
        pygame.init()

        

        SCORELOOP= False

        while not SCORELOOP:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    SCORELOOP=True

            key = pygame.key.get_pressed()

            if key[pygame.K_RETURN]:
                Gamezone()

            hello.fill(BLACK)

            Scoredisplay=pygame.font.SysFont("stencil",40)
            yourscore=Scoredisplay.render(message,True,RED)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,200)
            hello.blit(yourscore,Exiter)



            Scoredisplay=pygame.font.SysFont("stencil",size)
            yourscore=Scoredisplay.render(x,True,RED)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,300)
            hello.blit(yourscore,Exiter)

            Scoredisplay=pygame.font.SysFont("monospace",20)
            yourscore=Scoredisplay.render("Press Enter to Exit",True,GREY)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,400)
            hello.blit(yourscore,Exiter)


            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

            

            

        
    count=0
    
    while not GAMELOOP:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True

        key = pygame.key.get_pressed()
        
        

        if key[pygame.K_LEFT]:
            PLAYER.move(-5, 0)
        if key[pygame.K_RIGHT]:
            PLAYER.move(5, 0)
        if key[pygame.K_UP]:
            PLAYER.move(0, -5)
        if key[pygame.K_DOWN]:
            PLAYER.move(0, 5)
        

        if key[pygame.K_a]:
            ENEMY1.moveenemy(-1, 0)
            BULLET1.moveenemybullet(-1,0)
            BULLET2.moveenemybullet(-1,0)
            BULLET3.moveenemybullet(-1,0)
            BULLET4.moveenemybullet(-1,0)
            BULLET5.moveenemybullet(-1,0)
            BULLET6.moveenemybullet(-1,0)
            BULLET7.moveenemybullet(-1,0)
            BULLET8.moveenemybullet(-1,0)
            BULLET9.moveenemybullet(-1,0)
            BULLET10.moveenemybullet(-1,0)
            BULLET11.moveenemybullet(-1,0)
        if key[pygame.K_d]:
            ENEMY1.moveenemy(1, 0)
            BULLET1.moveenemybullet(1,0)
            BULLET2.moveenemybullet(1,0)
            BULLET3.moveenemybullet(1,0)
            BULLET4.moveenemybullet(1,0)
            BULLET5.moveenemybullet(1,0)
            BULLET6.moveenemybullet(1,0)
            BULLET7.moveenemybullet(1,0)
            BULLET8.moveenemybullet(1,0)
            BULLET9.moveenemybullet(1,0)
            BULLET10.moveenemybullet(1,0)
            BULLET11.moveenemybullet(1,0)
        if key[pygame.K_w]:
            ENEMY1.moveenemy(0, -1)
            BULLET1.moveenemybullet(0,-1)
            BULLET2.moveenemybullet(0,-1)
            BULLET3.moveenemybullet(0,-1)
            BULLET4.moveenemybullet(0,-1)
            BULLET5.moveenemybullet(0,-1)
            BULLET6.moveenemybullet(0,-1)
            BULLET7.moveenemybullet(0,-1)
            BULLET8.moveenemybullet(0,-1)
            BULLET9.moveenemybullet(0,-1)
            BULLET10.moveenemybullet(0,-1)
            BULLET11.moveenemybullet(0,-1)
        if key[pygame.K_s]:
            ENEMY1.moveenemy(0, 1)
            BULLET1.moveenemybullet(0,1)
            BULLET2.moveenemybullet(0,1)
            BULLET3.moveenemybullet(0,1)
            BULLET4.moveenemybullet(0,1)
            BULLET5.moveenemybullet(0,1)
            BULLET6.moveenemybullet(0,1)
            BULLET7.moveenemybullet(0,1)
            BULLET8.moveenemybullet(0,1)
            BULLET9.moveenemybullet(0,1)
            BULLET10.moveenemybullet(0,1)
            BULLET11.moveenemybullet(0,1)
        
        if key[pygame.K_z]:
            
                
            for bullet in bullets:
                bullet.moveenemybullet(0,slow)
            
            

        
        

    
            

        if PLAYER.rect.x>580 and PLAYER.rect.y>560 and PLAYER.rect.x<620:
            pos_x=120
            pos_y=320
            score=score+int(timer)
            displayscore("Your score is:",timer,40)

        if PLAYER.rect.x>300 and PLAYER.rect.x<350 and PLAYER.rect.y>200 and PLAYER.rect.y<300:
            pos_x=120
            pos_y=320
            score=score+int(timer)
            displayscore("YOU DIED!","DARKNESS IS DECEIVING",40)
        if PLAYER.rect.x>400 and PLAYER.rect.y>80 and PLAYER.rect.y<150 and PLAYER.rect.x<580:
            for block in blocks:
                if block.rect.x>400 and block.rect.y>80:
                    blocks.remove(block)

        hello.fill(BLACK)
        

        for wall in walls:
            pygame.draw.rect(hello,BLUE,wall.rect)

        for block in blocks:
            pygame.draw.rect(hello,RED,block.rect)

        for enemy in enemies:
            pygame.draw.rect(hello,GREY,enemy.rect)

        for bullet in bullets:
            for i in range(10):
                pygame.draw.rect(hello,GOLD,bullet.rect)
            
        pygame.draw.rect(hello,WHITE,PLAYER.rect)
        

        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render(timer,True,PURPLE)
        Exiter=exitfont.get_rect()
        Exiter.center=(150,400)
        hello.blit(exitfont,Exiter)

        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("THE ENEMY IS WEAK. NOT.",True,RED)
        Exiter=exitfont.get_rect()
        Exiter.center=(160,580)
        hello.blit(exitfont,Exiter)
        
        
        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("HERE!",True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(590,580)
        hello.blit(exitfont,Exiter)

        if slow>-100:
            slow=slow-1
        timer=str(int(timer)+1)
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

###############################################################################

def CLOTHINGZONE():
    List = []
    global n

    print"*"*60
    print"               Welcome To Clothing Zone"
    print"*"*60
    def mainMenu():
        print
        print
        print"Choose your options:"
        print"1. Add Items"
        print"2. Remove Items"
        print"3. Print Items"
        print"4. Quit" 
        choice = int(input("> ")) 
        return choice 

    def addItem():
        print
        print
        s=raw_input("Enter Gender:")
        if s=="m" or s=="M":
            print
            print"Choose your options:"
            print"1. Kurtas"
            print"2. Jeans"
            print"3. Casual Shirts"
            print"4. Formal Shirts"
            print("What item would you like to add?") 
            item = raw_input("> ") 
            if item not in List: 
                List.append(item) 
            elif item in List: 
                print("That item is already in your list.\n")

        if s=="F" or s=="f":
            print
            print"Choose your options:"
            print"1. Dresses"
            print"2. Salvar Suit"
            print"3. JumpSuits"
            print"4. Shorts"
            print"5. Tees"
            item = raw_input("> ") 
            if item not in List: 
                List.append(item) 
            elif item in List: 
                print("That item is already in your list.\n")
    
    

    def removeItem(): 
        print("Your shopping list contains:")
    
        i = 0 
        while i in range(len(List)): 
            print(List[i]) 
            i = i + 1
        print
        print("What would you like to remove?") 
        item = raw_input("> ") 
        if item not in List: 
            print("That doesn't seem to be a part of your list.") 
        elif item in List: 
            itemIndex = List.index(item)
            del List[itemIndex] 


    menuChoice=mainMenu()

    while menuChoice not in [1,2,3,4]: 
        print("Invalid entry") 


    while menuChoice in [1,2,3,4]: 
            if menuChoice == 1: 
                addItem() 
            r=raw_input("Do you want to continue: (Y?N)")
            if r=="Y":
                menuChoice=mainMenu()
            if r=="N":
                print"You can collect your item from the Cash Counter ! Thank You for Shopping!"
                break
            elif menuChoice == 2: 
                removeItem() 
            r=raw_input("Do you want to continue: (Y?N)")
            if r=="Y":
                menuChoice=mainMenu()
            if r=="N":
                print"You can collect your item from the Cash Counter ! Thank You for Shopping!"
                break 

            elif menuChoice == 3: 

                i = 0 
            print("Your  list contains:") 
            while i in range(len(List)): 
                print(List[i]) 
                i = i + 1
            r=raw_input("Do you want to continue: (Y?N)")
            if r=="Y":
                menuChoice=mainMenu()
            if r=="N":
                print"You can collect your item from the Cash Counter ! Thank You for Shopping!"
                break     
            else: 
                print"You can collect your item from the Cash Counter ! Thank You for Shopping!"
                break     




###############################################################################
def VirtualShop():
    
    global cloth
    global staytime
    
    
    x_speed=0
    y_speed=0
    
    
    keepingcount=1
    global pos_x,pos_y
    global n
    n=1
    
    
    pos_x,pos_y=200,50
    pygame.init()
    listitem=["jacket.jpg","DC.png","top.jpg","superman.jpg"]
    clock = pygame.time.Clock()
    thepic=pygame.image.load("DC.png")
    
    apple=pygame.image.load("Apple.jpg")
    
    clothitems=["Nike Jacket","DC","Superman Tshirt"]
    cloth=clothitems[1]
    
    def BUY(cloth):
        
        pygame.init()
        
        SCORELOOP=False
        while not SCORELOOP:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    SCORELOOP=True

            key = pygame.key.get_pressed()

            if key[pygame.K_RETURN]:
                VirtualShop()

            hello.fill(WHITE)

            display=pygame.font.SysFont("calibri",20)
            yourscore=display.render("You just bought ",True,RED)
            Exiter=yourscore.get_rect()
            Exiter.center=(220,300)
            hello.blit(yourscore,Exiter)

            display=pygame.font.SysFont("calibri",20)
            yourscore=display.render(cloth,True,RED)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,300)
            hello.blit(yourscore,Exiter)

            Scoredisplay=pygame.font.SysFont("monospace",20)
            yourscore=Scoredisplay.render("Press Enter to Exit",True,GREY)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,400)
            hello.blit(yourscore,Exiter)


            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

        
        
        
    GAMELOOP = False

    while not GAMELOOP:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True
                
            if event.type==pygame.MOUSEBUTTONUP:
                
                pos=pygame.mouse.get_pos()
                for i in range(len(pos)):
                    if i%2==0:
                        pos_x=pos[i]
                    else:
                        pos_y=pos[i]

                if pos>(100,280) and pos<(200,350):
                    if n>0:
                        n=n-1
                if pos>(600,280) and pos<(750,350):
                    if n<(len(listitem)-1):
                        n=n+1
                
                        
                
                        

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 100
                elif event.key == pygame.K_RIGHT:
                    x_speed = 100
                
            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
              
        if pos_x>650 and pos_y>480:
            pos_x=50
            pos_y=400
            thebase()
            
            
        if pos_x>100 and pos_x<200 and pos_y>280 and pos_y<350:
            thepic=pygame.image.load(listitem[n])
            
        if pos_x>600 and pos_x<750 and pos_y>280 and pos_y<350:
            thepic=pygame.image.load(listitem[n])

        if pos_x>220 and pos_x<300 and pos_y>520 and pos_y<600:
           
            BUY(cloth)
            
            
        
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed
    
            


        hello.fill(BLACK)
        hello.blit(apple,[-10,0])
        hello.blit(thepic,[200,50])


        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("Buy",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(220,540)
        hello.blit(yourscore,Exiter)

        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("Discard",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(520,540)

        hello.blit(yourscore,Exiter)
        
        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("EXIT",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(700,520)

        Scoredisplay=pygame.font.SysFont("calibri",50)
        yourscore=Scoredisplay.render("<",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(100,300)
        hello.blit(yourscore,Exiter)

        Scoredisplay=pygame.font.SysFont("calibri",50)
        yourscore=Scoredisplay.render(">",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(700,300)
        hello.blit(yourscore,Exiter)

        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("EXIT",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(700,520)
        hello.blit(yourscore,Exiter)

    
            
            
        pygame.draw.rect(hello,WHITE,[-20,31,840,540],2)
        pygame.draw.rect(hello,WHITE,[650,470,100,100],2)
        pygame.draw.rect(hello,WHITE,[150,510,150,50],2)
        pygame.draw.rect(hello,WHITE,[450,510,150,50],2)
        
        
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    
def Clothing():

    global a,b
    global cloth
    a,b=0,0
    global staytime
    x_speed=0
    y_speed=0
    global n
    n=1
    
    keepingcount=1
    global pos_x,pos_y
    pygame.init()
    clock = pygame.time.Clock()
    thepic=pygame.image.load("clothes.png")

    GAMELOOP = False

    while not GAMELOOP:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True
            if event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                for i in range(len(pos)):
                    if i%2==0:
                        pos_x=pos[i]
                    else:
                        pos_y=pos[i]
                
        

            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0
    

        if pos_x>650 and pos_y>480:
            pos_x=50
            pos_y=400
            VirtualShop()
            
        
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed
    
            


        hello.fill(BLACK)
        hello.blit(thepic,[-10,30])

        c="WELCOME TO SPLASH!"
      
        
        a=c[0:n]

        Scoredisplay=pygame.font.SysFont("calibri",30)
        yourscore=Scoredisplay.render(a,True,BLUE)
        Exiter=yourscore.get_rect()
        Exiter.center=(400,500)
        hello.blit(yourscore,Exiter)
        
        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("SHOP",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(700,520)
        hello.blit(yourscore,Exiter)
        
        if keepingcount%5==0:
            
            n=n+1
        elif keepingcount==95:
            keepingcount=0.34
        keepingcount=keepingcount+1
        

    
            
            
        pygame.draw.rect(hello,BLUE,[-20,31,840,540],2)
        pygame.draw.rect(hello,BLUE,[650,470,100,100],2)
        
        mario(hi, pos_x, pos_y)
        
        
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def ATM():


    global staytime
    x_speed=0
    y_speed=0
    global n
    n=1
    
    keepingcount=1
    global pos_x,pos_y
    pygame.init()
    clock = pygame.time.Clock()
    thepic=pygame.image.load("atmpic.jpg")

    GAMELOOP = False

    while not GAMELOOP:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0
    

        if pos_x>650 and pos_y>480:
            pos_x=650
            pos_y=400
            thebase()
            
        if pos_x>250 and pos_x<300 and pos_y>520:
            pos_x=250
            pos_y=400
            ATM2()
            
        
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed
    
            


        hello.fill(BLACK)
        hello.blit(thepic,[0,100])
        
        c="TRIDA ATM WELCOMES YOU!"
      
        
        a=c[0:n]

        Scoredisplay=pygame.font.SysFont("CALIBRI",30)
        yourscore=Scoredisplay.render(a,True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(400,35)
        hello.blit(yourscore,Exiter)
        
        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("Exit",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(700,520)
        hello.blit(yourscore,Exiter)

        Scoredisplay=pygame.font.SysFont("calibri",20)
        yourscore=Scoredisplay.render("RECEPTION",True,WHITE)
        Exiter=yourscore.get_rect()
        Exiter.center=(250,520)
        hello.blit(yourscore,Exiter)
        
        if keepingcount%5==0:
            
            n=n+1
        elif keepingcount==95:
            keepingcount=0.34
        keepingcount=keepingcount+1
        

    
            
            
        pygame.draw.rect(hello,WHITE,[-20,51,840,540],2)
        pygame.draw.rect(hello,WHITE,[650,470,100,100],2)
        pygame.draw.rect(hello,WHITE,[200,470,100,100],2)
        
        mario(hi, pos_x, pos_y)
        
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


    

    


def thebase():

    global staytime
    global pos_x,pos_y

    
    

    pygame.init()

    
    GAMELOOP = False

    clock = pygame.time.Clock()

    x_speed = 0
    y_speed = 0

    mariowallpaper=pygame.image.load("Basewallpaper.png")
    themall=pygame.image.load("gamezonefont.png")
    timeline=""
    
    def malltiming(staytime):
        pygame.init()

        if float(staytime)<600.0:
            change=float(staytime)
            change=change/10
            staytime=str(change)
            timeline="seconds"

        elif float(staytime)>=600.0:
            change=float(staytime)
            change=change/600
            change=round(change,2)
            staytime=str(change)
            timeline="minutes"
            

        

        SCORELOOP= False

        while not SCORELOOP:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    SCORELOOP=True

            key = pygame.key.get_pressed()

            if key[pygame.K_RETURN]:
                import exit

            hello.fill(BLACK)

            Scoredisplay=pygame.font.SysFont("calibri",30)
            yourscore=Scoredisplay.render("Your time at THE ELITE MALL is:",True,BLUE)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,200)
            hello.blit(yourscore,Exiter)

            Scoredisplay=pygame.font.SysFont("calibri",30)
            yourscore=Scoredisplay.render(timeline,True,BLUE)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,360)
            hello.blit(yourscore,Exiter)



            Scoredisplay=pygame.font.SysFont("stencil",100)
            yourscore=Scoredisplay.render(staytime,True,WHITE)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,300)
            hello.blit(yourscore,Exiter)

            Scoredisplay=pygame.font.SysFont("monospace",20)
            yourscore=Scoredisplay.render("Press Enter to Exit",True,GREY)
            Exiter=yourscore.get_rect()
            Exiter.center=(400,400)
            hello.blit(yourscore,Exiter)


            pygame.display.flip()
            clock.tick(60)

        pygame.quit()



    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True

            if event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                for i in range(len(pos)):
                    if i%2==0:
                        pos_x=pos[i]
                    else:
                        pos_y=pos[i]
            

            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            elif event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0

        if (pos_x)<-15 and (pos_y<300) and (pos_y>250):
            Gamezone()
            #left second
        if (pos_x)<-15 and (pos_y<200):
            MOVIEZONE()
            
        if (pos_x)<-15 and (pos_y>300 and pos_y<500):
            Clothing()
        if ((pos_x)<-15) and (pos_y>500):
            COMSERV()
            pos_x=0
            pos_y=530
        
            
            #left fourth
        if ((pos_x)>780) and (pos_y<200):
            grocery()
            
            #right first
        if (pos_x>780) and (pos_y<300):
            foodcourt()
            #right second
        if (pos_x)>780 and (pos_y>300 and pos_y<500):
            ATM()
            pos_x=720
            pos_y=350
        if (pos_x)>780 and (pos_y>500):
            FIFA()
            #right fourth

        if ((pos_x)>450) and (pos_y>580):
            pygame.mixer.quit()
            malltiming(staytime)
    


    
        pos_x = pos_x + x_speed
        pos_y = pos_y + y_speed


        hello.fill(WHITE)
        hello.blit(mariowallpaper,[0,80])
        hello.blit(themall,[200,25])
        
        walls=[[0,0,20,134,WHITE],[0,185,20,65,WHITE],[20,80,760,5,WHITE],[780,430,20,100,WHITE],[0,430,20,100,WHITE],[0,300,20,80,WHITE],[780,300,20,80,WHITE],[780,0,20,134,WHITE],[780,185,20,65,WHITE],[0,0,800,20,WHITE],[520,580,300,20,WHITE],[370,580,80,20,WHITE],[0,580,300,20,WHITE]]
        for item in walls:
    
            pygame.draw.rect(hello,RED,[item[0],item[1],item[2],item[3]],2)
        
        
    
        pygame.draw.rect(hello,WHITE,(680,250,150,50),2)
        pygame.draw.rect(hello,WHITE,(0,250,120,50),2)
        pygame.draw.rect(hello,WHITE,(0,530,120,50),2)
        pygame.draw.rect(hello,WHITE,(680,530,150,50),2)
        pygame.draw.rect(hello,WHITE,(450,540,70,60),2)
        pygame.draw.rect(hello,WHITE,(300,540,70,60),2)
        pygame.draw.rect(hello,WHITE,(0,380,120,50),2)
        pygame.draw.rect(hello,WHITE,(680,380,120,50),2)
        pygame.draw.rect(hello,WHITE,(0,134,120,50),2)
        pygame.draw.rect(hello,WHITE,(680,134,120,50),2)
        
        
        
        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("  FOODCOURT",True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(735,275)
        hello.blit(exitfont,Exiter)

        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("  GAMEZONE",True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(60,275)
        hello.blit(exitfont,Exiter)


        Exit=pygame.font.SysFont("calibri",20)
        exitfont=Exit.render("GROCERY",True,WHITE)
        Exiter=exitfont.get_rect()
        Exiter.center=(740,160)
        hello.blit(exitfont,Exiter)

        Exit1=pygame.font.SysFont("calibri",20)
        exitfont1=Exit1.render("EXIT",True,WHITE)
        Exiter1=exitfont1.get_rect()
        Exiter1.center=(485,565)
        hello.blit(exitfont1,Exiter1)

        Exit1=pygame.font.SysFont("calibri",20)
        exitfont1=Exit1.render("ENTER",True,WHITE)
        Exiter1=exitfont1.get_rect()
        Exiter1.center=(335,565)
        hello.blit(exitfont1,Exiter1)


        Exit1=pygame.font.SysFont("calibri",20)
        exitfont1=Exit1.render("ATM",True,WHITE)
        Exiter1=exitfont1.get_rect()
        Exiter1.center=(740,405)
        hello.blit(exitfont1,Exiter1)

        exitfont1=Exit1.render("SPLASH",True,WHITE)
        Exiter1=exitfont1.get_rect()
        Exiter1.center=(60,405)
        hello.blit(exitfont1,Exiter1)

        

        Exit12=pygame.font.SysFont("calibri",20)
        exitfont12=Exit12.render("             FIFA 2014",True,WHITE)
        Exiter12=exitfont12.get_rect()
        Exiter12.center=(700,550)
        hello.blit(exitfont12,Exiter12)

        FONT1=pygame.font.SysFont('arial',15)
        SURFACEFONT=FONT1.render('                       CUSTOMER CARE',True,WHITE)
        SURFACER=SURFACEFONT.get_rect()
        SURFACER.center=(23,555)
        hello.blit(SURFACEFONT,SURFACER)

        Hi1=pygame.font.SysFont("calibri",20)
        doorfont=Hi1.render("         CINEMA",True,WHITE)
        Hier=doorfont.get_rect()
        Hier.center=(35,160)
        hello.blit(doorfont,Hier)
   
    
        
        staytime=float(staytime)+0.2
        staytime=str(round(staytime,1))
        mario(hi, pos_x, pos_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

pygame.mixer.init()
pygame.mixer.music.load("Pirate.mp3")
pygame.mixer.music.play(-1,0.0)
   
thebase()


