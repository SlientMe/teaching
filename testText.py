from turtle import *
penup()
goto(0,-200)
pendown()
circle(200)

penup()
goto(-100,50)
pendown()
begin_fill()
circle(17.5)
end_fill()

penup()
goto(100,50)
pendown()
begin_fill()
circle(17.5)
end_fill()

penup()
goto(0,50)
pendown()
circle(-70,steps=3)

penup()
goto(-150,-70)
pendown()
right(15)
goto(0,-170)
goto(150,-70)

hideturtle()

done()