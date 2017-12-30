# coding:gbk
import turtle
import time
def makenumber(p,num,x,y): #显示数字 p：画笔 num：显示的数字 x,y:坐标
    if num==0:
        lst=[1,2,3,4,5,6]
        writenum(p,x,y,lst)
    if num==1:
        lst=[2,3]
        writenum(p,x,y,lst)
    if num==2:
        lst=[1,2,4,5,7]
        writenum(p,x,y,lst)
    if num==3:
        lst=[1,2,3,4,7]
        writenum(p,x,y,lst)
    if num==4:
        lst=[2,3,6,7]
        writenum(p,x,y,lst)
    if num==5:
        lst=[1,3,4,6,7]
        writenum(p,x,y,lst)
    if num==6:
        lst=[1,3,4,5,6,7]
        writenum(p,x,y,lst)
    if num==7:
        lst=[1,2,3]
        writenum(p,x,y,lst)
    if num==8:
        lst=[1,2,3,4,5,6,7]
        writenum(p,x,y,lst)
    if num==9:
        lst=[1,2,3,4,6,7]
        writenum(p,x,y,lst)
def writenum(p,x,y,nlst):   #lst为一个数字的七段数码
    l=50
    for t in nlst:
        p.penup()
        if  t==1:
            p.goto(x,y+2*l)
            p.pendown()
            p.setheading(0)
            p.forward(l)
        if  t==2:
            p.goto(x+l,y+2*l)
            p.pendown()
            p.setheading(270)
            p.forward(l)
        if  t==3:
            p.goto(x+l,y+l)
            p.pendown()
            p.setheading(270)
            p.forward(l)
        if  t==4:
            p.goto(x,y)
            p.pendown()
            p.setheading(0)
            p.forward(l)
        if  t==5:
            p.goto(x,y)
            p.pendown()
            p.setheading(90)
            p.forward(l)
        if  t==6:
            p.goto(x,y+l)
            p.pendown()
            p.setheading(90)
            p.forward(l)
        if  t==7:
            p.goto(x,y+l)
            p.pendown()
            p.setheading(0)
            p.forward(l)
def main():
    p=turtle.Turtle()
    while True:
        p.color("red")
        p.pensize(5)
        p.speed(200)
        p.hideturtle()
        nt=time.strftime("%Y%m%d", time.localtime())
        ti=time.strftime("%H%M%S", time.localtime())
        print nt,ti
        for t in range(8):
            '''
            if t==4:#不知为啥，无法显示字符
                p.write('年',align="center", font=("Courier", 14, "bold"))
            if t==6:
                p.write('月',align="center", font=("Courier", 14, "bold"))
            '''
            makenumber(p,int(nt[t]),-300+t*70,60)
            '''
            if t==7:
                p.write('日',align="center", font=("Courier", 14, "bold"))
            '''
        for t in range(6):
            makenumber(p,int(ti[t]),-260+t*70+(t/2*30),-60)
            if t==1 or t==3:
                p.penup()
                p.goto(-260+t*70+(t/2*30)+74,-45)
                p.pendown()
                p.write(':', move=False, align='center', font=('Arial', 60, 'normal'))
        time.sleep(5)
        p.reset()
        
    turtle.done()
        

main()

