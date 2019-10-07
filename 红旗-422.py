from turtle import *
setup(650 , 500 , 75 , 75)

#国旗底
penup()
fd(-155)
seth(90)
fd(110)
seth(0)
color('red' , 'red')
begin_fill()
pendown()
fd(330)
seth(-90)
fd(220)
seth(180)
fd(330)
seth(90)
fd(220)
end_fill()

#大星星
penup()
seth(0)
fd(55)
seth(-90)
fd(22)
seth(-72)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(58)
    right(144)
end_fill()

#小星星1
penup()
seth(0)
fd(66)
seth(-162)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

#小星星2
penup()
seth(-90)
fd(22)
seth(18)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

#小星星3
penup()
seth(-90)
fd(20)
seth(0)
fd(11)
seth(-78)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()

#小星星4
penup()
seth(-90)
fd(40)
seth(180)
fd(30)
seth(58)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(20)
    right(144)
end_fill()
penup()

ht()#隐藏箭头
