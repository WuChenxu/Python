import turtle


def draw_playground(window):
    window.bgcolor("red")

def exit_playground(window): 
    window.exitonclick() 

def draw_square(brad):
    for i in range(4): 
        brad.forward(100)
        brad.right(90)
    
def draw_circle(angie):
    angie.circle(150)

def draw_triangle(monic):
    for i in range(3):
        monic.right(120)
        monic.forward(120)
    
def draw_dimand(alfred):
    alfred.forward(120)
    alfred.right(60)
    alfred.forward(120)
    alfred.right(120)
    alfred.forward(120)
    alfred.right(60)
    alfred.forward(120)
    alfred.right(120)
     
def draw_flower():
    window = turtle.Screen()
    draw_playground(window)
    brad = turtle.Turtle()
    brad.speed(20)
    brad.color("green")
    brad.shape("turtle")
    brad.shapesize(1,1,1)
    for i in range(73):
        draw_dimand(brad)
        brad.right(5)
    exit_playground(window)
    
def draw_art():    
    window = turtle.Screen()
    draw_playground(window)
    brad = turtle.Turtle()
    brad.speed(20)
    brad.color("green")
    brad.shape("turtle")
    brad.shapesize(1,1,1)
    for i in range(37):
        draw_square(brad)
        brad.right(10)
    #draw_circle(brad)
    #draw_triangle(brad)
    exit_playground(window)

draw_flower()
#draw_art()
