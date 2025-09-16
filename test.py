import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    
def addsquare():
    y = 5
    for i in range(60):
        square(y)
        t.right(5)
        y=y+5
        t.speed(200)
addsquare()
turtle.done() """

 
""" #float
#bill = 3.14
students = ["cade","mason","andy"]
#can reference each iten in a list by their index
print(students[0]) #prints cade

#add students
students.append("alina")

#we can iterate or loop through a list 
for students in students:
      print(student) """

""" #boolean true or flase 
x = true 
y= False
#evaluations use double ==
if y==true:
      print("hello rodney")
print ("goodbye rodney")
 """
""" x=10
if x<10:
      print("less")
      elife x== 10:
      print("eqaul")
else:
    print ("Greater than 10") """


""" 
students=["cade","mason","andy","alina"]
for student in students:
 found=False
if student=="mason":
 print("Found mason")
found=true """



""" t.speed(200)  # Fastest drawing speed

# Function to draw a square
def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

# Function to draw 60 rotating, growing squares
def spiral_squares():
    length = 5
    for i in range(80):
        draw_square(length)
        t.right(5)
        length += 5

# Call the function
spiral_squares()

# Finish the turtle graphics
turtle.done() """




