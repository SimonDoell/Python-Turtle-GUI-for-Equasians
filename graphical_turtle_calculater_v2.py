import turtle
import time
import tkinter
import math


#turtle stuff
sc = turtle.Screen()
sc.setup(800,400) 
sc.bgcolor("white")

turtle = turtle.Turtle()
turtle.speed(10)
turtle.shape("circle")
turtle.turtlesize(0.3)
turtle.color("red")
turtle.pencolor("blue")



def draw_cross(color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(0, 400)
    turtle.pendown()
    turtle.goto(0, -400)
    turtle.penup()
    turtle.goto(-800, 0)
    turtle.pendown()
    turtle.goto(800, 0)
    turtle.goto(0, 0)
    turtle.pencolor("blue")
    
draw_cross("red")

def linear_graph(m_var, n_var):
    turtle.pencolor("black")
    m = m_var
    n = n_var

    def draw_graph(minus_or_plus_one):
        counter = 0
        i = 0
        while True:
            if counter > 0:
                i += minus_or_plus_one
                turtle.goto(i+1, (i+1)*m+n)
                if turtle.ycor() >= 400 or turtle.xcor() >= 800:
                    break
            else:
                turtle.penup()
                turtle.goto(i+1, (i+1)*m+n)
                turtle.pendown()
                counter += 1
           
        i = 0
        while True:
            i -= minus_or_plus_one
            turtle.goto(i-1, (i-1)*m+n)
            turtle.pendown()
            if turtle.ycor() <= -400 or turtle.xcor() <= -800:
                break
     
    if m >= 0:    
        draw_graph(1)
    else:
        draw_graph(-1)
    turtle.penup()    
    turtle.goto(0, 0)
    turtle.pencolor("green")
     
def exponential_graph(multiplier, devider, color):
    if multiplier > 0:
        turtle.pencolor(color)
        i = 0
        turtle.pendown()
        while turtle.ycor() >= -400 and turtle.xcor() >= -800 and turtle.ycor() <= 400 and turtle.xcor() <= 800:
            turtle.goto(i, (i**multiplier)/devider)
            i += 1
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        i = 0
        
        while turtle.ycor() >= -400 and turtle.xcor() >= -800 and turtle.ycor() <= 400 and turtle.xcor() <= 800:
            turtle.goto(i, (i**multiplier)/devider)
            i -= 1
            
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.pencolor("blue")
    
    
def wave_first_part(stretch, height):
    i = 0
    while turtle.ycor() >= -400 and turtle.xcor() >= -800 and turtle.ycor() <= 400 and turtle.xcor() <= 800:
        turtle.goto(i, height*(math.cos((i + 1)/stretch)))
        i += 1
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    wave_second_part(stretch, height)
        
    
def wave_second_part(stretch, height):
    i = 0
    while turtle.ycor() >= -400 and turtle.xcor() >= -800 and turtle.ycor() <= 400 and turtle.xcor() <= 800:
        turtle.goto(i, height*(math.cos((i - 1)/stretch)))
        i -= 1

    
def wave_sin(stretch, height):
    wave_first_part(stretch, height)
    


wave_sin(10, 100)

#linear_graph(m, n)
#exponential_graph(multiplier, devider)

def extended_cross(x):
    turtle.pencolor("red")
    exponential_graph(x, 100, "red")
    exponential_graph(x, -100, "red")
    exponential_graph(x, 1000, "red")
    exponential_graph(x, -1000, "red")
    turtle.pencolor("blue")



def two_half_circles(repeat):
    exponential_graph(2, 30, "green")
    exponential_graph(2, -30, "green")
    for i in range(repeat):
            exponential_graph(2, (i+1)*100, "green")
    for i in range(repeat):
            exponential_graph(2, ((i+1)*100)*-1, "green")


two_half_circles(15)
#two_half_circles(25)
            
def starting_circle(radius):
    turtle.pencolor("green")
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.pencolor("blue")

def full_start():
    extended_cross(2)
    
    two_half_circles(5)
    
    starting_circle(190)
    starting_circle(300)
    starting_circle(400)

    linear_graph(1, 0)
    linear_graph(-1, 0)
    linear_graph(0.5, 0)
    linear_graph(-0.5, 0)

full_start()


#tkinter stuff

#window = tkinter.Tk()
#window.title("Turtle Control")
#window.geometry("400x80")
#label_one = tkinter.Label(window, text="Use this box to draw lines and shapes on the canvas!").pack()
#label_two = tkinter.Button(window, text="Draw Line", command=linear_graph(1, 0)).pack()




turtle.penup()    
turtle.goto(0, 0)
#window.mainloop()


while True:
    command = input("What do you want to draw?(line/exponential/circle/wave)> ")
    if command == "line":
        linear_graph(float(input("What do you want m to be?> ")), float(input("What do you want n to be?> ")))
    if command == "exponential":
        exponential_graph(float(input("What do you want the multiplier to be?> ")), float(input("What do you want the devider to be?> ")), "blue")
    if command == "circle":
        starting_circle(float(input("What do you want the radius to be?(it will always be centered)> ")))
    if command == "wave":
        wave_sin(input("What do you want the stretch to be?> "), input("What do you want the height to be?> "))