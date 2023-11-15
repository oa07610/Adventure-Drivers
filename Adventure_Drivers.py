from tkinter import *
import time
import random
winner = False


#Initial Co-ordinates

blue_car_x = 0     #this is blue car
blue_car_y = 30

white_car_x = 0         #this is the white car
white_car_y = 250

teal_car_x= 0               #this is the teal car
teal_car_y = 110


#Actual Game Function:

def start_game(canvas2,top):

    global white_car_x
    global teal_car_x
    global blue_car_x
    global winner

    #Attaching images to canvas
    blue_car = canvas2.create_image(blue_car_x,blue_car_y, anchor=NW, image=blue_img)        #blue
    teal_car = canvas2.create_image(teal_car_x,teal_car_y, anchor=NW, image=teal_img)    #teal
    white_car = canvas2.create_image(white_car_x,white_car_y, anchor=NW, image=white_img)               #white

    side_track1 = canvas2.create_image(0,0, anchor=NW, image=side_track_img)
    side_track2 = canvas2.create_image(0,340, anchor=NW, image=side_track_img)

    track1 = canvas2.create_image(0,150, anchor=NW, image=track1_img)
    track2 = canvas2.create_image(0,240, anchor=NW, image=track2_img)

    while winner == False:
        time.sleep(0.07)
        random_move_white_car = random.randint(0,20)
        random_move_blue_car = random.randint(0,20)
        random_move_teal_car = random.randint(0,20)

        teal_car_x += random_move_white_car
        blue_car_x += random_move_blue_car
        white_car_x += random_move_teal_car

        move_cars(random_move_teal_car,random_move_white_car,random_move_blue_car,white_car,teal_car,blue_car,canvas2)
        top.update()
        winner = check_winner()

    if winner == "Tie":
        Label(top,text=winner,font=('open sans',22),fg='red').place(x=200,y=450)
    elif winner == "SORRY!! You LOST":
        Label(top,text=winner+". ",font=('open sans',22),fg='red',bg='white').place(x=200,y=450)
    else:
        Label(top,text=winner,font=('open sans',22),fg='red',bg='white').place(x=200,y=450)

#Movement of cars

def move_cars(random_move_teal_car,random_move_white_car,random_move_blue_car,white_car,teal_car,blue_car,canvas2):
    canvas2.move(white_car,random_move_white_car,0)
    canvas2.move(teal_car,random_move_teal_car,0)
    canvas2.move(blue_car,random_move_blue_car,0)

#Checking winner

def check_winner():
    s=select.get()
    if white_car_x >= 670 and teal_car_x >=670 and blue_car_x >=670:
        return "TIE!!"
    if teal_car_x >= 650:
        if s == "White Falcon":
            z = "Congrats!! You Won."
            return (z)
        else:
            return "Sorry!! You Lost."
    if white_car_x >= 670:
        if s=="Racing Shelby":
            z = "Congrats!! You Won."
            return (z)
        else:
            return "Sorry!! You Lost."
    if blue_car_x >= 670:
        if s == "Blue Thunder":
            z = "Congrats!! You Won."
            return (z)
        else:
            return "Sorry!! You Lost."
    return False

#Main Screen

main_screen = Tk()
main_screen.title('Adventure Drivers')
main_screen.geometry('940x601')
canvas = Canvas(main_screen,width=950,height=601) 

#Start Screen
ss = PhotoImage(file="./bg.png")
bg2 = PhotoImage(file="./bg2.png")

#Background image
bg_label=Label(main_screen, image=ss)
bg_label.place(x=0,y=0,relwidth=1,relheight=1) 
canvas.pack()     

select= StringVar() 
select.set('Choose your player:')


#Cars Images
blue_img = PhotoImage(file="./OW.png")    #blue
white_img = PhotoImage(file="./PL.png")        #white
teal_img = PhotoImage(file="./TT.png")  #green


#Side Track image
side_track_img = PhotoImage(file="./side_track.png") 


#Track images 
track1_img =  PhotoImage(file="./track.png")
track2_img =  PhotoImage(file="./track.png")


#Sizing the cars
blue_img = blue_img.zoom(6)
blue_img = blue_img.subsample(180)
white_img = white_img.zoom(8)
white_img = white_img.subsample(65)
teal_img = teal_img.zoom(17)
teal_img = teal_img.subsample(95)


#New Race window

def window():
    top=Toplevel(main_screen)
    top.geometry('750x510')
    top.title('Race')
    top.config(background='white')
    canvas2 = Canvas(top,width=750,height=400,bg='#808080')
    canvas2.pack(pady=20)

    #Calling game function
    start_game(canvas2,top)
    
#Player Selection

def selection():
    bg_label_2=Label(main_screen, image=bg2) 
    bg_label_2.place(x=0,y=0,relwidth=1,relheight=1)  

    #Drop Down Boxes
    options=["Blue Thunder",'White Falcon',"Racing Shelby"]
    drop = OptionMenu(main_screen,select,*options)
    drop.place(x=390,y=190) 

    #Window2 buttons 
    b1 = Button(main_screen,text="Let's Race!",height=1,width = 13,fg='white',bg='red',font=('open sans bold',14),command=window,borderwidth=0)
    b1.place(x=390,y=355)

#Designing Labels
b1 = Button(main_screen,text='Play!',height=1,width = 10,bg='red',fg='white',font=('open sans bold',14),command=selection)
b1.place(x=415,y=415)

main_screen.mainloop()
