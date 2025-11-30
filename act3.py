import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
pen = turtle.Turtle()
pen.color("black")
pen.speed(5)
def draw_cone(size):
    pen.circle(size, 180)  # Draw the curved surface of the cone
    pen.left(90)
    pen.forward(size)      # Draw the height of the cone
    pen.left(90)
    pen.forward(size)      # Draw the base line to complete the cone
    pen.left(180)          # Reorient the pen for potential further drawing
draw_cone(100)
turtle.done()